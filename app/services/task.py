from sqlalchemy.orm import Session

from app.repositories.task import Taskrepositories
from app.schemas.task import TaskCreateSchema, TaskSchema, TaskUpdateSchema


class TaskNotFound(Exception):
     ...
     

class TaskService:
    def __init__(self, db: Session):
        self.db =db
        self.task_repository = Taskrepositories(db)

    def task_list(self) -> list[TaskSchema]:
        tasks_orm = self.task_repository.get_all()
        return [TaskSchema.model_validate(task) for task in tasks_orm]

    def create_task(self, payload: TaskCreateSchema) -> TaskSchema:
        task_orm = self.task_repository.create(title = payload.title)
        self.db.commit()
        return TaskSchema.model_validate(task_orm)

    def update_task(self, task_id: str, payload: TaskUpdateSchema) -> TaskSchema:
        task_for_update = self.task_repository.get_by_id(task_id)
        if task_for_update is None:
             raise TaskNotFound(" Task not found")
        if payload.title:
                task_for_update.title = payload.title
        if payload.completed is not None:
                task_for_update.completed = payload.completed

        self.db.commit()
        return TaskSchema.model_validate(task_for_update)

    def delete_task(self, task_id: str) -> TaskSchema:
        task_for_delete = self.task_repository.get_by_id(task_id = task_id)
        if task_for_delete is None:
             raise TaskNotFound(" Task not found")
        self.task_repository.delete(task_for_delete)
        self.db.commit()
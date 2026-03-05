##not used anymore
import asyncio
from typing import Awaitable, Callable

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.core.config import settings


def create_scheduler(
        job: Callable[[], Awaitable[None]],
        loop: asyncio.AbstractEventLoop
) -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler(event_loop=loop)
    scheduler.add_job(
        job,
        trigger="interval",
        minutes=settings.parse_schedule_minutes, ##was seconds -> need minutes
        coalesce=True,
        max_instances=1,
    )
    return scheduler

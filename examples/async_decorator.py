import asyncio

from memory_profiler import profile


@profile
@asyncio.coroutine
def foo():
    b = [2] * (2 * 10 ** 7)
    yield from asyncio.sleep(1)
    del b
    return [1] * (10 ** 6)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(foo())

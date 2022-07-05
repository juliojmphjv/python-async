import asyncio
import random


async def fibo(number):
    if number == 0:
        return 0

    if number == 1:
        return 1

    fib1 = await fibo(number - 1)
    fib2 = await fibo(number - 2)

    return fib1 + fib2


async def get_fibo_from_random():
    number = random.randint(0,35)
    result = await asyncio.gather(fibo(number))
    return result

async def main():
    result = await asyncio.gather(*(get_fibo_from_random() for i in range(100)))
    return result

if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)

"""Модуль «Калькулятор комиссий»."""

MIN_AMOUNT = 100
MAX_AMOUNT = 50000

LOW_LIMIT = 1000
MID_LIMIT = 20000
FIXED_LIMIT = 40000

LOW_COMMISSION = 50.0
MID_COMMISSION = 100.0
FIXED_COMMISSION = 500.0


def calculate_commission(amount: int) -> float:
    """
    Рассчитывает комиссию для денежного перевода.

    Args:
        amount (int): Сумма перевода (от 100 до 50 000 руб.)

    Returns:
        float: Размер комиссии

    Raises:
        ValueError: Если сумма не входит в допустимый диапазон
    """
    if not isinstance(amount, (int, float)):
        raise TypeError("Сумма перевода должна быть числом")

    if amount < MIN_AMOUNT or amount > MAX_AMOUNT:
        raise ValueError("Сумма перевода должна быть от 100 до 50 000 руб.")

    if amount <= LOW_LIMIT:
        return LOW_COMMISSION
    if amount <= MID_LIMIT:
        return MID_COMMISSION
    if amount <= FIXED_LIMIT:
        return 200.0 + amount * 0.01
    return FIXED_COMMISSION

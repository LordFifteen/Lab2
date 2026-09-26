"""Модуль «Калькулятор комиссий»."""


def calculate_commission(amount: int) -> float:
    """Рассчитывает комиссию для денежного перевода.

    Args:
        amount (int): Сумма перевода (от 100 до 50 000 руб.)

    Returns:
        float: Размер комиссии

    Raises:
        TypeError: Если сумма не является числом.
        ValueError: Если сумма вне диапазона 100–50 000.
    """
    if not isinstance(amount, (int, float)):
        raise TypeError("Сумма перевода должна быть числом")

    if amount < 100 or amount > 50000:
        raise ValueError("Сумма перевода должна быть от 100 до 50 000 руб.")

    if amount <= 1000:
        return 50.0
    elif amount <= 20000:
        return 100.0
    elif amount <= 40000:
        return 200.0 + amount * 0.01
    else:
        return 500.0

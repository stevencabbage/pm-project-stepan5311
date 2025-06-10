import streamlit as st
import reveal_slides as rs


def presentation_page():
    st.title("Презентация проекта")

    presentation_markdown = """
    # Прогнозирование отказов оборудования

    ---

    ## Введение
    - Цель: предсказать отказ оборудования (Target = 1) или его отсутствие (Target = 0).
    - Датасет: 10,000 записей, 14 признаков (температура, крутящий момент, износ и т.д.).

    ---

    ## Этапы проекта
    1. Загрузка данных.
    2. Предобработка данных.
    3. Обучение модели.
    4. Оценка модели.
    5. Визуализация результатов.

    ---

    ## Предобработка данных
    - Удаление столбцов: `UDI`, `Product ID`, типы отказов (TWF, HDF и т.д.).
    - Кодирование признака `Type` (L→0, M→1, H→2).
    - Масштабирование числовых признаков с помощью `StandardScaler`.

    ---

    ## Модель
    - Алгоритм: **Logistic Regression**.
    - Обучение на 80% данных.
    - Оценка на 20% тестовой выборки.
    - Метрики: Accuracy, Confusion Matrix, Classification Report, ROC-AUC.

    ---

    ## Результаты
    - Accuracy: 0.97
    - ROC-AUC: 0.89

    ---

    ## Интерфейс ввода новых данных
    - Пользователь вручную вводит значения:
        - Тип (L, M, H)
        - Температура воздуха и процесса
        - Скорость вращения
        - Крутящий момент
        - Износ инструмента
    - После ввода отображается:
        - Класс (0 или 1)
        - Вероятность отказа (от 0 до 1)

    ---

    ## Выводы и рекомендации
    - Модель отлично выявляет отказы оборудования.
    - Возможности для улучшения:
        - Добавить другие модели (XGBoost, Random Forest).
        - Реализовать загрузку данных с использованием библиотеки ucimlrepo.

    """

    # Настройки презентации
    with st.sidebar:
        st.header("Настройки презентации")
        theme = st.selectbox("Тема", ["black", "white", "league", "beige",
        "sky", "night", "serif", "simple", "solarized"])
        height = st.number_input("Высота слайдов", value=500)
        transition = st.selectbox("Переход", ["slide", "convex", "concave",
        "zoom", "none"])
        plugins = st.multiselect("Плагины", ["highlight", "katex",
        "mathjax2", "mathjax3", "notes", "search", "zoom"], [])
        # Отображение презентации
    rs.slides(
        presentation_markdown,
        height=height,
        theme=theme,
        config={
            "transition": transition,
            "plugins": plugins,
        },
        markdown_props={"data-separator-vertical": "^--$"},
    )
# 🛠️ Проект: Бинарная классификация для предиктивного обслуживания оборудования

## 🎯 Цель
Разработка ML-модели для прогнозирования отказов промышленного оборудования с выводом в интерактивном Streamlit-приложении.

## 📂 Данные
**Датасет:** [UCI AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/predictive+maintenance+dataset)  
**Характеристики:**
- 10,000 записей
- Признаки: температура, крутящий момент, скорость вращения, износ и др.
- Целевая переменная: `Machine failure` (бинарная)

## 🔧 Техническая реализация
**Модель:** Logistic Regression  
**Метрики:**
- Accuracy: 0.97
- ROC-AUC: 0.89
- Матрица ошибок
- Classification Report

**Предобработка:**
1. Удаление нефункциональных признаков (UDI, Product ID)
2. One-Hot Encoding для категориальных переменных
3. Стандартизация числовых признаков

## 🖥️ Интерфейс
Streamlit-приложение включает:
- Загрузку пользовательских данных
- Визуализацию метрик модели
- Интерактивный ввод параметров оборудования
- Вывод прогноза вероятности отказа

## 🚀 Запуск проекта
```bash
git clone https://github.com/stevencabbage/pm-project-stepan5311.git
cd predictive_maintenance_project
pip install -r requirements.txt
streamlit run app.py
```

## 📹 Демонстрация
[Видео работы приложения](video/demo.mp4)
<video src="video/demo.mp4" controls width="100%" poster="img/preview.jpg"></video>

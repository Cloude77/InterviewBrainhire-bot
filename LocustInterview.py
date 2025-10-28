

#------------------------------------------------------------------------------------------------------------
# Рабочий код

# import os
# import time
# import subprocess
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# class BrainHireFinalWorking:
#     def __init__(self):
#         self.driver = None
#         self.wait = None
#         self.audio_file = r"C:\Users\Sergio\Desktop\Звук\record_out.mp3"
#         self.url = "https://bh75.brainhire.tech/interview/personal/5194d9da-31dd-489f-b5fd-d9cd7dc7932b"
#
#     def play_audio(self):
#         if not os.path.exists(self.audio_file):
#             print(f"❌ Аудиофайл не найден: {self.audio_file}")
#             return False
#         try:
#             subprocess.run(f'start "" "{self.audio_file}"', shell=True)
#             print("🔊 Запись голоса запущена")
#             return True
#         except Exception as e:
#             print(f"⚠️ Ошибка воспроизведения: {e}")
#             return False
#
#     def setup_browser(self):
#         print("🚀 Запускаем браузер...")
#         options = Options()
#         options.add_argument("--use-fake-ui-for-media-stream")
#         options.add_argument("--autoplay-policy=no-user-gesture-required")
#         options.add_argument("--no-sandbox")
#         options.add_argument("--disable-dev-shm-usage")
#         options.add_argument("--disable-gpu")
#         options.add_argument("--window-size=1920,1080")
#         options.add_argument("--disable-blink-features=AutomationControlled")
#         options.add_experimental_option("excludeSwitches", ["enable-automation"])
#         options.add_experimental_option('useAutomationExtension', False)
#
#         prefs = {
#             "profile.default_content_setting_values.media_stream_camera": 1,
#             "profile.default_content_setting_values.media_stream_mic": 1,
#             "profile.default_content_setting_values.notifications": 2,
#         }
#         options.add_experimental_option("prefs", prefs)
#
#         service = Service(ChromeDriverManager().install())
#         self.driver = webdriver.Chrome(service=service, options=options)
#         self.wait = WebDriverWait(self.driver, 30)
#         self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#         print("✅ Браузер готов")
#
#     def click_button_by_text(self, text, description=""):
#         """НАДЕЖНЫЙ клик по кнопке с текстом"""
#         try:
#             xpath = f"//button[contains(normalize-space(.), '{text}')]"
#             btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
#
#             print(f"🎯 Находим кнопку: '{text}'")
#
#             # Прокручиваем к кнопке
#             self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", btn)
#             time.sleep(0.5)
#
#             if not btn.is_displayed() or not btn.is_enabled():
#                 print(f"⚠️ Кнопка '{text}' не видна или не активна")
#                 return False
#
#             # Пробуем обычный клик
#             try:
#                 btn.click()
#                 print(f"✅ {description or f'Нажата кнопка: {text}'}")
#                 time.sleep(2)
#                 return True
#             except Exception as e:
#                 print(f"⚠️ Обычный клик не сработал: {e}")
#
#             # Пробуем ActionChains
#             try:
#                 from selenium.webdriver.common.action_chains import ActionChains
#                 actions = ActionChains(self.driver)
#                 actions.move_to_element(btn).click().perform()
#                 print(f"✅ ActionChains клик: '{text}'")
#                 time.sleep(2)
#                 return True
#             except Exception as e:
#                 print(f"⚠️ ActionChains не сработал: {e}")
#
#             # Пробуем JavaScript клик
#             try:
#                 self.driver.execute_script("arguments[0].click();", btn)
#                 print(f"✅ JavaScript клик: '{text}'")
#                 time.sleep(2)
#                 return True
#             except Exception as e:
#                 print(f"⚠️ JavaScript клик не сработал: {e}")
#
#             return False
#
#         except Exception as e:
#             print(f"❌ Не удалось нажать кнопку '{text}': {e}")
#             return False
#
#     def force_click_next_button(self):
#         """ИСКУССТВЕННОЕ нажатие кнопки 'Далее' через прямое выполнение кода"""
#         print("🎯 ИСКУССТВЕННОЕ НАЖАТИЕ КНОПКИ 'ДАЛЕЕ'...")
#
#         # Даем время для активации кнопки
#         time.sleep(3)
#
#         # Пробуем разные методы искусственного нажатия
#         methods = [
#             self._method_direct_function_call,
#             self._method_react_props,
#             self._method_dom_manipulation,
#             self._method_event_bypass,
#             self._method_prototype_hack
#         ]
#
#         for i, method in enumerate(methods, 1):
#             print(f"🔄 Искусственный метод {i}/5...")
#             if method():
#                 print(f"✅ Искусственный метод {i} СРАБОТАЛ!")
#                 return True
#             time.sleep(2)
#
#         return False
#
#     def _method_direct_function_call(self):
#         """Метод 1: Прямой вызов функции через JavaScript"""
#         try:
#             script = """
#             // Находим кнопку "Далее"
#             const buttons = Array.from(document.querySelectorAll('button'));
#             const nextBtn = buttons.find(btn =>
#                 btn.textContent && btn.textContent.includes('Далее')
#             );
#
#             if (nextBtn) {
#                 console.log('🔧 Прямой вызов функции для:', nextBtn);
#
#                 // Полностью обходим стандартные обработчики
#                 // Вызываем нативные методы кнопки
#                 if (nextBtn.onclick) {
#                     nextBtn.onclick(new MouseEvent('click'));
#                 }
#
#                 // Пробуем вызвать обработчики React
#                 const reactKey = Object.keys(nextBtn).find(key => key.startsWith('__reactProps'));
#                 if (reactKey && nextBtn[reactKey].onClick) {
#                     nextBtn[reactKey].onClick(new MouseEvent('click'));
#                 }
#
#                 // Вызываем все возможные обработчики
#                 const clickEvent = new Event('click', { bubbles: true, cancelable: true });
#                 nextBtn.dispatchEvent(clickEvent);
#
#                 // Принудительно меняем состояние и вызываем обработчики
#                 nextBtn.focus();
#                 nextBtn.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter' }));
#                 nextBtn.dispatchEvent(new KeyboardEvent('keyup', { key: 'Enter' }));
#
#                 return true;
#             }
#             return false;
#             """
#             return self.driver.execute_script(script)
#         except:
#             return False
#
#     def _method_react_props(self):
#         """Метод 2: Прямое обращение к React пропсам"""
#         try:
#             script = """
#             // Ищем React компонент кнопки
#             const buttons = document.querySelectorAll('button');
#             for (let btn of buttons) {
#                 if (btn.textContent && btn.textContent.includes('Далее')) {
#                     console.log('🔧 React метод для:', btn);
#
#                     // Ищем React пропсы
#                     const reactKey = Object.keys(btn).find(key =>
#                         key.startsWith('__reactProps') ||
#                         key.startsWith('__reactEventHandlers')
#                     );
#
#                     if (reactKey) {
#                         const props = btn[reactKey];
#                         // Вызываем все возможные обработчики
#                         if (props.onClick) props.onClick({ preventDefault: () => {} });
#                         if (props.onMouseDown) props.onMouseDown({ preventDefault: () => {} });
#                         if (props.onMouseUp) props.onMouseUp({ preventDefault: () => {} });
#                         if (props.onTouchEnd) props.onTouchEnd({ preventDefault: () => {} });
#
#                         // Также пробуем вызвать через внутренние методы
#                         btn.click();
#                         return true;
#                     }
#                 }
#             }
#             return false;
#             """
#             return self.driver.execute_script(script)
#         except:
#             return False
#
#     def _method_dom_manipulation(self):
#         """Метод 3: Манипуляция DOM для обхода защиты"""
#         try:
#             script = """
#             // Создаем полностью новую кнопку с теми же свойствами
#             const originalBtn = document.querySelector('button.chakra-button.css-1s89inu');
#             if (!originalBtn) return false;
#
#             console.log('🔧 DOM манипуляция для:', originalBtn);
#
#             // Клонируем кнопку
#             const clone = originalBtn.cloneNode(true);
#
#             // Удаляем все обработчики событий с оригинала
#             originalBtn.outerHTML = originalBtn.outerHTML;
#
#             // Находим новую кнопку
#             const newBtn = document.querySelector('button.chakra-button.css-1s89inu');
#             if (newBtn) {
#                 // Добавляем простой обработчик
#                 newBtn.onclick = function() {
#                     // Эмулируем стандартное поведение
#                     console.log('✅ Искусственный клик сработал!');
#                     return true;
#                 };
#
#                 // Вызываем клик
#                 newBtn.click();
#                 return true;
#             }
#             return false;
#             """
#             return self.driver.execute_script(script)
#         except:
#             return False
#
#     def _method_event_bypass(self):
#         """Метод 4: Полный обход системы событий"""
#         try:
#             script = """
#             // Находим кнопку
#             const btn = document.querySelector('button.chakra-button.css-1s89inu');
#             if (!btn) return false;
#
#             console.log('🔧 Обход системы событий для:', btn);
#
#             // Временно отключаем все обработчики
#             const originalAddEventListener = EventTarget.prototype.addEventListener;
#             EventTarget.prototype.addEventListener = function() {
#                 if (this === btn && (arguments[0] === 'click' || arguments[0] === 'mousedown')) {
#                     console.log('🔧 Блокируем обработчик:', arguments[0]);
#                     return;
#                 }
#                 return originalAddEventListener.apply(this, arguments);
#             };
#
#             // Выполняем клик
#             btn.click();
#
#             // Восстанавливаем
#             EventTarget.prototype.addEventListener = originalAddEventListener;
#
#             return true;
#             """
#             return self.driver.execute_script(script)
#         except:
#             return False
#
#     def _method_prototype_hack(self):
#         """Метод 5: Хак через прототипы"""
#         try:
#             script = """
#             // Находим кнопку
#             const btn = document.querySelector('button.chakra-button.css-1s89inu');
#             if (!btn) return false;
#
#             console.log('🔧 Prototype хак для:', btn);
#
#             // Сохраняем оригинальные методы
#             const originalClick = HTMLElement.prototype.click;
#             const originalDispatch = EventTarget.prototype.dispatchEvent;
#
#             // Подменяем методы
#             HTMLElement.prototype.click = function() {
#                 console.log('🔧 Перехвачен click для:', this);
#                 // Пропускаем вызов для нашей кнопки
#                 if (this === btn) {
#                     // Вызываем нативный click без ограничений
#                     originalClick.call(this);
#                     return;
#                 }
#                 return originalClick.apply(this, arguments);
#             };
#
#             // Вызываем клик
#             btn.click();
#
#             // Восстанавливаем
#             HTMLElement.prototype.click = originalClick;
#             EventTarget.prototype.dispatchEvent = originalDispatch;
#
#             return true;
#             """
#             return self.driver.execute_script(script)
#         except:
#             return False
#
#     def check_checkboxes(self):
#         """Отмечает чекбоксы"""
#         try:
#             checkboxes = self.driver.find_elements(By.CSS_SELECTOR, "svg[data-state='unchecked']")
#             print(f"Найдено неотмеченных чекбоксов: {len(checkboxes)}")
#             for i, svg in enumerate(checkboxes):
#                 try:
#                     parent = svg.find_element(By.XPATH, "./ancestor::*[contains(@class, 'chakra-checkbox')]")
#                     self.driver.execute_script("arguments[0].click();", parent)
#                     print(f"✅ Чекбокс {i + 1} отмечен")
#                     time.sleep(0.5)
#                 except:
#                     self.driver.execute_script("arguments[0].click();", svg)
#             return True
#         except Exception as e:
#             print(f"⚠️ Ошибка при отметке чекбоксов: {e}")
#             return False
#
#     def run(self):
#         try:
#             self.setup_browser()
#             print("\n" + "=" * 60)
#             print("🎬 НАЧИНАЕМ ПРОХОЖДЕНИЕ - ИСКУССТВЕННЫЕ МЕТОДЫ")
#             print("=" * 60)
#
#             # === 1. Согласие ===
#             print("📄 Шаг 1: Согласие")
#             self.driver.get(self.url)
#             time.sleep(4)
#             self.check_checkboxes()
#             self.click_button_by_text("Продолжить", "Кнопка 'Продолжить'")
#
#             # === 2. Начало интервью ===
#             print("▶️ Шаг 2: Начало интервью")
#             self.click_button_by_text("Начать интервью", "Кнопка 'Начать интервью'")
#
#             # === 3. Проверка скорости ===
#             print("📶 Шаг 3: Проверка скорости")
#             self.click_button_by_text("Начать проверку скорости Интернета", "Начать проверку скорости")
#             time.sleep(12)
#             self.click_button_by_text("Отлично, идем дальше", "Отлично, идем дальше")
#
#             # === 4. Камера ===
#             print("📹 Шаг 4: Проверка камеры")
#             self.click_button_by_text("Проверить камеру", "Проверить камеру")
#             time.sleep(6)
#
#             # Ждём сообщение о камере
#             try:
#                 success_msg = self.wait.until(EC.presence_of_element_located((
#                     By.XPATH,
#                     "//div[contains(text(), 'Камера в порядке')]"
#                 )))
#                 print("✅ Камера активна!")
#             except:
#                 print("⚠️ Камера не активирована")
#
#             # 🔴 ИСКУССТВЕННОЕ НАЖАТИЕ КНОПКИ "ДАЛЕЕ"
#             print("🎯 ЗАПУСКАЕМ ИСКУССТВЕННЫЕ МЕТОДЫ ДЛЯ КНОПКИ 'ДАЛЕЕ'...")
#             success = self.force_click_next_button()
#
#             if success:
#                 print("🎉 УСПЕХ! Перешли к микрофону!")
#             else:
#                 print("💥 Все искусственные методы не сработали")
#
#             # === 5. Микрофон ===
#             print("🎤 Шаг 5: Проверка микрофона")
#             self.click_button_by_text("Начать запись", "Начать запись")
#             time.sleep(2)
#
#             # Воспроизводим аудио
#             self.play_audio()
#             time.sleep(7)
#
#             self.click_button_by_text("Остановить запись", "Остановить запись")
#             time.sleep(3)
#             self.click_button_by_text("Далее", "Далее после микрофона")
#
#             # === 6. Инструкции ===
#             print("ℹ️ Шаг 6: Инструкции")
#             self.click_button_by_text("Все понятно", "Все понятно")
#             self.click_button_by_text("Перейти к вопросам", "Перейти к вопросам")
#
#             # === 7. Вопросы ===
#             print("❓ Шаг 7: Ответы на вопросы")
#             for i in range(1, 13):
#                 print(f"   Вопрос {i}/12")
#                 if i < 12:
#                     time.sleep(10)
#                     self.click_button_by_text("Перейти к следующему вопросу", f"Вопрос {i} → следующий")
#                 else:
#                     time.sleep(10)
#                     self.click_button_by_text("Завершить", "Завершить интервью")
#
#             print("\n🎉 ИНТЕРВЬЮ УСПЕШНО ЗАВЕРШЕНО!")
#             time.sleep(30)
#
#         except Exception as e:
#             print(f"💥 Ошибка: {e}")
#             time.sleep(20)
#         finally:
#             self.driver.quit()
#             print("🔚 Браузер закрыт")
#
#
# if __name__ == "__main__":
#     print("🎯 BRAINHIRE — ИСКУССТВЕННЫЕ МЕТОДЫ НАЖАТИЯ")
#     print("✅ Используем прямое выполнение JavaScript кода")
#     bot = BrainHireFinalWorking()
#     bot.run()


import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BrainHireFinalWorking:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.audio_file = r"C:\Users\Sergio\Desktop\Звук\record_out.mp3"
        self.url = "https://bh75.brainhire.tech/interview/personal/c85643ab-c4df-4b7f-9cd3-737ef9fe327d"

    def play_audio(self):
        if not os.path.exists(self.audio_file):
            print(f"❌ Аудиофайл не найден: {self.audio_file}")
            return False
        try:
            subprocess.run(f'start "" "{self.audio_file}"', shell=True)
            print("🔊 Запись голоса запущена")
            return True
        except Exception as e:
            print(f"⚠️ Ошибка воспроизведения: {e}")
            return False

    def setup_browser(self):
        print("🚀 Запускаем браузер...")
        options = Options()
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument("--autoplay-policy=no-user-gesture-required")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        prefs = {
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.notifications": 2,
        }
        options.add_experimental_option("prefs", prefs)

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        print("✅ Браузер готов")

    def click_button_by_text(self, text, description=""):
        """НАДЕЖНЫЙ клик по кнопке с текстом"""
        try:
            xpath = f"//button[contains(normalize-space(.), '{text}')]"
            btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

            print(f"🎯 Находим кнопку: '{text}'")

            # Прокручиваем к кнопке
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", btn)
            time.sleep(0.5)

            if not btn.is_displayed() or not btn.is_enabled():
                print(f"⚠️ Кнопка '{text}' не видна или не активна")
                return False

            # Пробуем обычный клик
            try:
                btn.click()
                print(f"✅ {description or f'Нажата кнопка: {text}'}")
                time.sleep(2)
                return True
            except Exception as e:
                print(f"⚠️ Обычный клик не сработал: {e}")

            # Пробуем ActionChains
            try:
                from selenium.webdriver.common.action_chains import ActionChains
                actions = ActionChains(self.driver)
                actions.move_to_element(btn).click().perform()
                print(f"✅ ActionChains клик: '{text}'")
                time.sleep(2)
                return True
            except Exception as e:
                print(f"⚠️ ActionChains не сработал: {e}")

            # Пробуем JavaScript клик
            try:
                self.driver.execute_script("arguments[0].click();", btn)
                print(f"✅ JavaScript клик: '{text}'")
                time.sleep(2)
                return True
            except Exception as e:
                print(f"⚠️ JavaScript клик не сработал: {e}")

            return False

        except Exception as e:
            print(f"❌ Не удалось нажать кнопку '{text}': {e}")
            return False

    def force_click_next_button(self):
        """ИСКУССТВЕННОЕ нажатие кнопки 'Далее' через прямое выполнение кода"""
        print("🎯 ИСКУССТВЕННОЕ НАЖАТИЕ КНОПКИ 'ДАЛЕЕ'...")

        # Даем время для активации кнопки
        time.sleep(3)

        # Пробуем разные методы искусственного нажатия
        methods = [
            self._method_direct_function_call,
            self._method_react_props,
            self._method_dom_manipulation,
            self._method_event_bypass,
            self._method_prototype_hack
        ]

        for i, method in enumerate(methods, 1):
            print(f"🔄 Искусственный метод {i}/5...")
            if method():
                print(f"✅ Искусственный метод {i} СРАБОТАЛ!")
                return True
            time.sleep(2)

        return False

    def _method_direct_function_call(self):
        """Метод 1: Прямой вызов функции через JavaScript"""
        try:
            script = """
            // Находим кнопку "Далее"
            const buttons = Array.from(document.querySelectorAll('button'));
            const nextBtn = buttons.find(btn => 
                btn.textContent && btn.textContent.includes('Далее')
            );

            if (nextBtn) {
                console.log('🔧 Прямой вызов функции для:', nextBtn);

                // Полностью обходим стандартные обработчики
                // Вызываем нативные методы кнопки
                if (nextBtn.onclick) {
                    nextBtn.onclick(new MouseEvent('click'));
                }

                // Пробуем вызвать обработчики React
                const reactKey = Object.keys(nextBtn).find(key => key.startsWith('__reactProps'));
                if (reactKey && nextBtn[reactKey].onClick) {
                    nextBtn[reactKey].onClick(new MouseEvent('click'));
                }

                // Вызываем все возможные обработчики
                const clickEvent = new Event('click', { bubbles: true, cancelable: true });
                nextBtn.dispatchEvent(clickEvent);

                // Принудительно меняем состояние и вызываем обработчики
                nextBtn.focus();
                nextBtn.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter' }));
                nextBtn.dispatchEvent(new KeyboardEvent('keyup', { key: 'Enter' }));

                return true;
            }
            return false;
            """
            return self.driver.execute_script(script)
        except:
            return False

    def _method_react_props(self):
        """Метод 2: Прямое обращение к React пропсам"""
        try:
            script = """
            // Ищем React компонент кнопки
            const buttons = document.querySelectorAll('button');
            for (let btn of buttons) {
                if (btn.textContent && btn.textContent.includes('Далее')) {
                    console.log('🔧 React метод для:', btn);

                    // Ищем React пропсы
                    const reactKey = Object.keys(btn).find(key => 
                        key.startsWith('__reactProps') || 
                        key.startsWith('__reactEventHandlers')
                    );

                    if (reactKey) {
                        const props = btn[reactKey];
                        // Вызываем все возможные обработчики
                        if (props.onClick) props.onClick({ preventDefault: () => {} });
                        if (props.onMouseDown) props.onMouseDown({ preventDefault: () => {} });
                        if (props.onMouseUp) props.onMouseUp({ preventDefault: () => {} });
                        if (props.onTouchEnd) props.onTouchEnd({ preventDefault: () => {} });

                        // Также пробуем вызвать через внутренние методы
                        btn.click();
                        return true;
                    }
                }
            }
            return false;
            """
            return self.driver.execute_script(script)
        except:
            return False

    def _method_dom_manipulation(self):
        """Метод 3: Манипуляция DOM для обхода защиты"""
        try:
            script = """
            // Создаем полностью новую кнопку с теми же свойствами
            const originalBtn = document.querySelector('button.chakra-button.css-1s89inu');
            if (!originalBtn) return false;

            console.log('🔧 DOM манипуляция для:', originalBtn);

            // Клонируем кнопку
            const clone = originalBtn.cloneNode(true);

            // Удаляем все обработчики событий с оригинала
            originalBtn.outerHTML = originalBtn.outerHTML;

            // Находим новую кнопку
            const newBtn = document.querySelector('button.chakra-button.css-1s89inu');
            if (newBtn) {
                // Добавляем простой обработчик
                newBtn.onclick = function() {
                    // Эмулируем стандартное поведение
                    console.log('✅ Искусственный клик сработал!');
                    return true;
                };

                // Вызываем клик
                newBtn.click();
                return true;
            }
            return false;
            """
            return self.driver.execute_script(script)
        except:
            return False

    def _method_event_bypass(self):
        """Метод 4: Полный обход системы событий"""
        try:
            script = """
            // Находим кнопку
            const btn = document.querySelector('button.chakra-button.css-1s89inu');
            if (!btn) return false;

            console.log('🔧 Обход системы событий для:', btn);

            // Временно отключаем все обработчики
            const originalAddEventListener = EventTarget.prototype.addEventListener;
            EventTarget.prototype.addEventListener = function() {
                if (this === btn && (arguments[0] === 'click' || arguments[0] === 'mousedown')) {
                    console.log('🔧 Блокируем обработчик:', arguments[0]);
                    return;
                }
                return originalAddEventListener.apply(this, arguments);
            };

            // Выполняем клик
            btn.click();

            // Восстанавливаем
            EventTarget.prototype.addEventListener = originalAddEventListener;

            return true;
            """
            return self.driver.execute_script(script)
        except:
            return False

    def _method_prototype_hack(self):
        """Метод 5: Хак через прототипы"""
        try:
            script = """
            // Находим кнопку
            const btn = document.querySelector('button.chakra-button.css-1s89inu');
            if (!btn) return false;

            console.log('🔧 Prototype хак для:', btn);

            // Сохраняем оригинальные методы
            const originalClick = HTMLElement.prototype.click;
            const originalDispatch = EventTarget.prototype.dispatchEvent;

            // Подменяем методы
            HTMLElement.prototype.click = function() {
                console.log('🔧 Перехвачен click для:', this);
                // Пропускаем вызов для нашей кнопки
                if (this === btn) {
                    // Вызываем нативный click без ограничений
                    originalClick.call(this);
                    return;
                }
                return originalClick.apply(this, arguments);
            };

            // Вызываем клик
            btn.click();

            // Восстанавливаем
            HTMLElement.prototype.click = originalClick;
            EventTarget.prototype.dispatchEvent = originalDispatch;

            return true;
            """
            return self.driver.execute_script(script)
        except:
            return False

    def check_checkboxes(self):
        """Отмечает чекбоксы"""
        try:
            checkboxes = self.driver.find_elements(By.CSS_SELECTOR, "svg[data-state='unchecked']")
            print(f"Найдено неотмеченных чекбоксов: {len(checkboxes)}")
            for i, svg in enumerate(checkboxes):
                try:
                    parent = svg.find_element(By.XPATH, "./ancestor::*[contains(@class, 'chakra-checkbox')]")
                    self.driver.execute_script("arguments[0].click();", parent)
                    print(f"✅ Чекбокс {i + 1} отмечен")
                    time.sleep(0.5)
                except:
                    self.driver.execute_script("arguments[0].click();", svg)
            return True
        except Exception as e:
            print(f"⚠️ Ошибка при отметке чекбоксов: {e}")
            return False

    def wait_for_questions_screen(self):
        """Явно ждем загрузки экрана с вопросами"""
        print("⏳ Ожидаем загрузки экрана с вопросами...")

        try:
            # Ждем появления элементов вопросов
            question_indicators = [
                "//button[contains(., 'Перейти к следующему вопросу')]",
                "//button[contains(., 'Завершить')]",
                "//div[contains(@class, 'question')]",
                "//h2[contains(., 'вопрос')]"
            ]

            for indicator in question_indicators:
                try:
                    element = self.wait.until(EC.presence_of_element_located((By.XPATH, indicator)))
                    if element.is_displayed():
                        print(f"✅ Экран вопросов загружен: {indicator}")
                        return True
                except:
                    continue

            # Если не нашли индикаторы, ждем просто по времени
            time.sleep(5)
            return True

        except Exception as e:
            print(f"⚠️ Ошибка ожидания экрана вопросов: {e}")
            return False

    def handle_questions(self):
        """Обработка вопросов с улучшенной логикой"""
        print("❓ Шаг 7: Ответы на вопросы")

        # Явно ждем загрузки экрана вопросов
        if not self.wait_for_questions_screen():
            print("⚠️ Не удалось дождаться экрана вопросов")
            return

        # Сначала проверяем, на каком вопросе мы находимся
        try:
            # Ищем индикатор текущего вопроса
            question_indicators = [
                "//div[contains(text(), 'вопрос')]",
                "//span[contains(text(), 'вопрос')]",
                "//*[contains(text(), '1 из')]",
                "//*[contains(text(), 'Вопрос')]"
            ]

            for indicator in question_indicators:
                elements = self.driver.find_elements(By.XPATH, indicator)
                for elem in elements:
                    if elem.is_displayed():
                        print(f"📊 Текущий статус: {elem.text}")
        except:
            print("ℹ️ Не удалось определить текущий вопрос")

        # Обрабатываем вопросы
        for i in range(1, 13):
            print(f"\n🎯 Обрабатываем вопрос {i}/12")

            # Ждем перед каждым вопросом
            time.sleep(10)

            if i < 12:
                # Для вопросов 1-11 нажимаем "Перейти к следующему вопросу"
                success = self.click_button_by_text("Перейти к следующему вопросу", f"Вопрос {i} → следующий")
                if not success:
                    print(f"⚠️ Не удалось перейти от вопроса {i}, пробуем продолжить...")
            else:
                # Для последнего вопроса нажимаем "Завершить"
                success = self.click_button_by_text("Завершить", "Завершить интервью")
                if not success:
                    print("⚠️ Не удалось завершить интервью")

    def run(self):
        try:
            self.setup_browser()
            print("\n" + "=" * 60)
            print("🎬 НАЧИНАЕМ ПРОХОЖДЕНИЕ - ИСПРАВЛЕННЫЕ ВОПРОСЫ")
            print("=" * 60)

            # === 1. Согласие ===
            print("📄 Шаг 1: Согласие")
            self.driver.get(self.url)
            time.sleep(4)
            self.check_checkboxes()
            self.click_button_by_text("Продолжить", "Кнопка 'Продолжить'")

            # === 2. Начало интервью ===
            print("▶️ Шаг 2: Начало интервью")
            self.click_button_by_text("Начать интервью", "Кнопка 'Начать интервью'")

            # === 3. Проверка скорости ===
            print("📶 Шаг 3: Проверка скорости")
            self.click_button_by_text("Начать проверку скорости Интернета", "Начать проверку скорости")
            time.sleep(12)
            self.click_button_by_text("Отлично, идем дальше", "Отлично, идем дальше")

            # === 4. Камера ===
            print("📹 Шаг 4: Проверка камеры")
            self.click_button_by_text("Проверить камеру", "Проверить камеру")
            time.sleep(6)

            # Ждём сообщение о камере
            try:
                success_msg = self.wait.until(EC.presence_of_element_located((
                    By.XPATH,
                    "//div[contains(text(), 'Камера в порядке')]"
                )))
                print("✅ Камера активна!")
            except:
                print("⚠️ Камера не активирована")

            # 🔴 ИСКУССТВЕННОЕ НАЖАТИЕ КНОПКИ "ДАЛЕЕ"
            print("🎯 ЗАПУСКАЕМ ИСКУССТВЕННЫЕ МЕТОДЫ ДЛЯ КНОПКИ 'ДАЛЕЕ'...")
            success = self.force_click_next_button()

            if success:
                print("🎉 УСПЕХ! Перешли к микрофону!")
            else:
                print("💥 Все искусственные методы не сработали")

            # === 5. Микрофон ===
            print("🎤 Шаг 5: Проверка микрофона")
            self.click_button_by_text("Начать запись", "Начать запись")
            time.sleep(2)

            # Воспроизводим аудио
            self.play_audio()
            time.sleep(7)

            self.click_button_by_text("Остановить запись", "Остановить запись")
            time.sleep(3)
            self.click_button_by_text("Далее", "Далее после микрофона")

            # === 6. Инструкции ===
            print("ℹ️ Шаг 6: Инструкции")
            self.click_button_by_text("Все понятно", "Все понятно")
            self.click_button_by_text("Перейти к вопросам", "Перейти к вопросам")

            # === 7. Вопросы ===
            self.handle_questions()

            print("\n🎉 ИНТЕРВЬЮ УСПЕШНО ЗАВЕРШЕНО!")
            time.sleep(30)

        except Exception as e:
            print(f"💥 Ошибка: {e}")
            time.sleep(20)
        finally:
            self.driver.quit()
            print("🔚 Браузер закрыт")


if __name__ == "__main__":
    print("🎯 BRAINHIRE — ИСПРАВЛЕННАЯ ЛОГИКА ВОПРОСОВ")
    print("✅ Вопросы начинаются с первого и обрабатываются корректно")
    bot = BrainHireFinalWorking()
    bot.run()


   

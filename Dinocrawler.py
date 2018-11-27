class Game: 
    def __init__(self, custom_config=True):
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars")
        self._driver = webdriver.Chrome(executable_path = chrome_driver_path, chrome_options=chrome_options)
        self._driver.set_window_position(x=-10,y=0)
        self._driver.set_window_size(200, 300)
        self._driver.get(os.path.abspath(game_url))
        if custom_config:
            self._driver.execute_script("Runner.config.ACCELERATION=0")
        def get_crashed(self):
            return self._driver.execute_script("return Runner.instance_.crashed")
        def get_playing(self):
            return self._driver.execute_script("return Runner.instance_.playing")
        def restart(self):
            self._driver.execute_script("runner.instance_.restart()")


            time.sleep(0.25)

        def press_down(self):
            self._driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_DOWN)
        def press_up(self):
            self._driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_UP)
        def get_score(self):
            score_array = self._driver.execute_script("return Runner.instance_.distanceMeter.digits")
            score = ''.join(score_array)
            return int(score)
        def pause(self):
            return self._driver.execute_script("return Runner.instance_.stop()")
        def resume(self):
            return self._driver.execute_script("return Runner.instance_.play()")
        def end(self):
            self._driver.close()

class Dino:
    def __init__(self, game):
        self._game = game;
        self.jump();
        time.sleep(.5)
    def is_running(self)
        return self._game.get_playing()
    def is_crashed(self)
        return self._game.get_crasehd()
    def jump(self)
        return self._game.press_up()
    def duck(self)
        return self._game.press_down()

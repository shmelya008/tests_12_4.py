from rt_with_exceptions import Runner
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            r1 = Runner('Serge', -5)
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            r2 = Runner(123)
            for i in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r1 = Runner('Serge')
        r2 = Runner('Alex')
        for i in range(10):
            r1.walk()
        for j in range(10):
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

if __name__ == '__main__':
    unittest.main()

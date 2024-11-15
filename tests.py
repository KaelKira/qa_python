class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    #проверка условия что не добавляется книга больше 40 символов (41)
    def test_add_new_book_add_book_with_long_name_false(self, collector):
        collector.add_new_book('12345678901234567890123456789012345678901')
        assert len(collector.books_genre) == 0

    # проверка условия что не добавляется книга c 0 символов
    def test_add_new_book_add_book_with_zero_name_false(self, collector):
        collector.add_new_book('')
        assert len(collector.books_genre) == 0

    # проверка условия что не добавляется дубль книги с уже существующим названием
    def test_add_new_book_add_book_with_same_name_false(self, collector):
        collector.add_new_book('Книги с одинаковым названием')
        collector.add_new_book('Книги с одинаковым названием')
        assert len(collector.books_genre) == 1

    # проверка книга добавилась с нужным именем
    def test_add_new_book_add_book_right_name_right_texting(self, collector):
        name = 'Над пропастью во ржи'
        collector.add_new_book(name)
        assert  list(collector.books_genre.keys())[0] == name

    # проверка книга добавилась с пустым жанром
    def test_add_new_book_right_name_empty_genre(self, collector):
        name = 'Над пропастью во ржи'
        collector.add_new_book(name)
        assert collector.books_genre[name] == ''

    #позитивный тест добавления жанра книге
    def test_set_book_genre_existing_genre_succesfully_added(self, collector):
        name = 'Планета обезьян'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    #негативный тест книга не в списке
    def test_set_book_genre_no_name_book_empty_str(self, collector):
        name = 'Планета обезьян'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre('Гарри Поттер', genre)
        assert collector.books_genre[name] == ''

    # негативный тест жанр не в списке
    def test_set_book_genre_no_name_genre_empty_str(self, collector):
        name = 'Планета обезьян'
        genre = 'Сатира'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == ''

    # получаем жанр книги по её имени, книга с жанром существует
    def test_get_book_genre_book_with_genre_existed_true(self, collector):
        name = 'Планета обезьян'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        assert collector.get_book_genre(name) == 'Фантастика'

    # получаем жанр книги по её имени, нет книги
    def test_get_book_genre_book_not_existed_false(self, collector):
        name = 'Планета обезьян'
        assert collector.get_book_genre(name) == None

    # получаем жанр книги по её имени, нет жанра у книги
    def test_get_book_genre_genre_not_existed_false(self, collector):
        name = 'Планета обезьян'
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''

    # выводим список книг с определённым жанром, выпадает нужная книга
    def test_get_books_with_specific_genre_ganre_and_book_existing_geted_book(self, collector):
        collector.add_new_book('Планета обезьян')
        collector.set_book_genre('Планета обезьян', 'Фантастика')
        collector.add_new_book('Худеющий')
        collector.set_book_genre('Худеющий', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы')[0] == 'Худеющий'

    # выводим список книг с определённым жанром выпадает только одна книга
    def test_get_books_with_specific_genre_ganre_and_book_existing_geted_one_book(self, collector):
        collector.add_new_book('Планета обезьян')
        collector.set_book_genre('Планета обезьян', 'Фантастика')
        collector.add_new_book('Худеющий')
        collector.set_book_genre('Худеющий', 'Ужасы')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 1

    # выводим список книг с определённым жанром, жанр отсутствует
    def test_get_books_with_specific_genre_no_genre_existing_geted_zero(self, collector):
        collector.add_new_book('Планета обезьян')
        collector.set_book_genre('Планета обезьян', 'Фантастика')
        collector.add_new_book('Худеющий')
        collector.set_book_genre('Худеющий', 'Ужасы')
        assert len(collector.get_books_with_specific_genre('Научпоп')) == 0

    # выводим список книг с определённым жанром, книга отсутствует
    def test_get_books_with_specific_genre_no_book_existing_geted_zero(self, collector):
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 0

    # получаем словарь books_genre если нет книг
    def test_get_books_genre_comparison_empty_books_true(self,collector):
        assert collector.get_books_genre() == {}

    # получаем словарь books_genre если книги есть
    def test_get_books_genre_comparison_book_existed_true(self,collector):
        collector.add_new_book('Планета обезьян')
        collector.set_book_genre('Планета обезьян', 'Фантастика')
        collector.add_new_book('Худеющий')
        collector.set_book_genre('Худеющий', 'Ужасы')
        assert collector.get_books_genre() == {'Планета обезьян' : 'Фантастика','Худеющий' : 'Ужасы'}

    # возвращаем книги, подходящие детям
    def test_get_books_for_children_right_book_true(self, collector):
        collector.add_new_book('Планета обезьян')
        collector.set_book_genre('Планета обезьян', 'Фантастика')
        collector.add_new_book('Худеющий')
        collector.set_book_genre('Худеющий', 'Ужасы')
        assert collector.get_books_for_children()[0] == 'Планета обезьян'

    # возвращаем книги, подходящие детям, отсутствие книг не подходящих детям
    def test_get_books_for_children_book_with_out_of_genre_only_one_book(self, collector):
        collector.add_new_book('Планета обезьян')
        collector.set_book_genre('Планета обезьян', 'Фантастика')
        collector.add_new_book('Золотая рыбка')
        collector.set_book_genre('Золотая рыбка', 'Сказки')
        assert len(collector.get_books_for_children()) == 1

    # возвращаем книги, подходящие детям, отсутствуют книги в списке
    def test_get_books_for_children_no_books_empty(self, collector):
        assert collector.get_books_for_children() == []

    # добавляем книгу в Избранное
    def test_add_book_in_favorites_ther_is_a_book_true(self, collector):
        name = 'Планета обезьян'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books()[0] == name

    # добавляем книгу в Избранное, которая уже была в избранном
    def test_add_book_in_favorites_double_operation_only_one_book_added(self, collector):
        name = 'Планета обезьян'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1

    # добавляем книгу в Избранное, которой вообще нет
    def test_add_book_in_favorites_no_book_at_all_empty_list(self, collector):
        name = 'Планета обезьян'
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_book_removed(self, collector):
        name = 'Планета обезьян'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    def test_delete_book_from_favorites_book_not_in_favorites(self, collector):
        collector.delete_book_from_favorites('No_name_book')
        assert 'No_name_book' not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Планета обезьян')
        collector.add_new_book('Худеющий')
        collector.add_book_in_favorites('Планета обезьян')
        collector.add_book_in_favorites('Худеющий')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Планета обезьян', 'Худеющий']
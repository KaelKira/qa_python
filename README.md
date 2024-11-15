# qa_python

## Добавленные тесты
- test_add_new_book_add_two_books: позитивный кейс - добавляем две книги
- test_add_new_book_add_book_with_long_name_false: проверка условия что не добавляется книга больше 40 символов (41)
- test_add_new_book_add_book_with_zero_name_false: проверка условия что не добавляется книга с 0 символов
- test_add_new_book_add_book_with_same_name_false: проверка условия что не добавляется дубль книги с уже существующим названием
- test_add_new_book_add_book_right_name_right_texting: проверка книга добавилась с нужным именем
- test_add_new_book_right_name_empty_genre: проверка книга добавилась с пустым жанром
- test_set_book_genre_existing_genre_succesfully_added: позитивный тест добавления жанра книге
- test_set_book_genre_no_name_book_empty_str: негативный тест книга не в списке
- test_set_book_genre_no_name_genre_empty_str: негативный тест жанр не в списке
- test_get_book_genre_book_with_genre_existed_true: получаем жанр книги по её имени, книга с жанром существует
- test_get_book_genre_book_not_existed_false: получаем жанр книги по её имени, нет книги
- test_get_book_genre_genre_not_existed_false: получаем жанр книги по её имени, нет жанра у книги
- test_get_books_with_specific_genre_ganre_and_book_existing_geted_book: выводим список книг с определённым жанром, выпадает нужная книга
- test_get_books_with_specific_genre_ganre_and_book_existing_geted_one_book: выводим список книг с определённым жанром выпадает только одна книга
- test_get_books_with_specific_genre_no_genre_existing_geted_zero: выводим список книг с определённым жанром, жанр отсутствует
- test_get_books_with_specific_genre_no_book_existing_geted_zero: выводим список книг с определённым жанром, книга отсутствует
- test_get_books_genre_comparison_empty_books_true: получаем словарь books_genre если нет книг
- test_get_books_genre_comparison_book_existed_true: получаем словарь books_genre если книги есть
- test_get_books_for_children_right_book_true: возвращаем книги, подходящие детям
- test_get_books_for_children_book_with_out_of_genre_only_one_book: возвращаем книги, подходящие детям, отсутствие книг не подходящих детям
- test_get_books_for_children_no_books_empty: возвращаем книги, подходящие детям, отсутствуют книги в списке
- test_add_book_in_favorites_ther_is_a_book_true: добавляем книгу в Избранное
- test_add_book_in_favorites_double_operation_only_one_book_added: добавляем книгу в Избранное, которая уже была в избранном
- test_add_book_in_favorites_no_book_at_all_empty_list: добавляем книгу в Избранное, которой вообще нет
- test_delete_book_from_favorites_book_removed: позитивный кейс удаления книги из избранного
- test_delete_book_from_favorites_book_not_in_favorites: пытаемся удалить книгу из избранного, которой нет в избранном (ничего не происходит)
- test_get_list_of_favorites_books: — получаем список книг в избранном
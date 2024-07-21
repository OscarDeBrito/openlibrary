import unittest
from unittest.mock import patch, MagicMock
from openlibrary.tests.views import get_trending_books 

class TestGetTrendingBooks(unittest.TestCase):

    @patch('your_module.Bookshelves.fetch')
    @patch('your_module.Bookshelves.most_logged_books')
    @patch('your_module.dateutil.todays_date_minus')
    
    def test_get_trending_books_now(self, mock_todays_date_minus, mock_most_logged_books, mock_fetch):
        mock_fetch.return_value = [{'work': 'Book 1'}, {'work': 'Book 2'}]
        mock_most_logged_books.return_value = [{'work': 'Book 1'}, {'work': 'Book 2'}]

        result = get_trending_books(since_days=0, since_hours=0, books_only=True)
        self.assertEqual(result, ['Book 1', 'Book 2'])

        result = get_trending_books(since_days=0, since_hours=0, books_only=False)
        self.assertEqual(result, [{'work': 'Book 1'}, {'work': 'Book 2'}])

    @patch('your_module.Bookshelves.fetch')
    @patch('your_module.Bookshelves.most_logged_books')
    @patch('your_module.dateutil.todays_date_minus')
    
    def test_get_trending_books_with_date(self, mock_todays_date_minus, mock_most_logged_books, mock_fetch):
        mock_todays_date_minus.return_value = 'mocked_date'
        mock_most_logged_books.return_value = [{'work': 'Book 3'}, {'work': 'Book 4'}]

        result = get_trending_books(since_days=1, books_only=True)
        self.assertEqual(result, ['Book 3', 'Book 4'])

        result = get_trending_books(since_days=1, books_only=False)
        self.assertEqual(result, [{'work': 'Book 3'}, {'work': 'Book 4'}])

    @patch('your_module.Bookshelves.fetch')
    @patch('your_module.Bookshelves.most_logged_books')
    @patch('your_module.dateutil.todays_date_minus')
    
    def test_get_trending_books_with_minimum(self, mock_todays_date_minus, mock_most_logged_books, mock_fetch):
        # Mocking the return values
        mock_todays_date_minus.return_value = 'mocked_date'
        mock_most_logged_books.return_value = [{'work': 'Book 5'}, {'work': 'Book 6'}]

        result = get_trending_books(since_days=1, minimum=10, books_only=True)
        self.assertEqual(result, ['Book 5', 'Book 6'])

        result = get_trending_books(since_days=1, minimum=10, books_only=False)
        self.assertEqual(result, [{'work': 'Book 5'}, {'work': 'Book 6'}])

if __name__ == '__main__':
    unittest.main()

from .models import Author, Book, Genre, Language

# Add Genres
fantasy = Genre.objects.create(name="Fantasy")
science_fiction = Genre.objects.create(name="Science Fiction")
romance = Genre.objects.create(name="Romance")
classics = Genre.objects.create(name="Classics")
adventure = Genre.objects.create(name="Adventure")

# Add Languages
english = Language.objects.create(name="English")
russian = Language.objects.create(name="Russian")

# Add Authors
tolkien = Author.objects.create(first_name="J.R.R.", last_name="Tolkien")
orwell = Author.objects.create(first_name="George", last_name="Orwell")
austen = Author.objects.create(first_name="Jane", last_name="Austen")
dostoevsky = Author.objects.create(first_name="Fyodor", last_name="Dostoevsky")
lee = Author.objects.create(first_name="Harper", last_name="Lee")

# Add Books
Book.objects.create(
    title="The Hobbit",
    author=tolkien,
    summary="A fantasy novel following Bilbo Baggins on an unexpected adventure to help dwarves reclaim their kingdom.",
    isbn="9780547928227",
    language=english,
).genre.set([fantasy, adventure])

Book.objects.create(
    title="1984",
    author=orwell,
    summary="A dystopian novel about a totalitarian regime that suppresses free thought.",
    isbn="9780451524935",
    language=english,
).genre.set([science_fiction])

Book.objects.create(
    title="Pride and Prejudice",
    author=austen,
    summary="A romantic novel exploring the social customs and relationships in early 19th century England.",
    isbn="9780141199078",
    language=english,
).genre.set([romance, classics])

Book.objects.create(
    title="Crime and Punishment",
    author=dostoevsky,
    summary="A psychological drama about a man’s struggle with guilt after committing murder.",
    isbn="9780486415871",
    language=russian,
).genre.set([classics])

Book.objects.create(
    title="To Kill a Mockingbird",
    author=lee,
    summary="A novel about racial injustice in the American South during the 1930s.",
    isbn="9780061120084",
    language=english,
).genre.set([classics, adventure])

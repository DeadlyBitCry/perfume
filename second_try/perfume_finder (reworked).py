import pandas as pd


# Загрузка базы парфюмов их csv файла.  Loading perfume base from CSV
def base_load():
    return pd.read_csv("perfume_base(2).csv")


# Функция поиска по нотам.  Function of searching by notes
def search_via_notes(df, notes):
    notes = [n.strip().lower() for n in notes.split(",")]
    result = []
    for _, row in df.iterrows():
        perfume_notes = [n.strip().lower() for n in row["notes"].split(",")]
        if all(note in perfume_notes for note in notes):
            result.append(row)
    return pd.DataFrame(result)


# Функция поиска по бренду.  Function of searching by brand
def search_via_brand(df, brands):
    brands_to_find = [b.strip().lower() for b in brands.split(",")]
    return df[df["brand"].str.lower().isin(brands_to_find)]


# Функция поиска по полу.  Function of searching by gender
def search_via_gender(df, genders):
    genders_to_find = [g.strip().lower() for g in genders.split(",")]
    return df[df["gender"].apply
              (lambda x: all
               (g in [item.strip().lower() for item in x.split(",")] for
                g in genders_to_find))]


# Функция поиска по сезону. Function of searching by season
def search_via_season(df, seasons):
    seasons_to_find = [s.strip().lower() for s in seasons.split(",")]
    return df[df["season"].apply
              (lambda x:
               all(s in [item.strip().lower()
                         for item in x.split(",")] for s in seasons_to_find))]


# Словарь с переменными по которым можно искать парфюмы.
# Dictionary with variables by which is possible to search perfume.
search_dictionary = {
    "ноты": search_via_notes,
    "бренд": search_via_brand,
    "гендер": search_via_gender,
    "сезон": search_via_season
    }


# Главная функция.  Main function
def main():
    df = base_load()
    print("Доступен поиск по: нотам, бренду, гендеру, сезону \n")
    aspect = input("Введите аспект поиска: ")
    if aspect not in search_dictionary:
        print("Такого аспекта нет")
        return
    search = input(f"Что вы ищете по {aspect}: ")
    result = search_dictionary[aspect](df, search)
    if not result.empty:
        print("\nРезультаты:")
        print(result[["name", "brand", "notes"]])
    else:
        print("Ничего не найдено")


if __name__ == "__main__":
    main()

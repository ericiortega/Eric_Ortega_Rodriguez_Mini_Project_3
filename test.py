from main import load_dataset, grab_mean, grab_median, grab_std, grab_max

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/drug-use-by-age/drug-use-by-age.csv"

df1 = load_dataset()


def test_load_dataset():
    assert len(df1) == 17


def test_grab_mean():
    assert grab_mean(df1, "marijuana_use") <= 120


def test_grab_median():
    assert grab_median(df1, "marijuana_use") <= 90


def test_grab_std():
    assert grab_std(df1, "marijuana_use") <= 60


def test_grab_max():
    assert grab_max(df1, "marijuana_use") <= 78
    assert grab_max(df1, "marijuana_use") > 30


if __name__ == "__main__":
    test_load_dataset()
    test_grab_mean()
    test_grab_median()
    test_grab_std()
    test_grab_max()

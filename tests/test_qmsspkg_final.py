from qmsspkg_final import qmsspkg_final

def test_get_best_team():
    example_stats = 'Batting_Average'
    expected = ['Guardians']
    actual = qmsspkg_final.get_best_teams(example_stats)
    assert actual == expected
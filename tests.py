from game_of_life import Cell


def test_living_cell_die_of_underpopulation():
    living_cell = Cell(alive=True)
    living_cell._neighbours = 1
    living_cell.set_state()
    assert living_cell._alive == False

def test_living_cell_survive_with_2_neighbours():
    living_cell = Cell(alive=True)
    living_cell._neighbours = 2
    living_cell.set_state()
    assert living_cell._alive == True

def test_living_cell_survive_with_3_neighbours():
    living_cell = Cell(alive=True)
    living_cell._neighbours = 3
    living_cell.set_state()
    assert living_cell._alive == True

def test_living_cell_die_of_overpopulation():
    living_cell = Cell(alive=True)
    living_cell._neighbours = 4
    living_cell.set_state()
    assert living_cell._alive == False

def test_dead_cell_become_alive():
    dead_cell = Cell(alive=False)
    dead_cell._neighbours = 3
    dead_cell.set_state()
    assert dead_cell._alive == True

def test_dead_cell_stay_dead_with_less_than_3_neighbours():
    dead_cell = Cell(alive=False)
    dead_cell._neighbours = 3
    dead_cell.set_state()
    assert dead_cell._alive == True

if __name__ == "__main__":
    test_living_cell_die_of_underpopulation()
    test_living_cell_survive_with_2_neighbours()
    test_living_cell_survive_with_3_neighbours()
    test_living_cell_die_of_overpopulation()
    test_dead_cell_become_alive()
    test_dead_cell_stay_dead_with_less_than_3_neighbours()

    print("Everything passed")
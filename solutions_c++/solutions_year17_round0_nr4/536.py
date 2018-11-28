#include <vector>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout

using namespace std;  // since cin and cout are both in namespace std, this saves some text

char grid[100][100];

void reset() {
	for (size_t i = 0; i < 100; i++) {
		for (size_t j = 0; j < 100; j++) {
			grid[i][j] = '.';
		}
	}
}
bool isValid(size_t size) {
	// check every row
	for (size_t i = 0; i < size; i++) {
		for (size_t j = 0; j < size; j++) {
			if (grid[i][j] != '.') {
				for (size_t k = j + 1; k < size; k++) {
					if (grid[i][k] != '.') {
						if (grid[i][j] != '+' && grid[i][k] != '+') {
							//cout << "row " << i << " " << j << " " << k << endl;
							return false;
						}
					}
				}
			}
		}
	}
	// check every column
	for (size_t i = 0; i < size; i++) {
		for (size_t j = 0; j < size; j++) {
			if (grid[i][j] != '.') {
				for (size_t k = i + 1; k < size; k++) {
					if (grid[k][j] != '.') {
						if (grid[i][j] != '+' && grid[k][j] != '+') {
							//cout << "col " << i << " " << j << " " << k << endl;
							return false;
						}
					}
				}
			}
		}
	}
	// check every main diagonal
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			if (grid[i][j] != '.') {
				for (int k = i + 1, l = j - 1; k < size && l >= 0; k++, l--) {
					if (grid[k][l] != '.') {
						if (grid[i][j] != 'x' && grid[k][l] != 'x') {
							//cout << "main " << i << " " << j << " " << k << " " << l << endl;
							return false;
						}
					}
				}
			}
		}
	}
	// check every cross diagonal
	for (size_t i = 0; i < size; i++) {
		for (size_t j = 0; j < size; j++) {
			if (grid[i][j] != '.') {
				for (size_t k = i + 1, l = j + 1; k < size && l < size; k++, l++) {
					if (grid[k][l] != '.') {
						if (grid[i][j] != 'x' && grid[k][l] != 'x') {
							//cout << "cross " << i << " " << j << " " << k << " " << l << endl;
							return false;
						}
					}
				}
			}
		}
	}

	return true;
}
void output(size_t size) {
	for (size_t i = 0; i < size; i++) {
		for (size_t j = 0; j < size; j++) {
			cout << grid[i][j];
		}
		cout << endl;
	}
	cout << endl;
}
size_t computeValue(size_t size) {
	size_t value = 0;
	for (size_t i = 0; i < size; i++) {
		for (size_t j = 0; j < size; j++) {
			if (grid[i][j] == '+' || grid[i][j] == 'x') {
				value += 1;
			}
			if (grid[i][j] == 'o') {
				value += 2;
			}
		}
	}
	return value;
}
struct Change {
	char model;
	size_t row;
	size_t col;
};
void computeGeneral(size_t testCase, size_t size) {
	//if (size == 1) {
	//	if (grid[0][0] == '.' || grid[0][0] == '+' || grid[0][0] == 'x') {
	//		cout << "Case #" << testCase << ": 2 1" << endl;
	//		cout << "o 1 1" << endl;
	//	} else {
	//		cout << "Case #" << testCase << ": 2 0" << endl;
	//	}
	//} else {
		vector<Change> changes(0);
		for (size_t i = 0; i < size; i++) {
			for (size_t j = 0; j < size; j++) {
				if (grid[i][j] != '.' && grid[i][j] != 'o') {
					char temp = grid[i][j];
					grid[i][j] = 'o';
					if (!isValid(size)) {
						grid[i][j] = temp;
					} else {
						changes.push_back({ 'o', i + 1, j + 1 });
					}
				}
			}
		}

		// test some changes
		for (size_t i = 0; i < size; i++) {
			for (size_t j = 0; j < size; j++) {
				if (grid[i][j] == '.') {
					grid[i][j] = 'x';
					if (!isValid(size)) {
						// only place + on the boarders
						if (i == size - 1 || i == 0 || j == size - 1 || j == 0) {
							grid[i][j] = '+';
							if (!isValid(size)) {
								grid[i][j] = '.';
							} else {
								changes.push_back({ '+', i + 1, j + 1 });
							}
						} else {
							grid[i][j] = '.';
						}
					} else {
						changes.push_back({'x', i+1, j+1});
					}
				}
			}
		}

		// check o or place one
		//bool found = false;
		//for (size_t i = 0; i < size; i++) {
		//	for (size_t j = 0; j < size; j++) {
		//		if (grid[i][j] == 'o') {
		//			found = true;
		//			break;
		//		}
		//	}
		//}
		//if (!found) {
			for (size_t i = 0; i < size; i++) {
				for (size_t j = 0; j < size; j++) {
					if (grid[i][j] != '.' && grid[i][j] != 'o') {
						char temp = grid[i][j];
						grid[i][j] = 'o';
						if (!isValid(size)) {
							grid[i][j] = temp;
						} else {
							// check for placed model
							bool update = false;
							for (Change& c : changes) {
								if (c.row == i + 1 && c.col == j + 1) {
									update = true;
									c.model = 'o';
									break;
								}
							}
							if (!update) {
								changes.push_back({ 'o', i + 1, j + 1 });
							}
							//break;
						}
					}
				}
			}
		//}

		// compute value
		size_t value = computeValue(size);

		cout << "Case #" << testCase+1 << ": " << value << " " << changes.size() << endl;
		//if (size == 1) {
		//	if (value != 2) cout << "ERROR" << endl;
		//} else {
		//	if (value != size * 3 - 2) cout << "ERROR" << endl;
		//}
		for (const Change& c : changes) {
			cout << c.model << " " << c.row << " " << c.col << endl;
		}
	//}
}
void main() {
	size_t testCount;
	cin >> testCount;

	size_t gridSize, placedModels;
	for (size_t i = 0; i < testCount; i++) {
		cin >> gridSize >> placedModels;

		reset();

		char model;
		int row, column;
		for (size_t j = 0; j < placedModels; j++) {
			cin >> model >> row >> column;
			grid[row-1][column-1] = model;
		}
		
		//cout << gridSize << endl;
		//output(gridSize);

		computeGeneral(i, gridSize);

		//output(gridSize);

		//if (isValid(gridSize)) {
		//	cout << "grid is valid" << endl;
		//} else {
		//	cout << "grid is not valid" << endl;
		//}

		//cout << "---------------" << endl;
	}
}
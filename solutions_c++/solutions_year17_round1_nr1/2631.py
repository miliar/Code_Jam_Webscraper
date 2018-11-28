#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <utility>

enum DIRECTION { HORIZONTAL, VERTICAL };

struct POS { int x, y; };

struct GPS { DIRECTION d; POS p; };

std::string print_cake(char ** cake, const int &R, const int &C) {
	std::string s = "";

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			s += cake[i][j];
		}
		s += '\n';
	}

	return s;
}

void flip(std::map<char, GPS> &m, int index) {
	std::map<char, GPS>::iterator it = m.begin();
	std::advance(it, index);
	switch (it->second.d)
	{
	case HORIZONTAL:
		it->second.d = VERTICAL;
		break;
	case VERTICAL:
		it->second.d = HORIZONTAL;
		break;
	default:
		std::cerr << "ERROR";
		break;
	}
}

void cut_cake(char ** cake, const int &R, const int &C) {
	std::map<char, GPS> directions;

	int n_qms = 0, placed_qms = 0, old_qms, flipper = -1;
	int i, j;
	for (i = 0; i < R; i++) {
		for (j = 0; j < C; j++) {
			if (cake[i][j] == '?') {
				n_qms++;
			}
		}
	}

	while (placed_qms < n_qms) {
		old_qms = placed_qms;

		for (i = 0; i < R; i++) {
			for (j = 0; j < C; j++) {
				if (cake[i][j] != '?') {
					if (directions.find(cake[i][j]) == directions.end()) {
						directions.insert(std::pair<char, GPS>(cake[i][j], { HORIZONTAL, {i, j} }));
					}

					switch (directions[1].d)
					{
					case HORIZONTAL:
						if (j >= -1 && j < C-1 && cake[i][j + 1] == '?') {
							cake[i][j + 1] = cake[i][j];
							placed_qms++;
						}
						if (j > 0 && j <= C && cake[i][j - 1] == '?') {
							cake[i][j - 1] = cake[i][j];
							placed_qms++;
						}
						break;
					case VERTICAL:
						if (i >= -1 && i < R - 1 && cake[i + 1][j] == '?') {
							cake[i + 1][j] = cake[i][j];
							placed_qms++;
						}
						if (i > 0 && i <= R && cake[i - 1][j] == '?') {
							cake[i - 1][j] = cake[i][j];
							placed_qms++;
						}
						break;
					default:
						std::cerr << "ERROR";
						break;
					}
				}

				else {
					if (j - 1 >= 0 && j - 1 < C && cake[i][j - 1] != '?' && directions[cake[i][j - 1]].d == HORIZONTAL) {
						cake[i][j] = cake[i][j - 1];
						placed_qms++;
					}

					if (j + 1 >= 0 && j + 1 < C && cake[i][j + 1] != '?' && directions[cake[i][j + 1]].d == HORIZONTAL) {
						cake[i][j] = cake[i][j + 1];
						placed_qms++;
					}

					if (i - 1 >= 0 && i - 1 < R  && cake[i - 1][j] != '?' && directions[cake[i - 1][j]].d == VERTICAL) {
						cake[i][j] = cake[i - 1][j];
						placed_qms++;
					}

					if (i + 1 >= 0 && i + 1 < R  && cake[i + 1][j] != '?' && directions[cake[i + 1][j]].d == VERTICAL) {
						cake[i][j] = cake[i + 1][j];
						placed_qms++;
					}
				}
			}
		}

		if (placed_qms == old_qms) {
			flip(directions, (++flipper) % (directions.size() - 1));
		}
	}
}

int main() {
	std::string filename = "Sample";
	std::ifstream fin(filename + ".in");
	std::ofstream fout(filename + ".out");

	if (!fin.is_open() || !fout.is_open()) return -2;

	int N_CASES;
	fin >> N_CASES;
	
	char ** cake = nullptr;
	int R, C;
	int i, j, k;
	for (i = 1; i <= N_CASES; i++) {
		if (cake != nullptr) {
			for (j = 0; j < R; j++) {
				delete[] cake[j];
			}
			delete[] cake;
		}

		fin >> R >> C;

		cake = new char* [R];
		for (j = 0; j < R; j++) cake[j] = new char[C];

		for (j = 0; j < R; j++) {
			for (k = 0; k < C; k++) {
				fin >> cake[j][k];
			}
		}

		std::cout << print_cake(cake, R, C);

		fout << "Case #" << i << ":\n";
		cut_cake(cake, R, C);
		fout << print_cake(cake, R, C);
	}

	return 0;
}
#include <iostream>
#include <fstream>
#include <vector>
#include <ctype.h>

#define TYPE(x) ((x) == '+' ? 1 : ((x) == 'x' ? 2 : 3))

struct pose {
	char type;
	int x;
	int y;
};

int main(int argc, char* argv[]) {
	if (argc <= 1)
		return -1;

	std::ifstream input_file;
	std::ofstream output_file("output");

	input_file.open(argv[1]);

	int T;
	input_file >> T;
	for (int t = 1; t <= T; t++) {
		int R, C;
		input_file >> R;
		input_file >> C;

		char* grid = new char[R * C];
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				char n = 0;
				while (!isprint(n))
					input_file >> n;

				grid[r * C + c] = n;
			}
		}

		for (int r = 0; r < R; r++) {
			char last = 0;
			for (int c = 0; c < C; c++) {
				if (grid[r * C + c] == '?') {
					if (last == 0) {
						for (int i = c + 1; i < C; i++) {
							if (grid[r * C + c + i] != '?') {
								last = grid[r * C + c + i];
								break;
							}
						}
					}
					if (last != 0) {
						grid[r * C + c] = last;
					}
					else {
						break;
					}
				}
				else {
					last = grid[r * C + c];
				}
			}
		}

		for (int r = 0; r < R; r++) {
			if (grid[r * C] != '?')
				continue;

			if (r > 0) {
				for (int c = 0; c < C; c++)
					grid[r * C + c] = grid[(r - 1) * C + c];
			}
			else {
				int i;
				for (i = r + 1; i < R; i++) {
					if (grid[i * C] != '?')
						break;
				}
				for (int c = 0; c < C; c++)
					grid[r * C + c] = grid[i * C + c];
			}
		}
		
		output_file << "Case #" << t << ":" << std::endl;

		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				output_file << grid[r * C + c];
			}
			output_file << std::endl;
		}
	}

	return 0;
}
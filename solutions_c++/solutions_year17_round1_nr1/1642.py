#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int main() {

	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("output.txt");

	int t;
	input >> t;
	for (int i = 0;i < t;i++) {

		char arr[25][25];

		int r, c;
		input >> r >> c;
		output << "Case #" << i + 1 << ":" << endl;
		for (int y = 0;y < r;y++) {
			for (int x = 0;x < c;x++) {
				char c;
				input >> c;
				arr[y][x] = c;
				if (c == '?' && x!=0) {
					if (arr[y][x - 1] != '?') {
						arr[y][x] = arr[y][x - 1];
					}
				}
			}
		}

		for (int y = 0;y < r;y++) {
			for (int x = c-1;x >= 0;x--) {
				if (arr[y][x] == '?' && x != c-1) {
					if (arr[y][x + 1] != '?') {
						arr[y][x] = arr[y][x + 1];
					}
				}
			}
		}
		
		for (int y = 1;y < r;y++) {
			for (int x = 0;x < c;x++) {
				if (arr[y][x] == '?') {
					if (arr[y-1][x] != '?') {
						arr[y][x] = arr[y-1][x];
					}
				}
			}
		}

		for (int y = r-2;y >= 0;y--) {
			for (int x = 0;x < c;x++) {
				if (arr[y][x] == '?') {
					if (arr[y + 1][x] != '?') {
						arr[y][x] = arr[y + 1][x];
					}
				}
			}
		}

		for (int y = 0;y < r;y++) {
			for (int x = 0;x < c;x++) {
				output << arr[y][x];
			}
			output << endl;
		}
		
	}

	return 0;
}
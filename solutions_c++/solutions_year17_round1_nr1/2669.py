#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

class Problem1 {
public:
	Problem1(string input_file, string output_file) {

		fs.open(input_file, std::fstream::in);
		ofs.open(output_file);
	}
	~Problem1() {
		fs.close();
		ofs.close();
	}
	void Problem1::run() {
		char line[1024];
		int idx = 0;
		int q = 0;
		char cc;
		fs >> q;
		for (idx = 1; idx <= q; idx++) {
			int R, C;
			string matrix[100];
			fs >> R >> C;
			fs.getline(line, 1024);
			for (int i = 0; i < R; i++) {
				fs.getline(line, 1024);
				string row_str(line);
				matrix[i] = row_str;
			}
			findCakeAlloc(matrix, R, C);
			ofs << "Case #" << idx << ":" << endl;
			for (int i = 0; i < R; i++) {
				ofs << matrix[i].c_str() << endl;
			}
		}
	}
private:
	fstream fs;
	ofstream ofs;
	struct init_info {
		int up, bottom, left, right;
		bool found;
	};
	void Problem1::findCakeAlloc(string *matrix, int R, int C) {
		struct init_info hash[26];
		memset(hash, 0, sizeof(hash));
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				int hash_val = matrix[i][j] - 'A';
				if (matrix[i][j] != '?') {
					if (hash[hash_val].found == false) {
						hash[hash_val].found = 1;
						hash[hash_val].up = i;
						hash[hash_val].bottom = i;
						hash[hash_val].left = j;
						hash[hash_val].right = j;
					}
					else {
						hash[hash_val].bottom = hash[hash_val].bottom < i ? i : hash[hash_val].bottom;
						hash[hash_val].left = hash[hash_val].left > i ? i : hash[hash_val].left;
						hash[hash_val].right = hash[hash_val].right < i ? i : hash[hash_val].right;
					}
				}
			}
		}
		for (int ii = 0; ii < 26; ii++) {
			if (hash[ii].found == false) continue;
			int up = hash[ii].up, bottom = hash[ii].bottom, left = hash[ii].left, right = hash[ii].right;
			for (int i = up; i <= bottom; i++) {
				for (int j = left; j <= right; j++) {
					matrix[i][j] = char('A' + ii);
				}
			}
			for (int i = up - 1; i >= 0; i--) {
				bool filled = true;
				for (int j = left; j <= right; j++) {
					if (matrix[i][j] != '?') {
						filled = false;
						break;
					}
				}
				if (filled) {
					for (int j = left; j <= right; j++) {
						matrix[i][j] = char('A' + ii);
					}
					hash[ii].up = i;
				}
				else {
					break;
				}
			}
			for (int i = bottom + 1; i < R; i++) {
				bool filled = true;
				for (int j = left; j <= right; j++) {
					if (matrix[i][j] != '?') {
						filled = false;
						break;
					}
				}
				if (filled) {
					for (int j = left; j <= right; j++) {
						matrix[i][j] = char('A' + ii);
					}
					hash[ii].bottom = i;
				}
				else {
					break;
				}
			}
			
		}
		for (int ii = 0; ii < 26; ii++) {
			if (hash[ii].found == false) continue;
			int up = hash[ii].up, bottom = hash[ii].bottom, left = hash[ii].left, right = hash[ii].right;
			for (int j = left - 1; j >= 0; j--) {
				bool filled = true;
				for (int i = up; i <= bottom; i++) {
					if (matrix[i][j] != '?') {
						filled = false;
						break;
					}
				}
				if (filled) {
					for (int i = up; i <= bottom; i++) {
						matrix[i][j] = char('A' + ii);
					}
					hash[ii].left = j;
				}
				else {
					break;
				}
			}
			for (int j = right + 1; j < C; j++) {
				bool filled = true;
				for (int i = up; i <= bottom; i++) {
					if (matrix[i][j] != '?') {
						filled = false;
						break;
					}
				}
				if (filled) {
					for (int i = up; i <= bottom; i++) {
						matrix[i][j] = char('A' + ii);
					}
					hash[ii].right = j;
				}
				else {
					break;
				}
			}
		}
	}
};

int main()
{
	Problem1 p1("A-small-attempt1.in", "out.txt");
	p1.run();
}

#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>

using namespace std;


struct inp_t {
	int x;
	int y;
	char ch[25][25];

	void print() {
		for(int i = 0; i < x; ++i) {
			for(int j = 0; j < y; ++j) {
				cout << ch[i][j];
			}
			cout << "\n";
		}
	}
};

void fillup(inp_t &inp, int i, int j);

string solve(inp_t & inp) {

//	inp.print();

	std::stringstream sr;
	sr << "\n";

	set<char> used;

	for(int i = 0; i < inp.x; ++i) {
		for (int j = 0; j < inp.y; ++j) {
			const char c = inp.ch[i][j];
			if ( c != '?' ) {
				if (used.find(c) == used.end()) {
					used.insert(c);
					fillup(inp, i, j);
				}
			}
		}
	}
	for(int i = 0; i < inp.x; ++i) {
		for(int j = 0; j < inp.y; ++j) {
			sr << inp.ch[i][j];
		}
		if (i < inp.x-1) sr << "\n";
	}
	return sr.str();
}

void fillup(inp_t &inp, int i, int j) {
	char ch = inp.ch[i][j];
	int x0 = i;
	int x1 = i;
	int y0 = j;
	int y1 = j;
//cout << "fillup" << endl;
	while(true) {
//		cout << x0 << "," << y0 << " " << x1 << "," << y1 << endl;
//		inp.print();
		// up
		bool quit = true;
		if (y0 > 0) {
			bool find = false;
			for(int l = x0; l <= x1; ++l) {
				if (inp.ch[l][y0-1]!='?') {
					find = true;
				}
			}
			if (!find) {
//				cout << ch << " UP\n";
				for(int l = x0; l <= x1; ++l) {
					inp.ch[l][y0-1]=ch;
				}
				quit = false;
				--y0;
				continue;
			}
		}

		if (x0 > 0) {
			bool find = false;
			for(int l = y0; l <= y1; ++l) {
				if (inp.ch[x0-1][l]!='?') {
					find = true;
				}
			}
			if (!find) {
//				cout << ch << " LEFT\n";
				for(int l = y0; l <= y1; ++l) {
					inp.ch[x0-1][l]=ch;
				}
				quit = false;
				--x0;
				continue;
			}
		}

		if (y1 < inp.y-1) {
			bool find = false;
			for(int l = x0; l <= x1; ++l) {
				if (inp.ch[l][y1+1]!='?') {
					find = true;
				}
			}
			if (!find) {
//				cout << ch << " DOWN\n";
				for(int l = x0; l <= x1; ++l) {
					inp.ch[l][y1+1]=ch;
				}
				quit = false;
				++y1;
				continue;
			}
		}

		if (x1 < inp.x-1) {
			bool find = false;
			for(int l = y0; l <= y1; ++l) {
				if (inp.ch[x1+1][l]!='?') {
					find = true;
				}
			}
			if (!find) {
//				cout << ch << " RIGHT\n";
				for(int l = y0; l <= y1; ++l) {
					inp.ch[x1+1][l]=ch;
				}
				quit = false;
				++x1;
				continue;
			}
		}


		if (quit)
			break;
	}
}

int main() {
	int n;
	cin >> n;
	string x;
	getline(cin, x);
	for (int l = 1; l <= n; ++l) {
		inp_t inp;
		getline(cin, x);
		stringstream ss(x);
		ss >> inp.x >> inp.y;
		for(int i = 0; i < inp.x; ++i) {
			getline(cin, x);
			for(int j = 0; j < inp.y; ++j) {
				inp.ch[i][j]=x[j];
			}
		}
		cout << "Case #" << l << ": " << solve(inp) << endl;
	}
	return 0;
}
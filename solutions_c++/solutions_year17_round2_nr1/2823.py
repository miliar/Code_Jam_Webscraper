#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

using namespace std;

typedef pair<int, int> pii;
typedef long long i64;
typedef vector<i64> vi64;
typedef pair<i64, i64> pi64;
typedef vector<int> vi;
typedef vector<char> vc;
typedef vector<vc> vvc;
typedef vector<pii> vpi;
typedef vector<pi64> vpi64;
typedef vector<vi> vvi;
typedef vector<vi64> vvi64;
typedef double ld;
typedef vector<ld> vd;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("Results.txt");
	fout.precision(9);

	if (!fin) {
		cout << "Error reading input file." << endl;
		return -1;
	}
	else if (!fout) {
		cout << "Error reading output file." << endl;
		return -1;
	}
	else {
		char line[101];
		fin.getline(line, (int)101);
		int t = stoi(line);
		for (int T = 0; T < t; T++) {
			fin.getline(line, (int)101,' ');
			ld D = (ld)stoi(line);
			fin.getline(line, (int)101);
			int N = stoi(line);
			ld speed = 1000000000000000;
			for (int i = 0; i < N; i++) {
				fin.getline(line, (int)101, ' ');
				ld Ki = (ld)stoi(line);
				fin.getline(line, (int)101);
				ld Si = (ld)stoi(line);
				if (D / ((D - Ki) / Si) < speed) {
					speed = D / ((D - Ki) / Si);
				}
			}
			fout << "Case #" << T + 1 << ": " << std::fixed << speed << endl;
		}
	}

	fin.close();
	fout.close();

	return 0;
}
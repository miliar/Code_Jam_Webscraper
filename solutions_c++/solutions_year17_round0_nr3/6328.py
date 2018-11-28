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

int main() {
	ifstream fin("C-small-2-attempt0.in");
	ofstream fout("Results.txt");

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
			fin.getline(line, (int)101, ' ');
			long long N = stoll(line);
			fin.getline(line, (int)101);
			long long K = stoll(line);
			long long Kin = K;
			long long high = 0;
			long long low = 0;
			long long max;
			long long min;
			int count = 0;
			int rem = 0;
			rem = (N-1) % 2;
			N = (N-1) >> 1;
			high = rem ? 1 : 0;
			low = 2 - high;
			K = K - pow(2, count++);
			while (K) {
				K = K - pow(2, count++);
				if (K < 1) {
					break;
				}
				rem = (N-1) % 2;
				N = (N-1) >> 1;
				high = rem ? (2 * high + low) : high;
				low = rem ? low : (2 * low + high);
			}
			K = K + pow(2, count - 1);
			if (N == 0 && Kin == 1) {
				max = rem ? 1 : 0;
				min = 0;
			} else if (Kin == 1) {
				max = N+rem;
				min = N;
			} else if (K > high) {
				max = N >> 1;
				min = (N % 2) ? N >> 1 : (N - 1) >> 1;
			}
			else {
				max = (N + 1) >> 1;
				min = N >> 1;
			}
			fout << "Case #" << T + 1 << ": " << max << ' ' << min << endl;
		}
	}

	fin.close();
	fout.close();

	return 0;
}
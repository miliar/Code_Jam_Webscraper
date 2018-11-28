#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cassert>
#include <iomanip>
#include <algorithm>
using namespace std;

using ll = long long int;
ifstream fin("1.in");
ofstream fout("1.out");

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		int N, P;
		fin >> N >> P;
		int counts[4] = {};
		for (int i = 0; i < N; i++) {
			int tmp;
			fin >> tmp;
			counts[tmp % P]++;
		}
		int answer = counts[0], rem;
		switch (P) {
		case 2:
			answer += (counts[1] + 1) / 2;
			break;
		case 3:
			answer += min(counts[2], counts[1]);
			rem = max(counts[2], counts[1]) - min(counts[2], counts[1]);
			answer += (rem + 2) / 3;
			break;
		case 4:
			answer += counts[2] / 2;
			answer += min(counts[3], counts[1]);
			rem = max(counts[3], counts[1]) - min(counts[3], counts[1]);
			if (counts[2] % 2 == 1)
				answer += 1 + (rem + 1) / 4;
			else
				answer += (rem + 3) / 4;
			break;
		}
		fout << "Case #" << t << ": " << answer << endl;
	}
}

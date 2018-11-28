#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <set>
#include <string>
#include <cmath>
#include <fstream>
using namespace std;

int compare(const void * x1, const void * x2)
{
	return (*(int*)x1 - *(int*)x2);
}

int main() {
	std::ios::sync_with_stdio(false);

	ifstream fin("A-large.in");
	ofstream fout("output");

	int T;
	fin >> T;
	for (int e = 0; e < T; ++e) {
		fout << "Case #" << e + 1 << ": ";
		string s;
		fin >> s;
		int n = s.length();
		int k;
		fin >> k;
		int ans = 0;
		for (int i = 0; i < n - k + 1; ++i) {
			if (s[i] == '-') {
				for (int j = 0; j < k; ++j) {
					if (s[i + j] == '-') {
						s[i + j] = '+';
					}
					else {
						s[i + j] = '-';
					}
				}
				ans++;
			}
		}
		bool f = true;
		for (int i = n - k + 1; i < n && f; ++i) {
			if (s[i] == '-') {
				fout << "IMPOSSIBLE" << endl;
				f = false;
			}
		}
		if (f) {
			fout << ans << endl;
		}
	}

	fin.close();
	fout.close();

	return 0;
}
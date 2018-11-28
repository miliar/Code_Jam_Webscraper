#include <bits/stdc++.h>

#define pb push_back
#define f first
#define s second
#define pii pair<int, int>
#define mp make_pair
 
using namespace std;
 
const string name = "A",
             in_file = name + ".in",
             out_file = name + ".out";
 
ifstream fin(in_file);
ofstream fout(out_file);
 
const int MAX = 1e3 + 1;

pii horses[MAX];

long double solve(int n, int dist) {
	long double longest_time = 0;
	for (int i = 0; i < n; i++) {
		long double remaining_dist = dist - horses[i].f;
		long double time_left = remaining_dist / (long double)horses[i].s;
		longest_time = max(longest_time, time_left);
	}

	return dist / longest_time;
}

int main() {
	int tests;
	fin >> tests;
	for (int test = 1; test <= tests; test++) {
		int dist, n;

		fin >> dist >> n;
		for (int i = 0; i < n; i++) {
			fin >> horses[i].f >> horses[i].s;
		}

		fout << "Case #" << test << ": " << fixed << setprecision(6) << solve(n, dist) << '\n';
	}
	return 0;
}
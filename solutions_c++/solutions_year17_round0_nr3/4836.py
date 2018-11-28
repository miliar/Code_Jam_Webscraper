#include <bits/stdc++.h>

#define pb push_back
#define f first
#define s second
#define pii pair<int, int>
#define mp make_pair
 
using namespace std;
 
const string name = "C",
             in_file = name + ".in",
             out_file = name + ".out";
 
ifstream fin(in_file);
ofstream fout(out_file);

void solve(long long n, long long k) {
	priority_queue<long long, vector<long long>, less<long long>> queue;
	queue.push(n);
	long long sol;
	for (int i = 1; i <= k; i++) {
		sol = queue.top();
		queue.pop();
		queue.push(sol / 2);
		if (sol % 2) {
			queue.push(sol / 2);
		} else {
			queue.push(sol / 2 - 1);
		}
	}
	fout << sol / 2 << ' ' << (sol % 2 ? sol / 2 : sol / 2 - 1) << '\n';
}

int main() {
	int t;
	fin >> t;
	for (int test = 1; test <= t; test++) {
		long long n, k;
		fin >> n >> k;
		fout << "Case #" << test << ": ";
		solve(n, k);
	}
	return 0;
}
#include <iostream>
#include <tuple>
#include <sstream>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <memory>
#include <array>

using namespace std;

pair<long, long> solve_brute(long n, long k)
{
	vector<bool> stalls(n, false);

	long max_gap = 0;
	for (long i = 0; i < k; ++i) {
		max_gap = 0;
		long max_i = 0;
		long curr_gap = 0;
		long curr_i = 0;
		for (long j = 0; j < n + 1; ++j) {
			if (j != n && !stalls[j]) {
				++curr_gap;
			} else {
				if (curr_gap > max_gap) {
					max_gap = curr_gap;
					max_i = curr_i;
				}
				curr_gap = 0;
				curr_i = j + 1;
			}
		}
		stalls[max_i + (max_gap - 1) / 2] = true;
	}

	return make_pair(max_gap / 2, (max_gap - 1) / 2);
}

pair<long, long> solve_brute2(long n, long k)
{
	priority_queue<long> q;
	q.push(n);
	long gap;
	for (long i = 0; i < k; ++i) {
		gap = q.top();
		q.pop();
		q.push(gap / 2);
		q.push((gap - 1) / 2);
	}

	return make_pair(gap / 2, (gap - 1) / 2);
}

long solve(long n, long k)
{
    return 0;
}

int main(int argc, char *argv[])
{
    if (argc > 1) freopen(argv[1], "r", stdin);
    if (argc > 2) freopen(argv[2], "w", stdout);

    int numCases;
    cin >> numCases;

    int casei = 0;
    long n, k;
    while (++casei, cin >> n >> k) {
		cout << "Case #" << casei << ": ";

		pair<long, long> sol = solve_brute2(n, k);
		cout << sol.first << " " << sol.second;

		cout << endl;
    }

    return 0;
}
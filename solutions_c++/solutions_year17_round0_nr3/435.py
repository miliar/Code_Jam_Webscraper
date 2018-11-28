#include <bits/stdc++.h>
using namespace std;

int T;
long long N, K, L, C, placed, bmin, bmax;

int main() 
{
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> N >> K;
		map <long long, long long> intervals;
		intervals[N] = 1;
		placed = 0;
		while (placed < K) {
			auto I = *intervals.rbegin();
			L = I.first;
			C = I.second;
			bmax = L/2;
			bmin = (L-1)/2;
			placed += C;
			intervals[L/2] += C;
			intervals[(L-1)/2] += C;
			intervals.erase(L);
		}
		cout << "Case #" << t << ": " << bmax << " " << bmin << endl;
	}
}

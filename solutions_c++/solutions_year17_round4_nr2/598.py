#include <bits/stdc++.h>
using namespace std;
#define TAM		101

int solve1 ( vector<int> a, vector<int> b ) {
	if ( a.size() < b.size() ) a.swap(b);
	sort ( a.rbegin(), a.rend() );
	sort ( b.begin(), b.end() );
	int ans = a.size();
	for ( int i = 0; i < b.size(); ++i )
		if ( a[i] == b[i] && a[i] == 1 )
			ans++;
	return ans;
}

int solve2 ( vector<int> a, vector<int> b, int N, int ans1 ) {
	for ( int i = 0; i < a.size(); ++i ) {
		int cntA = 0, cntB = 0;
		for ( int j = 0; j < a.size(); ++j )
			cntA += ( a[i] == a[j] );
		for ( int j = 0; j < b.size(); ++j )
			cntB += ( a[i] == b[j] );
		if ( cntA + cntB > ans1 )
			return cntA + cntB - ans1;
	}
	return 0;
}

int main ( )
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );

	int ntc;
	scanf ( "%d", &ntc );
	for ( int t = 1; t <= ntc; ++t ) {
		int N, C, M;
		scanf ( "%d%d%d", &N, &C, &M );

		vector<int> a, b;
		while ( M-- ) {
			int buyer, pos;
			scanf ( "%d%d", &pos, &buyer );
			if ( buyer == 1 ) a.push_back(pos);
			else b.push_back(pos);
		}

		int ans1 = solve1(a, b);
		int ans2 = solve2(a, b, N, ans1);

		printf ( "Case #%d: %d %d\n", t, ans1, ans2 );
	}

	return 0;
}

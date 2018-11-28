#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>
#include<bitset>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define f first
#define s second

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

VI segments;

void go(int n) {
	if(n == 0) {
		return;
	}
	segments.PB(n);
	if(n == 1) {
		return;
	}
	go((n - 1) / 2);
	go(n - (n - 1) / 2 - 1);
}

void solve() {
	int n, k;
	cin >> n >> k;

	segments.clear();
	go(n);
	sort(ALL(segments));
	reverse(ALL(segments));
//	REP(i, segments.size()) cout << segments[i] << endl;
	cout << (segments[k - 1] - (segments[k - 1] - 1) / 2 - 1) << " " << (segments[k - 1] - 1) / 2;
}

int main() {
	int t;
	cin >> t;

	REP(i, t) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
		cout << '\n';
	}
	return 0;
}

#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>
#include<bitset>
#include<vector>
#include<map>
#include<set>
#include<iomanip>
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

void testcase() {
	int n,k;
	cin >> n >> k;

	vector < pair<int,int> > pancakes;

	REP(i, n) {
		int r, h;
		cin >> r >> h;
		pancakes.PB(MP(r, h));
	}

	sort(ALL(pancakes));
	reverse(ALL(pancakes));
	
	long long result = 0;
	FOR(i, 0, n - k) {
		long long current = (long long)pancakes[i].first * pancakes[i].first;
		current += (long long)pancakes[i].first * pancakes[i].second * 2;

		vector< long long> areas;
		FOR(j, i + 1, n - 1) {
			areas.PB((long long)pancakes[j].first * pancakes[j].second);
		}
		sort(ALL(areas));
		reverse(ALL(areas));
		REP(j, k - 1) {
			current += 2 * areas[j];
		}
		result = max(result, current);
	}

	long double output = M_PI * result;
	cout << setprecision(15) << output << '\n';
}

int main() {
	int t;
	cin >> t;
	
	FOR(i, 1, t) {
		cout << "Case #" << i << ": ";
		testcase();
	}

	return 0;
}


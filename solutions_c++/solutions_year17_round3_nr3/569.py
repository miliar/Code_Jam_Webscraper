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
#include<iomanip>
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
	int n, k;
	cin >> n >> k;

	long double u;
	cin >> u;
	
	vector<long double> probs;
	REP(i, n) {
		double p;
		cin >> p;
		probs.PB(p);
	}

	long double l = 0.0;
	long double r = 1.0;

	REP(i, 100) {
		long double x = (l + r) / 2;
		long double s = 0.0;
		REP(j, n) {
			s += max((long double)0.0, x - probs[j]);
		}
		if(s > u) {
			r = x;
		} else {
			l = x;
		}
	}
	
	long double result = 1.0;
	REP(i, n) result *= max(l, probs[i]);
	cout << setprecision(15) << result << '\n';
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


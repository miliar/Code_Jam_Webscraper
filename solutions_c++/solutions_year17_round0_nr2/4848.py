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

long long findValue(VI digits) {
	long long value = 0;

	REP(i, digits.size()) {
		value *= 10;
		value += digits[i];
	}

	return value;
}

long long isTidy(VI digits) {
	REP(i, digits.size() - 1) {
		if(digits[i + 1] < digits[i]) {
			return false;
		}
	}
	return true;
}

void solve() {
	long long n;
	cin >> n;

	long long _n = n;
	VI digits;
	while(n) {
		digits.PB(n % 10);
		n /= 10;
	}
	reverse(ALL(digits));

	if(isTidy(digits)) {
		cout << _n;
		return;
	}

	long long result = 0;
	FOR(i, 0, digits.size() - 1) {
		if(digits[i] == 0) {
			continue;
		}
		VI d;
		REP(j, i) {
			d.PB(digits[j]);
		}
		d.PB(digits[i] - 1);
		REP(j, digits.size() - i - 1) {
			d.PB(9);
		}
		if(!isTidy(d)) {
			continue;
		}
		long long value = findValue(d);
		if(value <= _n) {
			result = max(result, value);
		}
	}

	cout << result;
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

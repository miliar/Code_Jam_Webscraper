#include <iostream>
using namespace std;
typedef unsigned long long ll;
#define f0(i,N) for (int i=0; i< N; i++) 
#define f1(i,N) for (int i=1; i<=N; i++) 

ll isTidy(ll N)
{
	ll ls = N % 10; N /= 10;
	while (N > 0) {
		ll cur = N % 10;
		if (cur > ls) return 0;
		ls = cur;
		N /= 10;
	}
	return 1;
}

ll power(ll d)
{
	ll ans = 1;
	f0(i, d) { ans = 10 * ans; }
	return ans;
}

ll nines(int d) {
	ll ans = 0;
	f0(i, d) { ans = 10 * ans + 9; }
	return ans;
}

ll tidy(ll N) {
	if (isTidy(N)) return N;
	ll ls = 10; int d = -1;
	while (N > 0) {
		d++;
		ll cur = N % 10;
		if (cur > ls) break;
		ls = cur;
		N /= 10;
	}
	return (tidy(N - 1)*power(d) + nines(d));
}


int main()
{
	ios::sync_with_stdio(false);
	int T; cin >> T; f1(t, T) {
		ll N; cin >> N; 
		cout << "Case #" << t << ": " << tidy(N) << endl;
	}
	return 0;
}

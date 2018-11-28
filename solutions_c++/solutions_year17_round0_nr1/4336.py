#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define itr iterator
#define ritr reverse_iterator
#define pint pair<int, int>
#define pll pair<ll, ll>
#define S second
#define F first
#define v(a) vector<a>
#define mk(a, b) make_pair(a, b)
#define psh(a) push_back(a)
#define mem(arr, a) memset(arr, a, sizeof(arr))
#define pr(n) printf("%d\n", n)
#define sc(n) scanf ("%d", &n)
#define scll(n) scanf ("%lld", &n)
#define prll(n) printf("%lld\n", n)
#define MOD 1000000007ll
#define inf 1000000000ll

string s;
int l;

int cal (int n, int x) {
	if (n+1 < x) {
		return 0;
	}
	if (s[n] == '+') {
		return cal(n-1, x);
	}else {
		int i;
		int temp = x;
		for (i = n; i >= 0 ,temp > 0; i--, temp--) {
			if (s[i] == '-') {
				s[i] = '+';
			}else{
				s[i] = '-';
			}
		}
		return cal(n-1, x) + 1;
	}

}

int main (void) {
	freopen("A-large.in","r",stdin);
	freopen("output_file_name1.out","w",stdout);
	int test;
	sc (test);
	for (int k = 1; k <= test; k++) {
		s.clear();
		cin>>s;
		int x;
		sc (x);
		l = s.size();
		int ans = cal(l-1, x);
		int i;
		for (i = 0; i < l; i++) {
			if (s[i] == '-'){
				break;
			}
		}
		if (i != l){
			printf("Case #%d: IMPOSSIBLE\n", k);
		}else {
			printf ("Case #%d: %d\n", k, ans);
		}
	}

	return 0;
}

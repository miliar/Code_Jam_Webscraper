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

priority_queue<int> p;

int main (void) {
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("output_file_name1.out","w",stdout);
	int test;
	sc (test);
	for (int a = 1; a <= test; a++) {
		int n;
		p = priority_queue<int> ();
		sc (n);
		int k;
		sc (k);
		printf("Case #%d: ", a);
		k--;
		int t;
		p.push(n);
		while (k) {
			t = p.top();
			if (t % 2 == 0) {
				p.pop();
				t = t/2;
				p.push(t);
				if(t>1)
					p.push(t-1);
			}else if(t != 1){
				p.pop();
				t = t/2;
				p.push(t);
				p.push(t);
			}else if (t == 1) {
				p.pop();
			}
			k--;
		}
		t = p.top();
		t++;
		int l , r;
		l = t/2 - 1;
		r = (t-1) - t/2;
		cout<<r<<" "<<l<<endl;
	}

	return 0;
}

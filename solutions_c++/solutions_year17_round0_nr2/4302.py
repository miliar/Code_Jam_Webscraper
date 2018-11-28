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

int main (void) {
	freopen("B-large.in","r",stdin);
	freopen("output_file_name1.out","w",stdout);
	int test;
	sc (test);
	for (int k = 1; k <= test; k++) {
		cin>>s;
		int l = s.size();
		printf("Case #%d: ", k);
		if(l == 1){
			cout<<s<<endl;
			continue;
		}
		bool f = true;
		int i, j;
		while (f) {
			i = l-2;
			while (i >= 0 && s[i] <= s[i+1]) {
				i--;
				//cout<<i<<endl;
			}
			if(i<0){
				f = false;
				break;
			}
			s[i] = s[i]-1;
			i++;
			for(; i < l; i++) {
				s[i] = '9';
			}
		}
		i = 0;
		while (s[i] == '0') {
			i++;
		}
		while (i < l){
			cout<<s[i];
			i++;
		}
		cout<<endl;
	}
	return 0;
}

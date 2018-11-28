#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int, int> pi;
const int mod = 1e9 + 7;
const double EPS = 1e-9;
const int INF = 1 << 29;
#define mp make_pair
#define el putchar('\n')
#define sp putchar(' ')
#define Fill(a,val) memset(a,val,sizeof a)
#define all(a) a.begin(),a.end()
#ifndef ONLINE_JUDGE
#define tr(a, it) for (decltype(a.begin()) it = a.begin(); it != a.end(); ++it)
#else
#define tr(a, it) for (typeof(a.begin()) it = a.begin(); it != a.end(); ++it)
#endif
#define in(n) scanf("%d",&n)
#define inl(n) scanf("%lld",&n)
#define out(n) printf("%d",n);
#define outl(n) printf("%lld",n);

char a[26][26];

void f1(int r, int c){
	for (int j = 1; j <= c; ++j){
		for (int i = 1; i <= r; ++i){
			if (a[i][j] != '?'){
				int k = i - 1;
				while (k >= 1 && a[k][j]=='?'){
					a[k][j] = a[i][j]; --k;
				}
			}
		}
		if (a[r][j] == '?'){
			int k = r - 1;
			while (k >= 1 && a[k][j] == '?')--k;
			if (k >= 1){
				char c = a[k][j];
				++k;
				while (k <= r)a[k][j] = c, ++k;
			}
		}
	}
}

void f2(int r, int c){
	for (int j = 1; j <= c; ++j){
		if (a[1][j] != '?')continue;
		bool ok = false;
		int k = j - 1;
		while (k >= 1 && a[1][k] == '?')--k;
		if (k >= 1){
			for (int i = 1; i <= r; ++i)a[i][j] = a[i][k];
			ok = true;
		}
		if (ok)continue;
		k = j + 1;
		while (k <= c && a[1][k] == '?')++k;
		if (k <= c){
			for (int i = 1; i <= r; ++i)a[i][j] = a[i][k];
			ok = true;
		}
	}
}

int main(){
	freopen("ip.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int t; in(t);
	for (int cs = 1; cs <= t; ++cs){
		int r, c; cin >> r >> c;
		for (int i = 1; i <= r; ++i){
			for (int j = 1; j <= c; ++j)
				cin >> a[i][j];
		}
		f1(r, c);
		f2(r, c);
		printf("Case #%d:\n", cs);
		for (int i = 1; i <= r; ++i){
			for (int j = 1; j <= c; ++j){
				cout << a[i][j];
			}el;
		}
	}
	return 0;
}
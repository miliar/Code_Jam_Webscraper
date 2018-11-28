#include <bits/stdc++.h>
 
#define gc getchar
#define ii(x) scanf(" %d", &x)
#define ill(x) scanf(" %lld", &x)
#define ll long long
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(),x.end()
#define fill(a,b) memset(a, b, sizeof(a))
#define rep(i,a,b) for(i=a;i<b;i++)
#define per(i,a,b) for(i=a;i>=b;i--)
#define pii pair<int, int>
 
using namespace std;
 
void in(int &x){
    register int c=gc();
    x=0;
    for(;(c<48||c>57);c=gc());
    for(;c>47&&c<58;c=gc()){x=(x<<1)+(x<<3)+c-48;}
}

int main()
{
	int t, n, k, i, j, tt;
	in(t); rep(tt, 1, t + 1){
		string s; int cnt = 0;
		cin >> s >> k;
		n = s.length();
		rep(i, 0, n - k + 1) if(s[i] == '-'){
			rep(j, i, i + k) s[j] = s[j] == '-' ? '+' : '-';
			cnt++;
		}
		bool ok = true;
		while(i < n){
			if(s[i] == '-') ok = false;
			i++;
		}
		printf("Case #%d: ", tt);
		if(ok) printf("%d\n", cnt);
		else printf("IMPOSSIBLE\n");
	}

	return 0;
}
#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define sz(a) ((int)(a).size())
#define rep(i, a, b) for(int (i) = (a); (i) < (b); (i)++)
#define dec(i, a, b) for (int (i) = (a); (i) >= (b); (i)--)
#define clr(a,v) memset(a, v, sizeof(a))
#define all(a) (a).begin(),(a).end()
#define MAXN 101010
#define LOGN 20
#define EPS 1e-10
#define fcin ios_base::sync_with_stdio(false)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

int t, n, k, bit[MAXN];
char s[MAXN];

void upd(int p){ for(p++; p <= n; p+=p&-p) bit[p]++; }
void upd(int l, int r){ upd(l); upd(r+1); }
int get(int p){ int ret = 0; for(p++; p>0; p-=p&-p) ret += bit[p]; return (ret&1); }

int main(){
	scanf("%d", &t);
	rep(caso,1,t+1){
		int ans = 0, ult = -1;
		scanf("%s%d", s, &k);
		n = strlen(s);
		rep(i,0,n+10) bit[i] = 0;
		rep(i,0,n) if((!get(i) && s[i] == '-')||(get(i) && s[i] == '+')){
			if(i+k-1 >= n){ ans = -1; break; }
			ans++;
			upd(i,i+k-1);
		}
		printf("Case #%d: ", caso);
		if(ans != -1) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
}


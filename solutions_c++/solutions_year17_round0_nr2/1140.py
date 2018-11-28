#include <cstdio>
#include <cstring>
#include <map>
#include <queue>

using namespace std;
#define rep(i,a,b) for (int i=(a);i<=(b);i++)
#define repd(i,a,b) for (int i=(a);i>=(b);i--)
#define for_iter(i,n) for (__typeof(n.begin())i=n.begin();i!=n.end();++i)
typedef long long ll;
const int maxn=22;
ll n,k,ans;
int m,a[maxn],b[maxn];

bool dfs(ll k,int e) {
	if (k==0) return true;
	if (e==1) {
		repd(i,a[k],b[k+1]) {
			b[k]=i;
			if (dfs(k-1,i==a[k]))
				return true;
		}
	} else {
		repd(i,9,b[k+1]) {
			b[k]=i;
			if (dfs(k-1,0))
				return true;
		}
	}
	return false;
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;scanf("%d\n",&T);
	rep(t,1,T) {
		printf("Case #%d: ",t);
		scanf("%lld\n",&n);
		ll tn=n;
		m=0;
		while (tn) a[++m]=tn%10,tn/=10;
		// TODO test n=1
		memset(b,0,sizeof b);
		repd(i,a[m],0) {
			b[m]=i;
			if (dfs(m-1,i==a[m])) {
				int j=m;
				while (b[j]==0) j--;
				repd(k,j,1)
					printf("%d",b[k]);
				puts("");
				break;
			}
		}
	}
	return 0;
}

#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define sz(a) ((int)(a).size())
#define rep(i, a, b) for(int (i) = (a); (i) < (b); (i)++)
#define dec(i, a, b) for (int (i) = (a); (i) >= (b); (i)--)
#define clr(a,v) memset(a, v, sizeof(a))
#define all(a) (a).begin(),(a).end()
#define ler freopen("in", "r", stdin)
#define fcin ios_base::sync_with_stdio(false)
#define EPS 1e-7
#define MAXN 303030
#define LOGN 18
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;

int t, n, p, vet[111], cnt[5];

int main(){
	scanf("%d", &t);
	rep(caso,1,t+1){
		int ans = 0;
		clr(cnt,0);
		scanf("%d%d", &n, &p);
		rep(i,0,n) scanf("%d",vet+i), cnt[vet[i]%p]++;
		if(p==2)
			ans = cnt[0]+(cnt[1]+1)/2;
		else if(p==3)
			ans = cnt[0] + min(cnt[1],cnt[2]) + (max(cnt[1],cnt[2])-min(cnt[1],cnt[2])+2)/3;
		else{
			rep(i,0,cnt[2]+1){
				if(cnt[1]/2 + cnt[3]/2 < i) break;
				int cur = cnt[0], aux=i, c1 = cnt[1], c2 = cnt[2]-i, c3 = cnt[3];
				while(aux){
					if(c1 > c3) c1-=2;
					else c3 -= 2;
					aux--;
					cur++;
				}
				cur += c2/2;
				cur += min(c1,c3) + (max(c1,c3)-min(c1,c3))/4;
				if(c2%2 || (max(c1,c3)-min(c1,c3))%4) cur++;
				ans = max(ans,cur);
			}
		}
		printf("Case #%d: %d\n", caso, ans);
	}
}


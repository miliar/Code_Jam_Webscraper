#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define ii pair<int,int>
#define INF 1000000100
#define INFLL 3000000000000000010ll
#define UQ(x) (x).resize(distance((x).begin(),unique(all((x)))))
#define mid(x,y) (((x)+(y))>>1)
int n,c,m;
bool taken[1005];
vector<ii> t[1005];//index = pos
int cnt[1005];
int main() {
	int tc;
	scanf("%d",&tc);
	for (int kk=1;kk<=tc;kk++) {
		scanf("%d%d%d",&n,&c,&m);
		int b,p;
		memset(cnt,0,sizeof(cnt));
		for (int i=0;i<n;i++) t[i].clear();
		memset(taken,0,sizeof(taken));
		for (int i=0;i<m;i++) {
			scanf("%d%d",&p,&b);
			--p,--b;
			t[p].pb(mp(b,i));
			cnt[b]++;
		}
		int take=0;
		int rides=-1;
		for (int k=1;k<=m;k++) {
			int cur=0;
			for (int i=0;i<n;i++) {
				for (ii x:t[i]) {
					if (taken[x.second]) continue;
					if (i<cur) continue;
					taken[x.second]=1;
					take++;
					cur++;
				}
			}
			if (take==m) {
				rides=k;
				break;
			}
		}
		assert(rides!=-1);
		rides=max(rides,*max_element(cnt,cnt+c));
		int ans=0,ext=0;
		for (int i=n-1;i>=0;i--) {
			int ct=sz(t[i]);
			if (ct>rides) {
				ext+=ct-rides;
				ans+=ct-rides;
			} else {
				ext-=(rides-ct);
				ext=max(ext,0);
			}
		}
		assert(ext==0);
		printf("Case #%d: %d %d\n", kk,rides,ans);
	}
}
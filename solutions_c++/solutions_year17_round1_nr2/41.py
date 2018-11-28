#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <utility>
#include <cstring>
#define mp make_pair

using namespace std;

vector<pair<int,int> > f;
int tt;
int n,p;
int used[60],cur[60];
int r[60];

bool cmp(const pair<int,int> &a,const pair<int,int> &b) {
	if (a.first!=b.first) return a.first<b.first;
	else return a.second>b.second;
}

bool check(int p,int q) {
	return 11*p>=q*10 && 9*p<=q*10;
}

void solve(int q,int per,int &l,int &r) {
	l=(int)((double)q/1.1/per);
	r=(int)((double)q/0.9/per)+1;
	while (!check(l*per,q) && l<=r) l++;
	while (!check(r*per,q) && l<=r) r--;
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d%d",&n,&p);
		for (int i=1;i<=n;++i)
			scanf("%d",&r[i]);
		f.clear();
		memset(used,0,sizeof(used));
		memset(cur,0,sizeof(cur));
		for (int i=1;i<=n;++i)
			for (int j=0;j<p;++j) {
				int x;
				scanf("%d",&x);
				int ll,rr;
				solve(x,r[i],ll,rr);
				if (ll>rr) continue;
				f.push_back(mp(ll,i));
				f.push_back(mp(rr,-i));
				//printf("%d %d: %d %d\n",i,j,ll,rr);
			}

		sort(f.begin(),f.end(),cmp);

		int ans=0;
		for (int i=0;i<(int)f.size();++i) {
			if (f[i].second>0) {
				int k=f[i].second;
				cur[k]++;
				bool flag=true;
				for (int j=1;j<=n;++j)
					if (cur[j]==0) {
						flag=false;
						break;
					}
				if (flag) {
					ans++;
					for (int j=1;j<=n;++j)
						cur[j]--,used[j]++;
				}
			} else {
				int k=-f[i].second;
				if (used[k]>0) used[k]--;
				else cur[k]--;
			}
		}

		printf("Case #%d: %d\n",ii,ans);
	}

}
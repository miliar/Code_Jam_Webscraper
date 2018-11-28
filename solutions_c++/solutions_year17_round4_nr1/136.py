#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;
typedef long long ll;

map<pair<vector<int>,int>,int> dp;
int n,p;

int f(vector<int> v, int k){
	if(dp.count(mp(v,k)))return dp[mp(v,k)];
	bool z=true;
	fore(i,0,v.size())z=z&&!v[i];
	if(z)return dp[mp(v,k)]=0;
	int r=0;
	fore(i,0,v.size()){
		if(v[i]>0){
			vector<int> w=v;
			w[i]--;
			int kk=(k+i+1)%p;
			int s=f(w,kk);
			if(!k)s++;
			r=max(r,s);
		}
	}
	return dp[mp(v,k)]=r;
}

int x[8];

int main(){
	int tn;
	scanf("%d",&tn);
	fore(tc,1,tn+1){
		printf("Case #%d: ",tc);
		scanf("%d%d",&n,&p);
		memset(x,0,sizeof(x));
		fore(i,0,n){
			int k;
			scanf("%d",&k);
			x[k%p]++;
		}
		vector<int> v;
		fore(i,1,p)v.pb(x[i]);
		dp.clear();
		printf("%d\n",x[0]+f(v,0));
	}
	return 0;
}

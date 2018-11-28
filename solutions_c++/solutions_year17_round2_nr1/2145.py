#include<bits/stdc++.h>
#define x first
#define y second
using namespace std;
#define MAXN 1005
int t,d,n;
int k[MAXN],s[MAXN]; 
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(int _=0;_<t;++_){
		scanf("%d%d",&d,&n);
		double ma=0;
		for(int i=0;i<n;++i){
			scanf("%d%d",&k[i],&s[i]);
			int tmd=d-k[i];
			ma=max(ma,(double)tmd/(double)s[i]);
		}
		printf("Case #%d: %.6f\n",_+1,d/ma);
	}
	return 0;
}


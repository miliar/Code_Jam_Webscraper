#include<bits/stdc++.h>
#define N 60
using namespace std;
int main(){
	int q[N],l[N][N],r[N][N];
	int T,n,p;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		scanf("%d%d",&n,&p);
		for(int i=0;i<n;i++){
			scanf("%d",&q[i]);
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<p;j++){
				scanf("%d",&l[i][j]);
			}
			sort(l[i],l[i]+p);
			for(int j=0;j<p;j++){
				r[i][j]=l[i][j]*10/9/q[i];
				l[i][j]=((l[i][j]*10+10)/11+q[i]-1)/q[i];
			}
		}
		int ans=0,mx;
		int pt[N]={};
		bool gg=false,fl=false;
		while(!gg){
			mx=0;
			for(int i=0;i<n;i++){
				mx=max(l[i][pt[i]],mx);
			}
			fl=false;
			for(int i=0;i<n;i++){ 
				while(pt[i]<p&&r[i][pt[i]]<mx) fl=true,pt[i]++;
			}
			if(!fl){
				ans++;
				for(int i=0;i<n;i++) pt[i]++;
			}
			for(int i=0;i<n;i++){
				if(pt[i]==p) gg=true;
			}
		}
		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}
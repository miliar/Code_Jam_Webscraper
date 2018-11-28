#include <bits/stdc++.h>
using namespace std;
int recipe[60];
int q[60][60];
int idx[60];
int Max[60][60];
int Min[60][60];

void valid(int x,int y){
	int n1 = q[x][y]*100/recipe[x]/110;
	int n2 = q[x][y]*100/recipe[x]/90;
	n1 -=2;
	n2 +=2;
	while(n1*recipe[x]*110<q[x][y]*100) n1++;
	while(n2*recipe[x]*90>q[x][y]*100) n2--;
	if(n1>n2) {
		Min[x][y] = Max[x][y] =-1;
		return;
	}

	Max[x][y]=n2;
	Min[x][y]=n1;

}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("Blarge.out","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		int n,p;
		cin>>n>>p;
		for(int i=1;i<=n;i++){
			cin>>recipe[i];
		}
		for(int i=1;i<=n;i++){
			for(int j=1;j<=p;j++){
				cin>>q[i][j];
				
			}
		}
		for(int i=1;i<=n;i++)
			sort(q[i]+1,q[i]+p+1);
		for(int i=1;i<=n;i++){
			for(int j=1;j<=p;j++){
				valid(i,j);
			}
		}
		for(int i=1;i<=n;i++) idx[i]=1;
		int ans =0,end =0;
		while(1){
			int m1 = 0,m2 = 1000000000;
			for(int i=1;i<=n;i++){
				while(Min[i][idx[i]]==-1 && idx[i]<=p) idx[i]++;
				if(idx[i]>p){
					end=1;
					break;
				}
				if(Min[i][idx[i]]>m1) {
					m1=Min[i][idx[i]];
					m2=Max[i][idx[i]];
				}
				else if(Min[i][idx[i]]==m1 && Max[i][idx[i]]<m2){
					m2=Max[i][idx[i]];
				}
			}
			if(end) break;
			int valid =1;
			for(int i=1;i<=n;i++){
				while(Max[i][idx[i]]<m1 || Min[i][idx[i]]==-1){
					idx[i]++;
					if(idx[i]>p){
						end=1;
						break;
					}
				}
				if(end) break;
				if(Min[i][idx[i]]>m2) valid =0;
			}
			if(end) break;
			if(valid){
				ans++;
				for(int i=1;i<=n;i++) idx[i]++;
			}
			if(end) break;
		}
		
		printf("Case #%d: %d\n",t,ans);
		
	}
}

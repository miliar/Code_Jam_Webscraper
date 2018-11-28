//#include<stdio.h>
//#include<stdlib.h>
#include<bits/stdc++.h>
//#define Min(a,b,c) min((a),min((b),(c)))
#define mp(a,b) make_pair((a),(b))
#define pii pair<int,int>
#define pll pair<LL,LL>
#define pb(x) push_back(x)
#define x first
#define y second
#define sqr(x) ((x)*(x))
#define EPS 1e-11
#define MEM(x) memset(x,0,sizeof(x))
//#define N 200005
#define M
#define pi 3.14159265359
using namespace std;
typedef long long LL;
int main(){
	int r,c;
	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;T++){ 
		scanf("%d %d",&r,&c);
		char ans[30][30];
		for(int i=1;i<=r;i++)
		scanf("%s",ans[i]+1); 
		for(int i=0;i<=r;i++)
		ans[i][0]='?';
		for(int i=0;i<=c;i++)
		ans[0][i]='?';
		for(int i=1;i<=r;i++){
			int find=-1;
			for(int j=1;j<=c;j++)
			if(ans[i][j]!='?'){
				find=j;
				break;
			}
			if(find==-1){
				for(int j=1;j<=c;j++)
				ans[i][j]=ans[i-1][j];
			}
			else{
				if(ans[i][1]=='?')
				ans[i][1]=ans[i][find];
				for(int j=2;j<=c;j++){
					if(ans[i][j]=='?')
					ans[i][j]=ans[i][j-1];
				} 
			}
		}
		for(int i=r;i>=1;i--){
			if(ans[i][1]=='?')
			for(int j=1;j<=c;j++)
			ans[i][j]=ans[i+1][j];
		}
		printf("Case #%d:\n",T);
		for(int i=1;i<=r;i++){ 
			for(int j=1;j<=c;j++)
			printf("%c",ans[i][j]);
			printf("\n");
		} 
	}
}


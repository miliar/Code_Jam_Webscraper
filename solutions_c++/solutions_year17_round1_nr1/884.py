#include<bits/stdc++.h>
#define rep(ii,x,y) for(int ii=(x);ii<(y);ii++)
#define FI first
#define SE second
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

int n,m,cas,t;
char str[30][30];


int check(int x1,int y1,int x2,int y2){
	int cnt=0;
	// bool chara[27];
	// memset(chara,0,sizeof(chara));
	rep(i,x1,x2+1){
		rep(j,y1,y2+1){
			if(str[i][j]!='?')cnt++;
		}
	}
	return cnt;
}

void dfs(int x1,int y1,int x2,int y2){
	if(check(x1,y1,x2,y2)==1){
		char c=0;
		rep(i,x1,x2+1){
			rep(j,y1,y2+1)if(str[i][j]!='?'){ c=str[i][j];break; }
			if(c!=0)break;
		}
		rep(i,x1,x2+1)rep(j,y1,y2+1)str[i][j]=c;
		return;
	}
	bool secc=false;
	if(x1<x2){
		rep(i,x1,x2){
			if(check(x1,y1,i,y2)>0 && check(i+1,y1,x2,y2)>0){
				dfs(x1,y1,i,y2);
				dfs(i+1,y1,x2,y2);
				secc=true;
				break;
			}
		}
	}
	if(!secc && y1<y2){
		rep(j,y1,y2){
			if(check(x1,y1,x2,j)>0 && check(x1,j+1,x2,y2)>0){
				dfs(x1,y1,x2,j);
				dfs(x1,j+1,x2,y2);
				break;
			}
		}		
	}
}


int main(){
#ifdef AKAISORA
	// freopen("in.txt","r",stdin);
	// freopen("out.txt","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif
	scanf("%d",&cas);
	for(int t=1;t<=cas;t++){
		printf("Case #%d:\n",t);
		scanf("%d%d",&n,&m);
		rep(i,0,n)scanf("%s",str[i]);
		dfs(0,0,n-1,m-1);
		rep(i,0,n){
			printf("%s\n",str[i]);
		}
	}
	return 0;
}
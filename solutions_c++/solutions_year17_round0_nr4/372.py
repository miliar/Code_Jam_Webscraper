#include<bits/stdc++.h>
#define N 210
using namespace std;
int mp[N][2],mx[N][2];
bool vis[N];
bool cp[N][N],cx[N][N],gr[N],gc[N],gp[N],gm[N];
int ori[N][N],pos[N][N];
bool ext(int s, int m[][2], bool c[][N], int n){
	vis[s]=true;
	for(int i=1;i<=n;i++){
		if(c[s][i]){
			if(!m[i][1]||!vis[m[i][1]]&&ext(m[i][1],m,c,n)){
				m[i][1]=s;
				m[s][0]=i;
				return true;
			}
		}
	}
	return false;
}
void matching(int m[][2],bool c[][N],int n){
	bool flag=true;
	while(flag){
		flag=false;
		for(int i=1;i<=n;i++){
			memset(vis,0,sizeof(vis));
			if(!m[i][0]&&ext(i,m,c,n)){
				flag=true;
			}
		}
	}
}
int main(){
	int T;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		int n,m,r,c,ch=0,sc=0;
		char tp;
		scanf("%d%d",&n,&m);
		memset(ori,0,sizeof(ori));
		memset(pos,0,sizeof(pos));
		memset(mx,0,sizeof(mx));
		memset(mp,0,sizeof(mp));
		memset(cx,0,sizeof(cx));
		memset(cp,0,sizeof(cp));
		memset(gr,0,sizeof(gr));
		memset(gc,0,sizeof(gc));
		memset(gm,0,sizeof(gm));
		memset(gp,0,sizeof(gp));
		while(m--){
			scanf(" %c%d%d",&tp,&r,&c);
			if(tp=='x'){
				ori[r][c]|=2;
				gr[r]=1,gc[c]=1;
				sc++;
			}
			else if(tp=='+'){
				ori[r][c]|=1;
				gp[r+c-1]=1,gm[r-c+n]=1;
				sc++;
			}
			else{
				ori[r][c]|=3,sc+=2;
				gr[r]=1,gc[c]=1;
				gp[r+c-1]=1,gm[r-c+n]=1;
			}
		}
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				if(!gr[i]&&!gc[j]) cp[i][j]=true;
				if(!gp[i+j-1]&&!gm[i-j+n]) cx[i+j-1][i-j+n]=true;
			}
		}
		matching(mp,cp,n);
		matching(mx,cx,n+n-1);
		for(int i=1;i<=n;i++){
			if(mp[i][0]){
				r=i,c=mp[i][0];
				if(!pos[r][c]) pos[r][c]=ori[r][c],ch++;
				pos[r][c]|=2;
				sc++;
			}
		}
		for(int i=1;i<=n+n-1;i++){
			if(mx[i][0]){
				r=(i+mx[i][0]+1-n)/2,c=(i-mx[i][0]+1+n)/2;
				if(!pos[r][c]) pos[r][c]=ori[r][c],ch++;
				pos[r][c]|=1;
				sc++;
			}
		}
		printf("Case #%d: %d %d\n",cs,sc,ch);
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				if(pos[i][j]==1){
					printf("+ %d %d\n",i,j);
				}
				else if(pos[i][j]==2){
					printf("x %d %d\n",i,j);
				}
				else if(pos[i][j]==3){
					printf("o %d %d\n",i,j);
				}
			}
		}
	}
	return 0;
}
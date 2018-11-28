#include<stdio.h>
#include<string.h>
#include<utility>
using namespace std;
int n;
char a[111][111];
char a2[111][111];
bool cross[111][111];
bool plus[111][111];

bool e[222][222];
bool bad_row[222],bad_col[222];
int lk[222];

int N;

bool B[222];
bool fd(int x){
	for(int i=1; i<=N; i++)
		if(e[x][i] && !B[i]){
			B[i] = true;
			if(lk[i] == -1 || fd(lk[i])){
				lk[i] = x;
				return true;
			}
		}
	return false;
}

pair<int,int> v[11111];int lv;

int main(){
	int _,t,m;char s[9];
	scanf("%d",&_);
	for(t=1; t<=_; t++){
		scanf("%d%d",&n,&m);
		memset(a,0,sizeof(a));
		while(m--){
			int x,y;
			scanf("%s%d%d",s,&x,&y);
			a[x][y] = *s;
		}
		//cross
		memset(cross,0,sizeof(cross));
		memset(bad_row,0,sizeof(bad_row));
		memset(bad_col,0,sizeof(bad_col));
		for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++)
		if(a[i][j] == 'x' || a[i][j] == 'o'){
			cross[i][j] = true;
			bad_row[i] = true;
			bad_col[j] = true;
		}
		memset(e,0,sizeof(e));
		for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++)
			if(!bad_row[i] && !bad_col[j])
				e[i][j] = true;
		memset(lk,-1,sizeof(lk));
		N = n;
		for(int i=1; i<=N; i++){
			memset(B,0,sizeof(B));
			fd(i);
		}
		for(int i=1; i<=N; i++)
			if(lk[i] != -1)
				cross[lk[i]][i] = true;

		//plus
		memset(plus,0,sizeof(plus));
		memset(bad_row,0,sizeof(bad_row));
		memset(bad_col,0,sizeof(bad_col));
		for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++)
		if(a[i][j] == '+' || a[i][j] == 'o'){
			plus[i][j] = true;
			bad_row[i+j-1] = true;
			bad_col[i-j+n] = true;
		}
		memset(e,0,sizeof(e));
		for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++)
			if(!bad_row[i+j-1] && !bad_col[i-j+n])
				e[i+j-1][i-j+n]=true;
		N = 2 * n -1;
		memset(lk,-1,sizeof(lk));
		for(int i=1; i<=N; i++){
			memset(B,0,sizeof(B));
			fd(i);
		}
		for(int i=1; i<=N; i++)
			if(lk[i] != -1){
				int x = lk[i] + 1, y = i - n;
				plus[(x+y)/2][(x-y)/2] = true;
			}

		memset(a2,0,sizeof(a2));
		int out = 0;
		for(int i=1; i<=n; i++)
			for(int j=1; j<=n; j++){
				out += cross[i][j];
				out += plus[i][j];
				if(cross[i][j] && plus[i][j])
					a2[i][j] = 'o';
				else
				if(cross[i][j])
					a2[i][j] = 'x';
				else
				if(plus[i][j])
					a2[i][j] = '+';
			}
		lv=0;
		for(int i=1; i<=n; i++)
			for(int j=1; j<=n; j++)
				if(a[i][j] != a2[i][j]){
					v[lv++]= make_pair(i,j);
				}
		printf("Case #%d: %d %d\n",t,out,lv);
		for(int i=0; i<lv; i++){
			int x = v[i].first, y = v[i].second;
			printf("%c %d %d\n",a2[x][y],x,y);
		}
	}
	return 0;
}

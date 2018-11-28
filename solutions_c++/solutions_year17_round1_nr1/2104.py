#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iomanip>
#include<sstream>
#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<bitset>
#define fou(i,j,k) for (int i=j;i<=k;i++)
#define fod(i,j,k) for (int i=j;i>=k;i--)
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> Pii;

const int maxn=110;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;

char ma[maxn][maxn];
int n,m;

void init(){
	scanf("%d%d",&n,&m);
	fou(i,1,n){
		getchar();
		fou(j,1,m){
			ma[i][j]=getchar();
		}
	}
}

void solve(){
	int top,l,r;
	char ch;
	bool flag;
	top=1;
	ch='A';
	fou(i,1,n){
		l=1;flag=false;
		fou(j,1,m)
			if (ma[i][j]!='?'){
				flag=true;
				ch=ma[i][j];
				r=j;
				while (r+1<=m && ma[i][r+1]=='?') r++;
				fou(x,top,i)
					fou(y,l,r) ma[x][y]=ch;
				l=j+1;
			}
		if (flag) top=i+1;
	}
	if (!flag){
		fou(j,1,m){
			top=n-1;
			while (top>=1 && ma[top][j]=='?') top--;
			if (top>=1) ch=ma[top][j];
			fou(i,top+1,n) ma[i][j]=ch;
		}
	}
	fou(i,1,n){
		fou(j,1,m){
			printf("%c",ma[i][j]);
		}
		printf("\n");
	}
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d:\n",i);
		init();
		solve();
	}
	return 0;
}

#include<bits/stdc++.h>


using namespace std;

const int maxn = 30;

int n,m,cas=0;

char st[maxn][maxn];

int xa[maxn],xi[maxn],ya[maxn],yi[maxn];

void Work(){
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)if(st[i][j]=='?'){
			int t=-1;
			for(int k=0;k<26;k++)if(xi[k]){
				bool ok=1;
				for(int x=min(i,xi[k]);x<=max(i,xa[k]);x++)
					for(int y=min(j,yi[k]);y<=max(j,ya[k]);y++)if(st[x][y]!='?'&&st[x][y]!='A'+k)ok=0;
				if(ok){
					t=k;
					break;
				}
			}
			assert(t!=-1);
			xi[t]=min(xi[t],i);xa[t]=max(xa[t],i);
			yi[t]=min(yi[t],j);ya[t]=max(ya[t],j);
			for(int x=xi[t];x<=xa[t];x++)
				for(int y=yi[t];y<=ya[t];y++)st[x][y]='A'+t;
		}
	printf("Case #%d:\n",++cas);
	for(int i=1;i<=n;i++)printf("%s\n",st[i]+1);
}

void Init(){
	scanf("%d%d",&n,&m);
	for(int i=0;i<26;i++)xi[i]=xa[i]=yi[i]=ya[i]=0;
	for(int i=1;i<=n;i++){
		scanf("%s",st[i]+1);
		for(int j=1;j<=m;j++)if(st[i][j]!='?'){
			int t=st[i][j]-'A';
			xi[t]=xa[t]=i;
			yi[t]=ya[t]=j;
		}
	}
}

int main(){
	freopen("A2.in","r",stdin);
	freopen("A2.out","w",stdout);
	int T;
	scanf("%d",&T);
	while(T--)
		Init(),
		Work();
	return 0;
}

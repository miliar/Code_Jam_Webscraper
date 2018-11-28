#include<bits/stdc++.h>
using namespace std;

#define scl(x) scanf("%lld",&x)
#define sc(x)  scanf("%d",&x)
#define ll long long
#define lop(i,n) for(int i=0;i<n;++i)
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;

const int mN=28;

char grid[mN][mN];
int n,m,t;

int main(){
#ifndef ONLINE_JUDGE
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
#endif
	sc(t);
	lop(C,t){
		printf("Case #%d:\n",C+1);

		sc(n),sc(m);
		lop(i,n)scanf(" %s",grid[i]);
		lop(i,n)lop(j,m)if(grid[i][j]!='?'){
			int cj=j;
			while(cj&&grid[i][cj-1]=='?'){
				cj--;
				grid[i][cj]=grid[i][j];
			}
		}
		lop(i,n)lop(j,m)if(grid[i][j]!='?'){
			int cj=j;
			while(cj+1<m&&grid[i][cj+1]=='?'){
				cj++;
				grid[i][cj]=grid[i][j];
			}
		}
		lop(i,n)lop(j,m)if(grid[i][j]!='?'){
			int ci=i;
			while(ci&&grid[ci-1][j]=='?'){
				ci--;
				grid[ci][j]=grid[i][j];
			}
		}
		lop(i,n)lop(j,m)if(grid[i][j]!='?'){
			int ci=i;
			while(ci+1<n&&grid[ci+1][j]=='?'){
				ci++;
				grid[ci][j]=grid[i][j];
			}
		}
		lop(i,n)printf("%s\n",grid[i]);
	}
}

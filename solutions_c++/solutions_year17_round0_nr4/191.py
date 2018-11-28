#include <bits/stdc++.h>

#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;

const int mod=1000000000+7;

int addm(int& a,int b) {return (a+=b)<mod?a:a-=mod;}

template<class T,class U> bool smin(T& a,U b) {return a>b?(a=b,1):0;}
template<class T,class U> bool smax(T& a,U b) {return a<b?(a=b,1):0;}

int T,N,M,nc,bd[2][100][100];
bool modif[100][100];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> T;
	for (int cas=1;cas<=T;cas++) {
		cin >> N >> M;
		nc=0;
		fill(bd[0][0],bd[2][0],0);
		fill(modif[0],modif[100],0);
		for (int c=0;c<M;c++) {
			char cc;int i,j;
			cin >> cc >> i >> j;i--;j--;
			if (cc!='+') bd[0][i][j]=1;
			if (cc!='x') bd[1][i][j]=1;
		}

		for (int i=0;i<N;i++) {
			bool f=0;
			for (int j=0;j<N;j++) if (bd[0][i][j]) f=1;
			if (f) continue;
			for (int j=0;j<N;j++) {
				f=0;
				for (int k=0;k<N;k++) if (bd[0][k][j]) f=1;
				if (!f) {
					bd[0][i][j]=1;
					modif[i][j]=1;
					break;
				}
			}
		}

		for (int c=0;c<2*N-1;c++) {
			int i,j;
			if (c%2==0) i=c/2,j=0;
			else j=N-1-c/2,i=N-1;

			bool f=0;
			for (int x=i,y=j,d=0;d<=c/2;d++,x--,y++) if (bd[1][x][y]) f=1;
			if (f) continue;
			for (int x=i,y=j,d=0;d<=c/2;d++,x--,y++) {
				f=0;
				int u=x-y,v=0;
				if (u<0) {
					v-=u;
					u=0;
				}
				for (;u<N && v<N;u++,v++) if (bd[1][u][v]) f=1;
				if (!f) {
					bd[1][x][y]=1;
					modif[x][y]=1;
					break;
				}
			}
		}

		int score=0,mods=0;
		for (int i=0;i<N;i++) for (int j=0;j<N;j++) {
			score+=bd[0][i][j]+bd[1][i][j];
			mods+=modif[i][j];
		}
		printf("Case #%d: %d %d\n",cas,score,mods);
		for (int i=0;i<N;i++) for (int j=0;j<N;j++) if (modif[i][j]) {
			char cc="x+oo"[bd[0][i][j]+2*bd[1][i][j]-1];
			printf("%c %d %d\n",cc,i+1,j+1);
		}
	}

}

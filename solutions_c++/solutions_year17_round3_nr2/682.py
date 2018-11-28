#include<bits/stdc++.h>
using namespace std;
#define x first
#define y second
int a[2000];
int l[500],r[500];
bool f[725][725][2][255];
//PI4 g[725][725][2][15];
const int N = 720;
void debug() {
	
}
int main() {
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int _t = 1;_t <= T;_t++) {
		int n,m;
		scanf("%d%d",&n,&m);
		memset(a,-1,sizeof a);
		int Min = 10000;
		for (int i=0;i<n+m;i++) {
			int x,y;
			scanf("%d%d",&x,&y);
			l[i] = x;
			r[i] = y;
			Min = min(Min,l[i]);
		}
		for (int i=0;i<n+m;i++) 
			for (int j=l[i] - Min;j < r[i] - Min;j++) a[j] = i < n ? 0 : 1;
		memset(f,0,sizeof f);
		if (a[0] == 0) f[1][0][0][0] = true;
		else f[0][1][1][0] = true;
		for (int i=0;i<=N;i++)
			for (int j=0;j<=N;j++) {
				for (int k=0;k<2;k++)
					for (int l=0;l<250;l++) {
						if (f[i][j][k][l] == false) continue;

						if (a[i + j] >= 0) {
							if (a[i + j] == k) {
								if (k == 0) {
									f[i + 1][j][k][l] = true;
									//g[i+1][j][k][l] = {{i,j},{k,l}};
								}
								else {
									//g[i][j+1][k][l] = {{i,j},{k,l}};
									f[i][j+1][k][l] = true;	
								}
							}
							else {
								if (k == 0) {
									f[i][j + 1][k ^ 1][l + 1] = true;
									//g[i][j + 1][k ^ 1][l + 1] = {{i,j},{k,l}};
								}
								else {
									f[i + 1][j][k ^ 1][l + 1] = true;
									//g[i+1][j][k ^ 1][l + 1] = {{i,j},{k,l}};
								}
							}
						}
						else if (a[i + j] < 0) {
							if (k == 0) {
								f[i + 1][j][k][l] = true;
							//	g[i + 1][j][k][l] = {{i,j},{k,l}};
								f[i][j+1][k ^ 1][l + 1] = true;
								//g[i][j+1][k ^ 1][l + 1] = {{i,j},{k,l}};
							}
							else {
								f[i + 1][j][k ^ 1][l + 1] = true;
							//	g[i + 1][j][k ^ 1][l + 1] = {{i,j},{k,l}};
								f[i][j+1][k][l] = true;	
								//g[i][j+1][k][l] = {{i,j},{k,l}};
							}
						} 
						else printf("???\n");
					}
						
			}
		//cout<<a[2]<<endl;
		//LOG(2,0,0,0);
		//LOG(718,719,1,1);
		//cout<<a[720]<<endl;
		
		int ans = 10000;
		for (int k=0;k<2;k++)
			for (int l=0;l<300;l++)
				if (f[N][N][k][l]) {
					//cout<<k<<' '<<l<<endl;
					if (k == a[0]) ans = min(ans,l);
					else ans = min(ans,l + 1);
				}
		printf("Case #%d: %d\n",_t,ans);
	}
}

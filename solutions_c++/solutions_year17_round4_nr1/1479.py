#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define FOR(i,l,r) for(int i=(l);i<=(r);++i)
#define all(c) begin(c), end(c)
#define uniquenize(v) (v).erase(unique(all(v)), end(v))
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
const int maxn=1e5+1;
const int INF=1e6;
template<class T> inline void maxi(T &a,T b) { if (a<b) a=b; }

int n,P;
int G[101];
int f3[101][101][3],f[101][101][101][4];
int gs[4];
int ans;
int main() {
	int T; scanf("%d",&T);
	FOR (z,1,2) f3[0][0][z]=-INF;
	FOR (z,1,3) f[0][0][0][z]=-INF;

	FOR (tt,1,T) {
		printf("Case #%d: ",tt);
		scanf("%d%d",&n,&P);

		memset(gs,0,sizeof(gs));//FOR (i,1,P-1) gs[i]=0;
		ans=0;

		FOR (i,1,n) {
			scanf("%d",&G[i]);
			if (G[i]%P==0) {
				ans++;
			} else {
				++gs[G[i]%P];
			}
		}

		/*if (P==2) {
			ans+=gs[1]/2+(gs[1]&1);
		} else if (P==3) {
			FOR (z,0,P-1) {
				FOR (i,0,gs[1])
					FOR (j,0,gs[2]) {
						f3[i][j][z]=-INF;
						if (i>0&&f3[i-1][j][z]!=-INF) f3[i][j][(z+1)%P] = max(f3[i][j][(z+1)%P], f3[i-1][j][z]+(z==0));
						if (j>0&&f3[i][j-1][z]!=-INF) f3[i][j][(z+2)%P] = max(f3[i][j][(z+2)%P], f3[i][j-1][z]+(z==0));
					}
			printf("%d\n",f3[gs[1]][gs[2]]);
		} else {
			FOR (z,0,P-1) {
				FOR (i,0,gs[1])
					FOR (j,0,gs[2])
						FOR (k,0,gs[3]) {
							f[i][j][k][z]=-INF;
							if (i>0&&f[i-1][j][k][z]!=-INF) upmax(f[i][j][k][(z+1)%P], f[i-1][j][k][z]+(z==0));
							if (j>0&&f[i][j-1][k][z]!=-INF) upmax(f[i][j][k][(z+2)%P], f[i][j-1][k][z]+(z==0));
							if (k>0&&f[i][j][k-1][z]!=-INF) upmax(f[i][j][k][(z+3)%P], f[i][j][k-1][z]+(z==0));
						}
			printf("%d\n",f[gs[1]][gs[2]][gs[3]]);
		}*/
		FOR (i,0,gs[1])
			FOR (j,0,gs[2])
				FOR (k,0,gs[3])
					FOR (z,0,P-1)
						if (i!=0||j!=0||k!=0) {
							f[i][j][k][z]=-INF;
						}
		
		FOR (i,0,gs[1])
			FOR (j,0,gs[2])
				FOR (k,0,gs[3])
					FOR (z,0,P-1) {
						if (i!=0||j!=0||k!=0) {
							if (i>0&&f[i-1][j][k][z]!=-INF) {
								maxi(f[i][j][k][(z+1)%P], f[i-1][j][k][z]+(z==0));
							}
							/*	if (i==2&&j==1&&k==0&&z==0) {
							printf("%d %d %d %d %d\n",i-1,j,k,z,f[i-1][j][k][z]);
									cout<<f[i-1][j][k][z]<<" haha "<<f[i][j][k][(z+1)%P]<<endl;
								}*/
							if (j>0&&f[i][j-1][k][z]!=-INF) maxi(f[i][j][k][(z+2)%P], f[i][j-1][k][z]+(z==0));
							if (k>0&&f[i][j][k-1][z]!=-INF) maxi(f[i][j][k][(z+3)%P], f[i][j][k-1][z]+(z==0));
						}
					}
		/*FOR (z,0,P-1)
			FOR (i,0,gs[1])
				FOR (j,0,gs[2])
					FOR (k,0,gs[3])
						if (i!=0||j!=0||k!=0) {
							printf("%d %d %d %d %d\n",i,j,k,z,f[i][j][k][z]);
						}*/
		int mx=0;
		FOR (z,0,P-1) mx=max(mx,f[gs[1]][gs[2]][gs[3]][z]);
		//cout<<ans<<" "<<mx<<endl;
		printf("%d\n",ans+mx);

	}
	return 0;
}


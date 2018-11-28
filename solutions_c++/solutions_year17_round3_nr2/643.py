#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i,l,r) for(int i=(l);i<=(r);i++)

//#define DEBUG
#ifdef DEBUG
#define print(...) fprintf(stderr, __VA_ARGS__)
#else
#define print(...) 
#endif
#define dbg(x) cout<<#x<<" = "<<x<<endl

template<typename T,typename S>inline bool upmin(T&a,const S&b){return a>b?a=b,1:0;}
template<typename T,typename S>inline bool upmax(T&a,const S&b){return a<b?a=b,1:0;}
#define mmo(a,b) (((a)=1ll*(a)*(b)%mo)<0?(a)+=mo:(a))  //<--
#define buli(x) (__builtin_popcountll(x))
#define bur0(x) (__builtin_ctzll(x))
#define bul2(x) (63-__builtin_clzll(x))

using namespace std;
typedef long long LL;
const int maxn=1e5+1;
const int INF=0x7ffffff;

int Ac,Aj;
int a[1500];
int f[2][1500][2][2];  //2nd: Ac time cost on baby care, 3rd: (Ac: 0, Aj: 1)
int main() {
	int T; scanf("%d",&T);
	FOR (tt,1,T) {
		scanf("%d%d",&Ac,&Aj);
		FOR (i,1,1440) a[i]=0;
		for (int i=1;i<=Ac;i++) {
			int c,d;
			scanf("%d%d",&c,&d);
			FOR (j,c+1,d) a[j]=1;
		}
		FOR (i,1,Aj) {
			int j,k;
			scanf("%d%d",&j,&k);
			FOR (p,j+1,k) a[p]=2;
		}

		int p=0;
		FOR (i,0,720) FOR (j,0,1) FOR (k,0,1) f[p][i][j][k]=INF;
		f[p][0][0][0]=0; f[p][0][1][1]=0;
		FOR (i,1,1440) {
			p=!p;
			FOR (z,0,1) {
				FOR (j,0,720) FOR (k,0,1) f[p][j][k][z]=INF;  //
				if (a[i]==0) {
					FOR (j,0,min(720,i)) {
						if (j>0) f[p][j][0][z]=min(f[!p][j-1][0][z],f[!p][j-1][1][z]+1);
						if (j<i) f[p][j][1][z]=min(f[!p][j][1][z],f[!p][j][0][z]+1);
					}
				} else if (a[i]==1) {  //Aj baby care time
					FOR (j,0,min(720,i)) {
						if (j<i) f[p][j][1][z]=min(f[!p][j][1][z],f[!p][j][0][z]+1);
					}
				} else {  //Ac baby care time
					FOR (j,0,min(720,i)) {
						if (j>0) f[p][j][0][z]=min(f[!p][j-1][0][z],f[!p][j-1][1][z]+1);
					}
				}
				// cout<<f[p][0][0][z]<<endl;
				// FOR (j,0,min(720,i)) FOR (k,0,1) cout<<i<<" "<<j<<" "<<k<<" "<<z<<" "<<f[p][j][k][z]<<endl;
			}
		}
		// for (int i=1;i<=1440;i++) {
		// 	p=!p;
		// 	if (a[i]==0) {
		// 		FOR (j,0,min(720,i)) {
		// 			if (j>0) f[p][j][0]=min(f[!p][j-1][0],f[!p][j-1][1]+1);
		// 			f[p][j][1]=min(f[!p][j][1],f[!p][j][0]+1);
		// 		}
		// 	} else if (a[i]==1) {  //Aj baby care time
		// 		FOR (j,0,min(720,i)) {
		// 			f[p][j][0]=INF;
		// 			f[p][j][1]=min(f[!p][j][1],f[!p][j][0]+1);
		// 		}
		// 	} else {  //Ac baby care time
		// 		FOR (j,0,min(720,i)) {
		// 			if (j>0) f[p][j][0]=min(f[!p][j-1][0],f[!p][j-1][1]+1);
		// 			f[p][j][1]=INF;
		// 		}
		// 	}
		// }

		int ans=INF;
		FOR (z,0,1) ans=min(ans,f[p][720][z][z]);//,cout<<z<<" "<<zz<<" "<<f[p][720][z][zz]<<endl;
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}

#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define itt ::iterator
#define ritt ::reverse_iterator
#define MAXPQ(T) priority_queue<T>
#define MINPQ(T) priority_queue<T,vector<T>,greater<T> >
const int NSIZ=1010;
const int MSIZ=1000010;
const int inf=1010580540;
const int mxint=2147483647;
const long long mxll=9223372036854775807LL;
const long long prime15=1000000000000037LL;
const long long mod=1000000007LL;
const long long mod9=1000000009LL;
typedef pair<int,int> pii;
typedef pair<long long,int> pli;
typedef pair<long long,long long> pll;
typedef pair<double,int> pdi;
typedef pair<int,pair<int,int> > pip;
typedef pair<long long,pair<int,int> > plp;
typedef pair<pair<int,int>,pair<int,int> > ppp;

int n, m, o, re=0, test;
long long res=0;
pii a[NSIZ];
long long sp[NSIZ][NSIZ];
vector<pii> ve[NSIZ];
vector<double> ans;
char c[NSIZ];
bool chk[NSIZ];
MINPQ(pdi) pq;
double dijk(int d, int fin){
	while(!pq.empty())pq.pop();
	memset(chk,0,sizeof(chk));
	// printf("=%d %d\n", d, fin);
	pq.push(pdi(0.0,d));
	while(!pq.empty()){
		pdi p=pq.top();pq.pop();
		// printf(".%lf %d\n", p);
		if(chk[p.S]==1)continue;
		chk[p.S]=1;
		if(p.S==fin)return p.F;
		for(int i=1; i<=n; i++){
			if(chk[i]==1)continue;
			if(sp[p.S][i]>a[p.S].F)continue;
			pq.push(pdi(p.F+((double)sp[p.S][i]/a[p.S].S),i));
		}
	}
    return -1;
}
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
    	scanf("%d %d", &n, &m);
    	ans.clear();
    	for(i=1; i<=n; i++){
    		for(j=1; j<=n; j++){
    			sp[i][j]=2e18;
    		}
    	}
    	for(i=1; i<=n; i++){
    		scanf("%d %d", &a[i].F, &a[i].S);
    	}
    	for(i=1; i<=n; i++){
    		sp[i][i]=0;
    		for(j=1; j<=n; j++){
    			scanf("%d", &k);
    			if(k==-1)continue;
    			ve[i].push_back(pii(j,k));
    			sp[i][j]=k;
    		}
    	}
    	for(k=1; k<=n; k++){
    		for(i=1; i<=n; i++){
    			for(j=1; j<=n; j++){
    				sp[i][j]=min(sp[i][j],sp[i][k]+sp[k][j]);
    			}
    		}
    	}
    	// for(i=1; i<=n; i++){
    	// 	for(j=1; j<=n; j++){
    	// 		printf("%d %d = %lld\n", i, j, sp[i][j]);
    	// 	}
    	// }
    	printf("Case #%d: ", zz);
    	for(int qq=0; qq<m; qq++){
    		scanf("%d %d", &k, &l);
    		printf("%.8lf ", dijk(k,l));
    	}
    	printf("\n");
    }
    return 0;
}
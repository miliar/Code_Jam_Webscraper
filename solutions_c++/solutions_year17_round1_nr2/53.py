#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;
typedef long long ll;

int n,m,k;
int r[64];
int q[64][64];
int w[64];

bool rem(){
	fore(i,0,n)if(w[i]==m)return false;
	return true;
}

int main(){
	int tn;
	scanf("%d",&tn);
	fore(tc,1,tn+1){
		printf("Case #%d: ",tc);
		scanf("%d%d",&n,&m);
		fore(i,0,n)scanf("%d",r+i);
		fore(i,0,n){
			fore(j,0,m)scanf("%d",&q[i][j]);
			sort(q[i],q[i]+m);
		}
		memset(w,0,sizeof(w));k=1;
		int rr=0;
		while(rem()){
			fore(i,0,n)k=max(k,(q[i][w[i]]*10+r[i]*11-1)/(r[i]*11));
			bool c=true;
			fore(i,0,n){
				if(q[i][w[i]]*10<9*k*r[i]){
					w[i]++;
					c=false;
				}
			}
			if(!c)continue;
			rr++;
			fore(i,0,n)w[i]++;
		}
		printf("%d\n",rr);
	}
	return 0;
}

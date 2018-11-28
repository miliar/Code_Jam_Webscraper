#include <cstdio>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#define pii pair<int,int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
using namespace std;
typedef long long ll;

#define MX 1005
int ary[MX],spd[MX];
double tim[MX];

int main() {
	int D,N,i,j,k,T,C,S,f,sz;
	scanf("%i",&C);
	for(T=1;T<=C;++T) {
		printf("Case #%i: ",T);
		scanf("%i%i",&D,&N);
		for(i=0;i<N;++i) scanf("%i%i",ary+i,spd+i);
		double mx=0;
		for(i=0;i<N;++i){
			tim[i]=((double)(D-ary[i]))/((double)(spd[i]));
			mx = max(mx,tim[i]);
		}
		
		
		printf("%lf",D/mx);
		if(T!=C) printf("\n");
	}
}
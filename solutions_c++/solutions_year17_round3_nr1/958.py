#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
#define F(i,n) for(int i=1; i<=n; i++)
#define r first
#define h second
typedef pair<long long int,long long int> P;
const double pi = acos(-1);

int N, K;
long long int tmp, mr;
double ans;
P pan[1005];
bool cmp(P a, P b){
	if(a.r*a.h!= b.r*b.h)
		return a.r*a.h > b.r*b.h;
	else return a.r > b.r;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
	scanf("%d",&T);
    for(int cases=1; cases<=T; cases++){
    	ans = tmp = mr = 0;
    	printf("Case #%d: ",cases);
    	scanf("%d %d",&N,&K);
    	F(i,N){
    		scanf("%lld %lld",&pan[i].r, &pan[i].h);
		}
		sort(pan+1, pan+1+N, cmp);
		F(i, K-1) {
			ans+=2*pan[i].r*pan[i].h;
			if(pan[i].r > mr) mr = pan[i].r;
		}
		if(pan[K].r > mr) tmp = pan[K].r*pan[K].r + 2*pan[K].r*pan[K].h;
		else tmp = mr*mr + 2*pan[K].r*pan[K].h;
		for(int i=K; i<=N; i++){
			if(pan[i].r * pan[i].r + 2*pan[i].r*pan[i].h > tmp && pan[i].r> mr) tmp =  pan[i].r * pan[i].r + 2*pan[i].r*pan[i].h;
		}
		ans+=tmp;
		ans*=pi;
		printf("%.9lf\n",ans);
	}
    return 0;
}

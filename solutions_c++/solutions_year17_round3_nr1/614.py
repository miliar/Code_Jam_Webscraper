#include <bits/stdc++.h>

#define lld long long
#define pi 3.14159265358979323846

using namespace std;

struct data{
	lld r,h;
}a[1002];

void process(){
	int N,K;

	scanf("%d %d",&N,&K);
	for(int i=1; i<=N; i++){
        scanf("%lld %lld",&a[i].r,&a[i].h);
	}
    sort(a+1,a+N+1,[&](data x,data y){
		return x.r < y.r;
    });
    lld ans = 0;
    for(int i=K; i<=N; i++){
        vector<lld> tmp;
		for(int j=1; j<i; j++) tmp.push_back(a[j].r*a[j].h*2);
        sort(tmp.begin(),tmp.end());
        reverse(tmp.begin(),tmp.end());
        lld sum = a[i].r*a[i].h*2;
		for(int j=1; j<K; j++) sum += tmp[j-1];
        sum += (a[i].r*a[i].r);
        ans = max(sum,ans);
    }
    double aans = (double)ans * (double)pi;
    printf("%.8f\n",aans);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; i++){
		printf("Case #%d: ",i);
		process();
	}

	return 0;
}

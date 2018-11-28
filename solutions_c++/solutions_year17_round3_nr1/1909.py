#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<queue>
#include<vector>
#include<set>
#include<stack>
#include<map>
#include<ctime>
#include<bitset>
#define LL long  long
#define db double
#define EPS 1e-8
#define inf 1e9
#define pi 3.1415926535898
using namespace std;

typedef struct cake{
    double r,h;
};

bool comparison(cake a,cake b){
    return (a.r*a.h)>(b.r*b.h);
}
bool cmp1(cake a,cake b){
    return a.r>b.r;
}

void run(){
    int n,k;
    cake fuck;
    vector<cake> cakee;
    scanf("%d %d",&n,&k);
    for (int i=0;i<n;i++){
        scanf("%lf %lf",&fuck.r,&fuck.h);
        cakee.push_back(fuck);

    }
    double ans=0;
    sort(cakee.begin(),cakee.end(),cmp1);

    for (int i=0;i<=n-k;++i){
        double maxr=cakee[i].r;
        vector<cake> vec;
        for(int j=i+1;j<n;++j){
            vec.push_back(cakee[j]);
        }
        sort(vec.begin(),vec.end(),comparison);
        double sumare=cakee[i].r*cakee[i].h;
        for (int j=0;j<k-1;++j)
            sumare+=vec[j].r*vec[j].h;
        ans=max(ans,pi*(maxr*maxr+2*sumare));
    }
    printf("%.10f\n",ans);

}

int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T;
    scanf("%d", &T);
	for (int i=1; i<=T; i++){
		printf("Case #%d: ",i);
		run();
	}
    return 0;
}

#include <bits/stdc++.h>
#define in_T int t;for(scanf("%d",&t);t--;)
#define in_I(a) scanf("%d",&a)
#define in_F(a) scanf("%lf",&a)
#define in_L(a) scanf("%lld",&a)
#define in_S(a) scanf("%s",a)
#define newline printf("\n")
#define BE(a) a.begin(), a.end()
using namespace std;

const long double eps = 1e-9;
long double getans(vector<long double> &P, long double U, long double target){
    long double ret = 1;
    long double U2 = 0;
    for(long double p: P){
        U2 += max((long double)0, target-p);
        ret *= max(target, p);
    }
    if(U2 > U)
        return -100;
    return ret;
}
int main(){
    int z = 0;
    int T;
    cin>>T;
    while(T--){
        z++;
        int N, K;
        long double U;
        cin>>N>>K>>U;
        vector<long double> P;
        long double sum = 0;
        for(int i = 0;i<N;i++){
            long double X;
            cin>>X;
            P.push_back(X);
            sum += X;
        }
        long double st = 0, end = 1;
        int cnt = 0;
        long double ans;
        while(st < end){
            cnt++;
            if(cnt == 1000000)
                break;
            long double mid = (st + end)/2;
            long double annn = getans(P, U, mid);
            if(annn > -1){
                ans = annn;
                st = mid;
            }else end = mid;
        }
        printf("Case #%d: %.9Lf\n", z, ans);
    }
}

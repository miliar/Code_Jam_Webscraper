#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define si(X) scanf("%d", &(X))
#define sll(X) scanf("%lld",&(X))
#define INFL 0x3f3f3f3f3f3f3f3fLL
const int mod = 1e9+7;
ll gcd(ll a,ll b){
	if(b==0)
	return a;return gcd(b,a%b);
}
ll expo(ll base,ll pow){
    ll ans = 1;
    while(pow!=0){
        if(pow&1==1){
            ans = ans*base;
            ans = ans%mod;
        }
        base *= base;base%=mod;
        pow/=2;
    }return ans;
}
ll inv(ll x){
    return expo(x,mod-2);
}

double pi = 3.141592653589793238462643;
double error = 0.0000001;
int dx[8] = {1 , 0 , -1 , 0 , 1 , -1 , -1 , 1};    // last 4 diagonal
int dy[8] = {0 , 1 , 0 , -1 , 1 , 1 , -1 , -1};
/* -------Template ends here-------- */

const int M = 100001;

int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int T;
    si(T);

    for(int alp = 1 ; alp <= T ; alp++){
        //int ans = 0;

        double las;
        int n;
        cin >> las >> n;
        double t_m = 0;

        for(int i = 1 ; i <= n ; i++){
            double here , speed;
            cin >> here >> speed;
            t_m = max(t_m , (las - here)/speed);
        }
        double ans = las/t_m;







        printf("Case #%d: " , alp);
        printf("%.6f\n" , ans);

    }


}

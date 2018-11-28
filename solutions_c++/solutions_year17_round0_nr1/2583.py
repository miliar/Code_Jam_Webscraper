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

const int M = 1005;
int arr[M];
int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int T;
    si(T);

    for(int alp = 1 ; alp <= T ; alp++){
        int ans = 0;


        string str;
        cin >> str;
        int n = str.length();
        int k;
        si(k);

        for(int i = 0 ; i < M ; i++){
            arr[i] = 0;
        }

        for(int i = 0 ; i<n ; i++){
            if(str[i] == '+'){
                arr[i + 1] = 1;
            }
        }

        int o = 0;

        for(int i = 1 ; i <= n ; i++){
            if(arr[i]) continue;
            int ri = i + k - 1;
            if(ri > n){
                o++;
                break;
            }
            ans++;
            for(int j = i ; j <= ri ; j++){
                arr[j] = 1 - arr[j];
            }
        }

        printf("Case #%d: " , alp);

        if(o){
            printf("IMPOSSIBLE\n");
            continue;
        }
        printf("%d\n" , ans);

    }




















}













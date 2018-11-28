#include <bits\stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
int T;

ll powx(ll a, ll n)
{
    ll r = 1;
    ll q = a;
    while (n>0)
    {
        if (n & 1)
            r = (r*q);
        q = (q*q);
        n = n >> 1;
    }
    return r;
}

ll repu(int k){
    return (powx(10ll,k)-1)/9;
}

vector<int> todigits(ll n){
    vector<int> d;
    while(n){
        d.push_back(n%10);
        n/=10;
    }
    return d;
}

void solvesmall(int testi){
    int N;
    scanf("%d",&N);
    while(N){
        vector<int> d = todigits(N);
        int ok = 1;
        for(int i=0; i<d.size()-1; i++)
            ok &= d[i]>=d[i+1];
        if (ok){
            printf("Case #%d: %d\n",testi, N);
            return;
        }
        N--;
    }
}

void solve(int testi){
    ll N;
    scanf("%lld",&N);
    vector<int> d = todigits(N);
    ll sol = 0;
    ll dp[20][10]{};
    ll ten = powx(10ll, d.size()-1);
    int rem = d.size();
    for(int i=1; i<=d.size(); i++){
        for(int j=0; j<10; j++){
            for(int k=0; k<=j; k++){
                if (dp[i-1][k]+repu(rem)*j<=N)
                    dp[i][j] = max(dp[i][j],dp[i-1][k]+ten*j);
            }
        }
        ten /= 10;
        rem--;
    }
    for(int j=0; j<10; j++)
        sol = max(sol, dp[d.size()][j]);
    printf("Case #%d: %lld\n",testi, sol);
}

int main(){
	#ifdef LOCAL_PROJECT
		freopen("d:\\src\\CppProjects\\stdin","r",stdin);
		freopen("d:\\src\\CppProjects\\stdout","w",stdout);
	#endif
	scanf("%d",&T);
	for(int testi = 1; testi<=T; testi++)
        solve(testi);
	return 0;
}

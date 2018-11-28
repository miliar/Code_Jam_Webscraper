//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<int(n); ++i)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

int extra() {
    ll n, k, p;
    cin >> n >> k;
    k--;
    map<ll, ll> M;
    M[-n] = 1;
    while(k > 0) {
        n = -M.begin()->first;
        p = M.begin()->second;
        M.erase(M.begin());

        ll pocet = min(k, p);
        if (p > pocet) {
            M[-n] = p;
        }
        ll pol = (n - 1) / 2;
        if (pocet > 0 && pol > 0) {
            M[-pol] += pocet;
        }
        if (pocet > 0 && n-1-pol > 0) {
            M[-(n-1-pol)] += pocet;
        }
        k -= pocet;
    }
    n = -M.begin()->first;
    cout << (n-1) - (n-1)/2 << " " << (n-1)/2 << endl;
}

int main() {
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}

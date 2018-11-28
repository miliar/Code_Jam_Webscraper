#include<cstdio>
#include<iostream>
#include<sstream>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<string>
#include<cstring>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<ctime>
#include<vector>
#include<fstream>
#include<list>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define ms(s) memset(s,0,sizeof(s))

const double PI = 3.141592653589;
const int INF = 0x3fffffff;

long long base[100];
long long sum[100];

long long solve(ll n, ll k) {
    int layer = 0;
    while(k > sum[layer])
        layer++;
    k -= sum[layer-1];
    
    ll num = n/(base[layer-1]);
    ll counts = base[layer-1] - (base[layer-1]*num - (n - sum[layer-1]));
    if(k <= counts)
        return num;
    else
        return num-1;
}

int main() {
//        freopen("/Users/really/Documents/code/C-large.in","r",stdin);
//        freopen("/Users/really/Documents/code/output","w",stdout);
    ios::sync_with_stdio(false);
    
    //getBase
    base[0] = 1;
    for(int i = 1; i <= 63; i++)
        base[i] = base[i-1] * 2;
    sum[0] = 0;
    for(int i = 1; i <= 60; i++)
        sum[i] = sum[i-1] + base[i-1];
    //start
    int t;
    ll n, k;
    cin >> t;
    for(int cas = 1; cas <= t; cas++) {
        cin >> n >> k;
        ll t = solve(n, k);
        if(t%2 != 0)
            cout << "Case #" << cas << ": " << t/2 << " " << t/2 << endl;
        else
            cout << "Case #" << cas << ": " << t/2 << " " << t/2 - 1 << endl;
    }
    
    
    
    return 0;
}

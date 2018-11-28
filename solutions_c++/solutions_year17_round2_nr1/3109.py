#include <iostream>
#include <queue>
#include <cmath>
#include <stdio.h>

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pll;


void process(ll d, ll n, vector<ll> k, vector<ll> s){
    // println(k)
    // priority_queue<pll, vector<pll>, compare> pq;
    double m = 0;
    for(int j = 0; j < n; j++){
        if (d > k[j])
        m = max(m, double(d-k[j])/s[j]);
        // cout << "test: " << n << " "<< k[j] << endl  ;
    }
    // cout << d/m ;
    printf( "%.6f", d/m);
}


int main()
{
    int T, i;
    ll d,n;
    vector<ll> k,s;
    cin >> T;
    i = T;
    while (i-- > 0)
    {
        cin >> d >> n;
        k.resize(n);
        s.resize(n);
        for(int j = 0; j < n; j++){
            cin >> k[j] >> s[j];
            // cout << 
        }
        cout << "Case #" << T - i << ": ";
        process(d,n,k, s);
        cout << endl;
    }
}
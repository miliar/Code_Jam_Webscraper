#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <climits>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

using namespace std;
#define fast ios::sync_with_stdio(false);cin.tie(0); cout.tie(0);
#define pb push_back
#define sz(s) (int)s.size()
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()

typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<ll> vl;
const ll N= (ll)1e5+7;
const ll mod = (ll) 1e9+7;

int main() {
    fast
    freopen("/Users/gauravsharma/Downloads/C-small-2-attempt0.in.txt", "r", stdin);
    freopen("/Users/gauravsharma/Desktop/output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int kase = 1; kase <= t; kase++) {
        priority_queue<int> pq;
        int n,k,x,mx=0,mn=0;
        cin>>n>>k;
        pq.push(n);
        for(int i=0;i<k;i++){
            x=pq.top();
            pq.pop();
            if(x==0){
                mx=0;
                mn=0;
                break;
            }
            pq.push((int)floor((double)(x-1)/2));
            pq.push((int)ceil((double)(x-1)/2));
            mx=(int)ceil((double)(x-1)/2);
            mn=(int)floor((double)(x-1)/2);
        }
        cout<<"Case #"<<kase<<": "<<mx<<" "<<mn<<endl;
    }
    return 0;
}

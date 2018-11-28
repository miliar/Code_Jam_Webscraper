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

int n,k,ans;
string s;

int main() {
    fast
    freopen("/Users/gauravsharma/Downloads/A-large.in.txt", "r", stdin);
    freopen("/Users/gauravsharma/Desktop/output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int kase = 1; kase <= t; kase++) {
        cin>>s>>k;
        ans=0;
        for(int i=0;i<sz(s)-k+1;i++){
            if(s[i]=='-'){
                for(int j=0;j<k;j++){
                    if(s[i+j]=='+') s[i+j]='-';
                    else s[i+j]='+';
                }
                ans++;
            }
        }

        for(int i=0;i<sz(s);i++){
            if(s[i]=='-') ans=-1;
        }
        if(ans==-1) cout<<"Case #"<<kase<<": "<<"IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<kase<<": "<<ans<<endl;
    }
    return 0;
}

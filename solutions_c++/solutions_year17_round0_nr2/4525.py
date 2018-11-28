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

string s;

int main() {
    fast
    freopen("/Users/gauravsharma/Downloads/B-large.in.txt", "r", stdin);
    freopen("/Users/gauravsharma/Desktop/output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int kase = 1; kase <= t; kase++) {
        cin>>s;
        int i;
        for(i=0;i<sz(s)-1;i++){
            if(s[i]>s[i+1]){
                for(int j=i+1;j<sz(s);j++) s[j]='9';
                s[i]--;
                break;
            }
        }

        while(i>=0 and s[i-1]>s[i]){
            s[i-1]--;
            s[i]='9';
            i--;
        }
        string ans;
        if(s[0]=='0'){
            string st(sz(s)-1,'9');
            ans=st;
        }else{
            ans=s;
        }

        cout<<"Case #"<<kase<<": "<<ans<<endl;
    }
    return 0;
}

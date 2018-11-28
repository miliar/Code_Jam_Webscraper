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
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define for1(i,n) for(int i=1;i<=(int)n;i++)

typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<ll> vl;
const ll N= (ll)1e5+7;
const ll mod = (ll) 1e9+7;

int main() {
    fast
    freopen("/Users/gauravsharma/Downloads/A-large.in-2.txt", "r", stdin);
    freopen("/Users/gauravsharma/Desktop/output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int kase = 1; kase <= t; kase++) {
        int n,m,ans,vis[30][30]={0};
        string s[30];
        cin>>n>>m;
        forn(i,n) cin>>s[i];

        forn(i,n){
            forn(j,m){
                if(s[i][j]=='?' or vis[i][j]) continue;
                char c = s[i][j];
                int l=j,r=j,u=-1,d=n;
                for( ;l>=0;l--){
                    if(s[i][l]!=c and s[i][l]!='?') break;
                }
                for( ;r<m;r++){
                    if(s[i][r]!=c and s[i][r]!='?') break;
                }
                bool up=false,down=false;
                for(int col = l+1;col<r;col++){
                    for(int row=i;row>=0;row--){
                        if(s[row][col]!=c and s[row][col]!='?'){
                            up=true;
                            u=max(u,row);
                        }
                    }
                    for(int row=i;row<n;row++){
                        if(s[row][col]!=c and s[row][col]!='?'){
                            down=true;
                            d=min(d,row);
                        }
                    }
                }

                if(!up) u=-1;
                if(!down) d=n;

                for(int row=u+1;row<d;row++){
                    for(int col=l+1;col<r;col++){
                        s[row][col]=c;
                        vis[row][col]=1;
                    }
                }
            }
        }

        cout<<"Case #"<<kase<<":"<<endl;
        for(int i=0;i<n;i++,cout<<endl){
            for(int j=0;j<m;j++){
                cout<<s[i][j];
            }
        }
    }
    return 0;
}

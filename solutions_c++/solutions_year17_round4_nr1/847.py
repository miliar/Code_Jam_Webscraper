#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long ll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(i,c)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

typedef pair<int,int> ii;
typedef pair<double,double> dd;

#include <cassert>


int solve(int N, int P, vector<int>& G) {




    map<int,int> m;
    rep(i,N) {
        int r = G[i] % P;
        m[r]++;
    }

    int ans = m[0];
    switch (P) {
        case 2:{
            ans += (m[1]+1)/2;
            break;
        }
        case 3:{
            int x = min(m[1], m[2]);

            ans += x;
            m[1] -= x; m[2] -= x;

            int y = m[1]+m[2];
            ans += (y+2)/3;

            break;
        }
        case 4:{
            ans += m[2]/2;
            m[2] %= 2;

            int x = min(m[1], m[3]);
            ans += x;
            m[1] -= x; m[3] -= x;

            int y = m[1]+m[3];
            if (m[2]) {
                if (y>=2) {
                    ans++; y-=2;
                    ans += (y+3)/4;
                } else {
                    ans++;
                }
            } else {
                ans += (y+3)/4;
            }
            break;
        }
    }
    return ans;
}

int main(){
    int _T; cin>>_T;
    rep(_t,_T){
        int N, P; cin >> N >> P;
        vector<int> G(N);
        rep(n,N) cin >> G[n];
        int ans = solve(N,P,G);
    answer:
        cout << "Case #" << (1+_t) << ": " << ans << endl;
    }
}

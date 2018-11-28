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



#include <cassert>


string sub(vector<ii>& s) {


    int L = s[0].first;
    vector<vector<int> > p(L*2);

    int c0 = s[0].second;
    rep(i, L) p[2*i].push_back(c0);

    int c1 = s[1].second;
    for (int i=0,c=s[1].first; i<c; ++i) {
        p[2*i+1].push_back(c1);
    }

    int c2 = s[2].second;
    for (int i=0,c=s[2].first; i<c; ++i) {
        p[2*(L-1-i)+1].push_back(c2);
    }

    stringstream ss;
    rep(i, L*2) {
        int np = p[i].size();
        assert(np == 1 || np == 2);
        rep(j, np) {
            int c = p[i][j];
            ss << ("ROYGBV"[c]);
        }
    }
    return ss.str();
}

string solve_s(int N, vector<int>& ROYGBV) {
    int R = ROYGBV[0], Y = ROYGBV[2], B = ROYGBV[4];
    if (R > Y+B || Y > B+R || B > R+Y) {
        return "IMPOSSIBLE";
    }
    vector<ii> s;
    s.push_back(ii(R,0));
    s.push_back(ii(Y,2));
    s.push_back(ii(B,4));
    sort(all(s)); reverse(all(s));
    return sub(s);

    return "POSSIBLE";

}

int main(){
  int _T; cin>>_T;
  rep(_t,_T){
    vector<int> ROYGBV(6);
    int N; cin >> N;
    rep(i, 6) cin >> ROYGBV[i];

 answer:
    cout << "Case #" << (1+_t) << ": ";
    cout << solve_s(N, ROYGBV);
    cout << endl;
  }
}

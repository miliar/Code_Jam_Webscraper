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

typedef pair<int, int> ii;


int solve_l(string& S, int k) {
    int LS = S.size();

    vector<bool> t(LS);
    rep(i, LS) t[i] = (S[i] == '-');

    int c = 0;
    for (int i=0; i<=LS-k; ++i) {
        if (t[i]) {
            for (int j=0; j<k; ++j) {
                t[i+j] = !t[i+j];
            }
            ++c;
        }
    }
    for (int i=LS-k+1; i<LS; ++i) {
        if (t[i]) return -1;
    }
    return c;
}

int main(){
  int _T; cin>>_T;
  rep(_t,_T){
    string S; cin >> S;
    int LS = S.size();
    int K; cin >> K;

    int ans = solve_l(S, K);

 answer:
    cout << "Case #" << (1+_t) << ": ";
    if (ans >= 0) {
      cout << ans;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << endl;
  }
}

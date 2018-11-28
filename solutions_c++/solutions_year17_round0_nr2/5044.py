#include <iostream>
#include <cstdio>
#include <string>
#include <sstream> 
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <ctime>
#include <cassert>
using namespace std;
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define vi vector<int>
#define vpii vector<pii>
#define SZ(x) ((int)(x.size()))
#define fi first
#define se second
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FORI(i,n) for(int (i)=1;(i)<=(n);++(i))
#define IN(x,y) ((y).find((x))!=(y).end())
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));
#define DBG cerr << "debug here" << endl;
#define DBGV(vari) cerr << #vari<< " = "<< (vari) <<endl;

typedef long long ll;
const int INF = 1e9;

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int tid = 1; tid <= t; ++tid) {
        string s;
        cin >> s;
        int n = s.size();
        vector<int> v;
        for (int i = 0; i < n; ++i) v.pb(s[i]-'0');
        int idx = -1;
        for (int i = 0; i < n-1; ++i) {
            if (v[i] > v[i+1]) {
                idx = i;
                break;
            }
        }
        if (idx != -1) {
            while (idx >= 1 && v[idx-1] == v[idx]) --idx;
            v[idx] = v[idx]-1;
            for (int i = idx+1; i < n; ++i) {
                v[i] = 9;
            }
        }

        string ans;
        for (int i = 0; i < n; ++i) {
            if (ans.size() == 0 && v[i] == 0) continue;
            ans += char('0' + v[i]);
        }
        cout << "Case #" << tid << ": " << ans << endl;
    }
    return 0;
}

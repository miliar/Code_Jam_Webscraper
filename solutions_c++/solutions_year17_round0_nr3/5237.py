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

const int N = 1e6;
bool a[N+2];
int L[N+2];
int R[N+2];

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int tid = 1; tid <= t; ++tid) {
        int n, k;
        cin >> n >> k;
        priority_queue<int> Q;
        Q.push(n);
        for (int kid = 1; kid <= k; ++kid) {
            int b = Q.top()-1;
            Q.pop();
            int b1 = ceil(b/2.0);
            int b2 = floor(b/2.0);
            if (kid == k) {
                cout << "Case #" << tid << ": " << b1 << " " << b2 << endl;
                break;
            }
            Q.push(b1);
            Q.push(b2);
        }
    }
    return 0;
}

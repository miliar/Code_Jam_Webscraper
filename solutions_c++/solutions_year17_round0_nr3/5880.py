#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define fi first
#define se second

using namespace std;

typedef long long int64;
typedef pair<int, int> ii;

const double EPS = 1e-9;
const int INF = 0x3f3f3f3f;

int sgn(double a) { return ((a > EPS) ? (1) : ((a < -EPS) ? (-1) : (0))); }
int cmp(double a, double b = 0.0) { return sgn(a - b); }

typedef pair<int, ii> node;

int main(){
    ios::sync_with_stdio(false);
    int t;
    int n, k;
    cin >> t;
    for (int cs = 1; cs <= t; cs++){
        cout << "Case #" << cs << ": ";
        cin >> n >> k;
        priority_queue<ii> q;
        n--;
        int x = floor(n/2.0), y = ceil(n/2.0);
        q.push(mp(y, x));
        int ans = 0;
        while (!q.empty()){
            ii at = q.top(); q.pop();
            ans++;
            if (ans == k){
                cout << at.fi << " " << at.se << "\n";
                break;
            }
            y = at.fi, x = at.se;
            if (x > 0) q.push(mp(ceil((x-1)/2.0), floor((x-1)/2.0)));
            if (y > 0) q.push(mp(ceil((y-1)/2.0), floor((y-1)/2.0)));
        }
    }
    return 0;
}
//O....O
//O.O..O
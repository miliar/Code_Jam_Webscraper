#include <bits/stdc++.h>
using namespace std;
#define readfiles freopen("/home/andrewiski/NetBeansProjects/ACM/in.txt","r",stdin);freopen("/home/andrewiski/NetBeansProjects/ACM/out.txt","w",stdout)
#define clr(x,y) memset(x,y,sizeof(x))
#define pb push_back
#define mp make_pair
#define eps (1e-9)
#define oo (0x7fffffff)
#define OO (0x7fffffffffffffff)
#define PI acos(-1)
#define sqr(x) ((x)*(x))
#define moder (1000000007l)
#define ABS(x) ((x>0)?x:-x)
#define LOG2(x) ((log10(x))/(log10(2)))
#define UNSET(n,x) (n&(~(1 << x)))
#define SET(n,x) (n|(1<<x))
typedef long long int ll;
typedef unsigned long long int ull;
#define MAXN 7

typedef pair<int, pair<int, int> > range;

void solve() {
    int cases;
    cin>>cases;
    int c=0;
    while (cases--) {
        c++;
        priority_queue<pair<int, pair<int, int> > > pq;
        int n, k;
        cin >> n>>k;
        pq.push(mp(n, mp(0, n - 1)));
        int res1 = 0, res2 = 0;
        for (int i = 0; i < k; i++) {
            pair<int, pair<int, int> >  rr = pq.top();
            pq.pop();
            int l = rr.second.first;
            int r = rr.second.second;
            int mid = (l + r) / 2;
            pq.push(mp(mid - l, mp(l, mid - 1)));
            pq.push(mp(r - mid, mp(mid + 1, r)));
            if (i == k - 1) {
                res1 = max(mid - l, r - mid);
                res2 = min(mid - l, r - mid);
            }
        }
        cout <<"Case #"<<c<<": "<<res1 <<" "<< res2 << endl;
    }
}

int main() {
    //readfiles;
#ifndef ONLINE_JUDGE

    //  double begin = clock();
#endif
    solve();
    return 0;
#ifndef ONLINE_JUDGE
    //  printf("%.4f", (clock() - begin) / CLOCKS_PER_SEC);
#endif
}
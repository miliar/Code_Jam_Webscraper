#include <iostream>
#include <string.h>
#include <map>
using namespace std;

int t;

const int maxn = 1000001;
int mark[maxn];
int n, k;
int tot = 0;

struct pos {
    int sr, sl, s, maxs, mins;
}a[maxn];

void putall (int l, int r) {
    if (l > r) return;
    
    int mid = (l+r)/2;
    
    pos ans;
    
    ans.s = mid;
    ans.sl = mid - l;
    ans.sr = r - mid;
    ans.maxs = max (ans.sl, ans.sr);
    ans.mins = min (ans.sl, ans.sr);
    a[tot] =  ans;
    tot++;
    putall (l, mid-1);
    putall (mid + 1, r);
    
}

bool cmp(pos x, pos y) {
    if (x.mins != y.mins)
        return x.mins > y.mins;
    if (x.maxs != y.maxs)
        return x.maxs > y.maxs;
    return x.s < y.s;
}

void solve () {
    cin >> n >> k;
    //memset (mark, 0, sizeof(mark));
    tot = 0;
    putall(1, n);
    sort(a, a+tot, cmp);
    cout << a[k-1].maxs << " " << a[k-1].mins << endl;
}

int main () {
    cin >> t;
    int tmp  = 1;
    while (t--) {
        cout << "Case #" << tmp << ": ";
        solve();
        tmp ++;
    }
    
}
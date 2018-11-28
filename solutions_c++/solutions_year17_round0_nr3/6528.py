#include <iostream>
#include <algorithm>
using namespace std;

const int N = 1000001;
bool f[N];

void put(bool *f, const int n, int &resl, int &resr)
{
    int p = -1;
    resl = -1;
    resr = -1;
    for (int i=1; i <= n; ++i) {
        if (f[i]) continue;
        int l = 0;
        int r = 0;
        for (int j=i-1; f[j]==false; --j) ++l;
        for (int j=i+1; f[j]==false; ++j) ++r;
        if (min(resl, resr) < min(l,r))
        {
            resl = l;
            resr = r;
            p = i;
        }
        else if (
            min(resl, resr) == min(l,r) &&
            max(resl, resr) < max(l, r)
        ){
            resl = l;
            resr = r;
            p = i;
        }
    }
    f[p] = true;
}

void solve(const int n, const int k)
{
    fill(f, f+n+2, false);
    f[0] = f[n+1] = true;
    int maxLR=0, minLR=n;
    for (int j=0; j < k; ++j) {
        int l, r;
        put(f, n, l, r);
        if (j==k-1) {
            maxLR = max(maxLR, max(l, r));
            minLR = min(minLR, min(l, r));
        }
    }
    cout << maxLR << " " << minLR;
}

int main()
{
    int T;
    cin >> T;
    for (int ci=0; ci < T; ++ci) {
        int n, k;
        cin >> n >> k;
        cout << "Case #" << ci+1 << ": ";
        solve(n,k);
        cout << endl;
    }
}

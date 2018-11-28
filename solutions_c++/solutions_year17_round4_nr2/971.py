#include <bits/stdc++.h>

using namespace std;

vector <int> A[1005];
int n, m, c, a[1005], b[1005], res1, res2;
bool F[1005];

void tinh(int n) {
    int ans1 = n, ans2 = 0;
    for (int i = 0; i < n; ++i)
        if (a[i]==1 && b[i]==1) ans1++;
    for (int i = 0; i < n; ++i)
        if (a[i]==b[i] && a[i] != 1)
            ans2++;
    if (res1 > ans1 || (res1==ans1 && res2 > ans2)) {
        res1 = ans1;
        res2 = ans2;
    }
}

void xoay(int L, int R) {
    int tmp = b[R];
    for (int i = R; i > L; --i)
        b[i] = b[i-1];
    b[L] = tmp;
}

void solve() {
    memset(F, 0, sizeof F);
    if (A[1].size() < A[2].size()) swap(A[1],A[2]);
    while (A[2].size() < A[1].size()) A[2].push_back(0);
    sort(A[1].begin(),A[1].end());
    sort(A[2].begin(),A[2].end());
    int i = 0, n = A[1].size(), m = A[2].size();
    while (i < m && A[2][i]==0) {
        a[i] = A[1][i];
        b[i] = A[2][i];
        ++i;
    }
    for (int j = i; j < n; ++j) {
        a[j] = A[1][j];
        b[j] = A[2][j];
    }
    res1 = 1000000000, res2 = 1000000000;
    for (int k = 0; k < n*2; ++k) {
        tinh(n);
        //xoay(i,n-1);
        xoay(0,n-1);
    }
    cout << res1 << " " << res2 << endl;
}

int main() {
	freopen("B-small-attempt3.in","r",stdin);
	freopen("output2.txt","w",stdout);
    int t; scanf("%d",&t); int te = t;
    while (t--) {
        scanf("%d%d%d",&n,&c,&m);
        for (int i = 1; i <= c; ++i)
            A[i].clear();
        for (int i = 1; i <= m; ++i) {
            int x, y; scanf("%d%d",&x,&y);
            A[y].push_back(x);
        }
        printf("Case #%d: ",te-t);
        if (c>2) {
            cout << "-10 -10" << endl;
            continue;
        }
        solve();
    }
	return 0;
}

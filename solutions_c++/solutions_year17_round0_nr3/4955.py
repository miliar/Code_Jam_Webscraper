#include <bits/stdc++.h>

#define F first
#define S second
#define prev azaza
#define mp make_pair
#define pb push_back

using namespace std;
typedef long long ll;
typedef long double ld;

const int max_n = 1000111, inf = 1000111222;

struct segm
{
    int left, len;
    segm (int left, int len) {
        this->left = left;
        this->len = len;
    }
};

bool operator< (const segm &a, const segm& b) {
    if (a.len < b.len) return true;
    if (a.len == b.len) {
        return a.left > b.left;
    }
    return false;
}

pair<int, int> solve(int n, int k) {
    priority_queue<segm> s;
    s.push(segm(0, n));
    for (int i = 0; i < k - 1; ++i) {
        segm seg = s.top();
        s.pop();
        if (seg.len % 2 == 1) {
            s.push(segm(seg.left, seg.len / 2));
            s.push(segm(seg.left + seg.len / 2 + 1, seg.len / 2));
        } else {
            s.push(segm(seg.left, seg.len / 2 - 1));
            s.push(segm(seg.left + seg.len / 2, seg.len / 2));
        }
    }
    segm seg = s.top();
    return mp(seg.len / 2, (seg.len - 1) / 2);
}

int main()
{
    //freopen("C-small-1-attempt0.in", "r", stdin);
    //freopen("C-small-1-attempt0.out", "w", stdout);
    ifstream fin("C-small-2-attempt0.in");
    ofstream fout("C-small-2-attempt0.out");
    int T, n, k;
    fin >> T;
    T = 100;
    for (int I = 1; I <= T; ++I) {
        cout << I << endl;
        fin >> n >> k;
        pair<int, int> ans = solve(n, k);
        fout << "Case #" << I << ": " << ans.F << ' ' << ans.S << endl;
    }
    return 0;
}



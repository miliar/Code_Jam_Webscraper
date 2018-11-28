#include <bits/stdc++.h>
using namespace std;


struct node{
    int l, r;
    node(){}
    node(int l_, int r_):l(l_), r(r_){};
    const bool operator <(const node &A) const{
        if (r - l != A.r - A.l) return r - l < A.r - A.l;
        return l > A.l;
    }
};


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int CAS;
    cin >> CAS;
    for (int cas = 1; cas <= CAS; cas++) {

        priority_queue<node> que;
        //set<pair<int, int>> deleted;
        int n, k;
        cin >> n >> k;
        cerr << cas << " " << n << " " << k << endl;
        que.push(node(0, n + 1));
        int len = 0;
        while (k--) {
            node x = que.top(); que.pop();
            if (x.r == x.l) continue;
            //if (deleted.find(make_pair(x.l, x.r)) != deleted.end()) continue;
            //deleted.insert(make_pair(x.l, x.r));
            que.push(node(x.l, x.l + (x.r - x.l) / 2));
            que.push(node(x.l + (x.r - x.l) / 2, x.r));
            len = x.r - x.l - 1;
        }
        printf("Case #%d: %d %d\n", cas, len / 2, (len - 1) / 2);
    }
}

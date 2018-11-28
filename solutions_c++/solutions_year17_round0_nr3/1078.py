#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair <ll, ll> pll;
const ll MAX1 = 1e3;
const ll MAX2 = 1e6;
int test;
ll n, k;

pll solve1(ll n, ll k){
    static bool fr[MAX1 + 1];
    static int pref[MAX1 + 2], suf[MAX1 + 2];
    pref[0] = 0, suf[n + 1] = n + 1;
    memset(fr + 1, false, n);

    struct Node{
        ll idx, ls, rs;
        Node() {}
        Node(const int& idx, const int& ls, const int& rs) : idx(idx), ls(ls), rs(rs) {}
        bool operator > (const Node& other) const{
            if (min(ls, rs) != min(other.ls, other.rs))
                return min(ls, rs) > min(other.ls, other.rs);
            if (max(ls, rs) != max(other.ls, other.rs))
                return max(ls, rs) > max(other.ls, other.rs);
            return idx < other.idx;
        }
    };

    Node res;
    while (k--){
        for (int i = 1; i <= n; ++i)
            pref[i] = (fr[i] ? i : pref[i - 1]);
        for (int i = n; i >= 1; --i)
            suf[i] = (fr[i] ? i : suf[i + 1]);

        res = Node(0, 0, 0);
        for (int i = 1; i <= n; ++i)
        if (!fr[i]){
            Node raw(i, i - pref[i] - 1, suf[i] - i - 1);
            if (res.idx == 0 || raw > res)
                res = raw;
        }
        fr[res.idx] = true;
    }

    return pll(max(res.ls, res.rs), min(res.ls, res.rs));
}

pll solve2(ll n, ll k){
    struct cmp{
        bool operator () (const pll& a, const pll& b){
            if (a.second != b.second)
                return a.second < b.second;
            return a.first > b.first;
        }
    };

    priority_queue <pll, vector <pll>, cmp> heap;
    heap.push(pll(1, n));
    pll node;
    ll len;
    while (k--){
        node = heap.top();
        heap.pop();
        len = node.second - 1;
        if ((len >> 1) > 0)
            heap.push(pll(node.first, len >> 1));
        if (((len + 1) >> 1) > 0)
            heap.push(pll(node.first + (len >> 1) + 1, (len + 1) >> 1));
    }
    return pll((len + 1) >> 1, len >> 1);
}

pll solve3(ll n, ll k){
    map <ll, ll> mp({pll(n, 1)});
    pll node;
    ll len;
    while (k > (node = *mp.rbegin()).second){
        k -= node.second;
		mp.erase(node.first);
		len = node.first - 1;
		if ((len >> 1) > 0)
			mp[len >> 1] += node.second;
		if (((len + 1) >> 1) > 0)
			mp[(len + 1) >> 1] += node.second;
    }
    len = node.first - 1;
    return pll((len + 1) >> 1, len >> 1);
}

int main(){
    //freopen("in.txt", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &test);
    pll res;
    for (int tt = 1; tt <= test; ++tt){
        scanf("%lld %lld", &n, &k);
        if (n <= MAX1)
            res = solve1(n, k);
        else
        if (n <= MAX2)
            res = solve2(n, k);
        else
            res = solve3(n, k);

        printf("Case #%d: %lld %lld\n", tt, res.first, res.second);
    }
    return 0;
}

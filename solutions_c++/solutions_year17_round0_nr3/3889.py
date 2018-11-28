#include <bits/stdc++.h>

using namespace std;

#ifndef ONLINE_JUDGE
#define db(...) printf(__VA_ARGS__);
#else
#define db(...)
#endif

#define mp(x,y) make_pair(x,y)
#define For(i,n) for(int i = 0; i<n; ++i)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vl;

void print(vector<bool>& zach) {
    for(bool z: zach) {
        db("%c", z?'1':'0');
    }
    db("\n");
}

// max, min
pii vyries(int n, int k) {
    vector<bool> zach(n+2, false);
    zach[0] = true; zach[n+1] = true;
    //print(zach);

    priority_queue<pii> pq;
    pq.push({n+1, -0});
    int last = -1;
    For(clovek, k) {
        pii usek = pq.top();
        pq.pop();
        int dlzka = usek.first, left = -usek.second;
        int right = left + dlzka;
        int mid = (left + right) / 2;
        zach[mid] = true;
        pq.push({mid-left, -left});
        pq.push({right-mid, -mid});
        //print(zach);
        last = mid;
    }
    int lava = last-1;
    while (!zach[lava]) lava--;
    int prava = last + 1;
    while (!zach[prava]) prava++;
    int ls = (last - lava - 1);
    int rs = (prava - last - 1);

    return {max(ls, rs), min(ls, rs)};
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t<=T; ++t) {
        int n,k;
        cin >> n >> k;
        pii res = vyries(n, k);
        cout<<"Case #"<<t<<": "<<res.first<<" "<<res.second<<endl;
    }
    return 0;
}

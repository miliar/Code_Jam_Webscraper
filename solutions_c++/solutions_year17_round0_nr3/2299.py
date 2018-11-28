#include<cstdio>
#include<cstring>
#include<algorithm>
#include<unordered_map>
using namespace std;

typedef long long LL;

unordered_map<LL, LL> cnt;
long long n,K;

inline pair<LL, LL> meiosis(long long x) {
    return {x >> 1, x - 1 >> 1};
}

pair<LL, LL> iterate(long long K) {
    vector<pair<LL, LL>> pairs;
    for (auto p : cnt) {
        pairs.push_back(p);
    }
    cnt.clear();
    sort(pairs.rbegin(), pairs.rend());
    for (auto p : pairs) {
        if (p.second >= K) return meiosis(p.first);
        K -= p.second;
        pair<LL,LL> children = meiosis(p.first);
        cnt[children.first] += p.second;
        cnt[children.second] += p.second;
    }
    return iterate(K);
}

int main() {
    freopen("stalls.in","r",stdin);
    freopen("stalls.out", "w",stdout);
    int c,c2;
    int tests;
    scanf("%d",&tests);
    for (int test=1;tests--;test++) {
        scanf("%lld%lld",&n,&K);
        cnt.clear();
        cnt[n] = 1;
        pair<LL, LL> ret = iterate(K);
        printf("Case #%d: %lld %lld\n",test,ret.first, ret.second);
    }
    
    return 0;
}

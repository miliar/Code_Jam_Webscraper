#include <cstdio>
#include <iostream>
#include <cassert>
#include <vector>
#include <tuple>

using namespace std;

typedef long long int int64;

tuple<int64, int64> split(int64 x) {
    int64 s = (x - 1ll) / 2ll;
    int64 y = min(s, x - 1 - s);
    int64 z = max(s, x - 1 - s);
    return make_tuple(y, z);
}

tuple<int64, int64> solve(int64 N, int64 K) {
    vector< tuple<int64, int64, int64> > v;
    v.push_back(make_tuple(N, 1ll, 1ll));    
    K -= 1;
    while (K > 0) {
        int64 R = 0;
        for (int i = int(v.size() - 1); i >= 0; i--) {            
            int64 d = min(K, get<2>(v[i]));
            K -= d;
            get<2>(v[i]) -= d;
            R += get<2>(v[i]);
        }                    
        if (K == 0 && R > 0) {
            break;
        }
        vector<tuple<int64, int64, int64> > w;
        for (int i = 0; i < int(v.size()); i++) {
            int64 y, z;
            tie(y, z) = split(get<0>(v[i]));
            w.push_back(make_tuple(y, get<1>(v[i]), get<1>(v[i])));
            w.push_back(make_tuple(z, get<1>(v[i]), get<1>(v[i])));
        }
        v.clear();
        v.push_back(w[0]);
        for (int i = 1; i < int(w.size()); i++) {
            assert(get<0>(w[i]) >= get<0>(v.back()));
            if (get<0>(w[i]) == get<0>(v.back())) {
                get<1>(v.back()) += get<1>(w[i]);
                get<2>(v.back()) += get<2>(w[i]);
            } else {                
                v.push_back(w[i]);
            }
        }
        assert(v.size() <= 2);
    }
    int p;
    for (p = int(v.size()) - 1; get<2>(v[p]) == 0; p--);    
        
    return split(get<0>(v[p]));
};

int main() {
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        int64 N, K;        
        scanf("%lld %lld", &N, &K);
        int64 L, R;
        tie(L, R) = solve(N, K);
        printf("Case #%d: %lld %lld\n", test + 1, R, L);
    }
    
};

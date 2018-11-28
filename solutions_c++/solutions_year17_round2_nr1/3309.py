#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <set>

typedef long long ll;

using namespace std;

ll T, D, N;

struct horse {
    ll start;
    ll speed;

    friend bool operator<(const horse &l, const horse &r){
        return l.start < r.start;
    }

    long double remain_t() {
        return (long double)(D-start) / speed;
    }

};

set<horse> horses;

int main() {
    cin >> T;
    for (int i=0; i<T; ++i) {
        horses.clear();
        cin >> D >> N;
        for (int j=0; j<N; ++j) {
            ll start, speed;
            cin >> start >> speed;
            horses.insert(horse{start, speed});
        }
        long double longest_remain = 0;
        for (auto horse: horses) {
            longest_remain = max(longest_remain, horse.remain_t());
        }
        printf("Case #%d: %.6Lf\n", i+1, D / longest_remain);

    }

    return 0;
}

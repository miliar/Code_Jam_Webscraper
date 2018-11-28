#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <thread>
#include <unistd.h>

using namespace std;


#define ll long long
#define ull unsigned long long
#define uint unsigned int
//long long
#define dot(x,y) ((ll)x[0]*y[0]+ (ll)x[1]*y[1])



int main() {
    int T;
    cin >> T;

    for (int testcase = 1; testcase <= T; testcase++) {
        ll N, K;
        cin >> N >> K;

        map<ll, ll> gaps;
        gaps[N] = 1;

        ll size, cnt;
        while (K > 0) {
            auto last = *(--gaps.end());
            size = last.first;
            cnt = last.second;
            gaps.erase(--gaps.end());
            K -= cnt;
            gaps[(size - 1) / 2] += cnt;
            gaps[size / 2] += cnt;
            //printf("K%lld size%lld %lld %lld \n", K, size, (size - 1) / 2, (size ) / 2);
        }

        printf("Case #%d: %lld %lld\n", testcase, size / 2, (size - 1) / 2);
    }
    return 0;
}

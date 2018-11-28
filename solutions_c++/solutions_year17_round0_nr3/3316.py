#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#include <utility>
#include <algorithm>

using namespace std;

int main() {
    int T;

    cin >> T;
    for(int cs=1;cs<=T;cs++) {
        long long N,K;

        cin >> N >> K;
        map<long long, long long, greater<long long>> m;
        m[N] = 1;

        long long range = 0;
        long long cnt = 0;
        for(;;) {
            long long cc = m.begin()->second;
            range = m.begin()->first;

            if(cnt + m.begin()->second >= K) {
                break;
            }

            m.erase(m.begin());

            if(range%2 == 0) {
                m[range/2-1] += cc;
                m[range/2] += cc;
            } else {
                m[range/2] += cc*2;
            }

            cnt += cc;
        }

        long long a;
        long long b;
        a = b = range/2;
        if(range%2 == 0) {
            b = range/2 - 1;
        }

        printf("Case #%d: %lld %lld\n", cs, a,b);
    }

    return 0;
}

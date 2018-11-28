#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;

ll one[19];
int main()
{
    for (int i = 1; i < 19; ++i) {
        one[i] = one[i - 1] * 10 + 1;
    }

    int T; cin>>T;
    for (int TT = 1; TT <= T; ++TT) {
        printf("Case #%d: ", TT);
        ll num; cin>>num;
        int ptr = 18;
        ll ans = 0;
        while(ptr) {
            while (ans + one[ptr] <= num && ans % 10 != 9) {
                ans += one[ptr];
            }
            ptr --;
        }
        printf("%lld\n", ans);
    }
    return 0;
}
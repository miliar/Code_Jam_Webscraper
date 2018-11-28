#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long ll;
int main()
{
    int T; cin>>T;
    for (int TT = 1; TT <= T; ++TT) {
        printf("Case #%d: ", TT);
        ll n, k, cnt = 0, itre = 1;
        cin>>n>>k;
        while (k > itre) {
            k -= itre;
            cnt += itre;
            itre <<= 1;
        }
        ll rem = (n - cnt) % (cnt + 1);
        ll num = (n - cnt) / (cnt + 1);
        if(k <= rem) num += 1;
        printf("%lld %lld\n", num / 2, (num - 1) / 2);
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
using namespace std;

long long n, k;
set<pair<long long, long long> > m;

void insert_to_m(long long len, long long cnt) {
    if (len == 0)
        return;
    set<pair<long long, long long> >::iterator cur = m.lower_bound(make_pair(len, 0));
    if (cur->first == len) {
        cnt += cur->second;
        m.erase(cur);
    }

    m.insert(make_pair(len, cnt));
}

void solve()
{
    scanf("%lld %lld", &n, &k);
    m.clear();
    insert_to_m(n, 1);
    while (k) {
        set<pair<long long, long long> >::iterator cur = m.end();
        cur--;
        long long len = cur->first - 1;
        long long len1 = len / 2;
        long long len2 = len - len1;
        long long cnt = cur->second;
        m.erase(cur);
        if (k > cnt) {
            k -= cnt;
            insert_to_m(len1, cnt);
            insert_to_m(len2, cnt);
        }
        else {
            printf("%lld %lld", len2, len1);
            return;
        }
    }
}

int main() {
    int t;
    scanf("%d\n", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}

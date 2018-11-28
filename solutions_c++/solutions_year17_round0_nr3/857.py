#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int N = 1010;

ll n, k;
map<ll, ll> segments;

void _main() {
    cin >> n >> k;
    segments.clear();
    segments[n] = 1;
    while(k) {
        map<ll, ll>::reverse_iterator rit = segments.rbegin();
        ll length = rit->first, cnt = rit->second;
        ll left_split = (length - 1) / 2, right_split = length / 2;
        if (cnt >= k) {
            cout << right_split << ' ' << left_split << endl;
            break;
        }
        k -= cnt;
        segments[left_split] += cnt;
        segments[right_split] += cnt;
        segments.erase(segments.find(length));
    }
}
int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, cas = 0;
    for (scanf("%d", &t); t--; ) {
        printf("Case #%d: ", ++cas);
        _main();
    }
    return 0;
}

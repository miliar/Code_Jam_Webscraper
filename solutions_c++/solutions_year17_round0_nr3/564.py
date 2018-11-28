#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <cmath>
#include <string>

using namespace std;

#define ll long long
ll N;
ll K;

typedef pair<ll, ll> Pd;

int main() {
    int T;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        cin>>N>>K;

        Pd start = {(N-1)/2, (N)/2};

        map<Pd, ll> cnt;
        cnt[start]++;

        Pd ans;

        while (K > 0) {
            auto itr = cnt.end();
            --itr;
            Pd cur = itr->first;
            ll val = itr->second;
            cnt.erase(itr);

            Pd next1 = {(cur.first-1)/2, cur.first/2};
            Pd next2 = {(cur.second-1)/2, cur.second/2};

            if (val >= K) {
                ans = cur;
                break;
                
            } else {
                K -= val;
                cnt[next1] += val;
                cnt[next2] += val;
            }

        }

        printf("Case #%d: %lld %lld\n", t, ans.second, ans.first);
    }
}


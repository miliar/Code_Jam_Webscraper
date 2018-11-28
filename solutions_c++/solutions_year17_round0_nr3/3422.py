#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<queue>
#include<map>

using namespace std;

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++)
    {
        long long ans = 0LL, N, K;
        scanf("%lld%lld", &N, &K);
        priority_queue<long long> que;
        map<long long, long long> mp;
        mp.insert(make_pair(N, 1LL));
        que.push(N);
        long long cur = 0LL;
        while (true)
        {
            ans = que.top(); que.pop();
//            cout<<ans<<endl;
            long long num = mp[ans];
            cur += num;
            if (cur >= K) break;
            long long s1 = (ans >> 1);
            if (mp.find(s1) == mp.end()) que.push(s1);
            mp[s1] += num;
            long long s2 = ((ans - 1LL) >> 1);
            if (mp.find(s2) == mp.end()) que.push(s2);
            mp[s2] += num;
//            cout<<s1<<" "<<s2<<endl;
            mp.erase(mp.find(ans));
        }
        printf("Case #%d: %lld %lld\n", cas, ans >> 1, (ans - 1LL) >> 1);
    }
    return 0;
}

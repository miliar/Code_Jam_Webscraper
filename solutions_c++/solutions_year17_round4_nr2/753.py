#include <bits/stdc++.h>
using namespace std;
multiset <int> vec[1005];
int t[1005][2];
map <pair<int, int>, int> mp;
int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int c = 1, cas;
    scanf("%d", &cas);
    while(cas--)
    {
        vec[1].clear();
        vec[2].clear();
        int N, C, M;
        scanf("%d %d %d", &N, &C, &M);
        for(int i = 0; i < M; i++)
        {
            scanf("%d %d", &t[i][0], &t[i][1]);
            vec[t[i][1]].insert(t[i][0]);
        }
        int ans = 0, fuck = 0;
        multiset <int> ::iterator now = vec[2].begin();
        while(now != vec[2].end())
        {
            multiset <int> ::iterator it = upper_bound(vec[1].begin(), vec[1].end(), *vec[2].begin());
            if(it != vec[1].end())
            {
                vec[1].erase(it);
                vec[2].erase(now++);
                ans++;
            }
            else
            {
                now++;
            }
        }
        now = vec[1].begin();
        while(now != vec[1].end())
        {
            multiset <int> ::iterator it = upper_bound(vec[2].begin(), vec[2].end(), *vec[1].begin());
            if(it != vec[2].end())
            {
                vec[2].erase(it);
                vec[1].erase(now++);
                ans++;
            }
            else
            {
                now++;
            }
        }
        while((!vec[1].empty()) && (!vec[2].empty()))
        {
            if(*vec[1].begin() == 1 && *vec[2].begin() == 1)
            {
                ans++;
                vec[1].erase(vec[1].begin());
            }
            else
            {
                ans++;
                vec[1].erase(vec[1].begin());
                vec[2].erase(vec[2].begin());
                fuck++;
            }
        }
        ans += vec[1].size();
        ans += vec[2].size();
        printf("Case #%d: %d %d\n", c++, ans, fuck);
//        int P = 0;
//        for(int i = 0; i < M; i++)
//        {
//            int seat, id;
//            scanf("%d %d", &seat, &id);
//            vec[id].insert(seat);
//            P = max(P, id);
//        }
//        for(int i = 0; i < P; i++)
//        {
//            if(vec[i].size() != 0)
//            {
//                mp.insert(make_pair(make_pair(*vec[i].rbegin(), vec[i].size()), i));
//            }
//        }
//        int cnt = M;
//        while(cnt != 0)
//        {
//            map <pair<int, int>, int>::reverse_iterator it = mp.rbegin();
//            while(it != mp.rend())
//            {
//
//                it++;
//            }
//        }
    }
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

int tests , T , Ac , Aj , a , b ,  i , add , moves , M , val , u , sum[2] , p[2] , have[2];
priority_queue < int > must[2];
vector < pair < pair < int , int > , int > > events;

int main()
{

freopen("input" , "r" , stdin);
freopen("output" , "w" , stdout);

scanf("%d" , &tests);
for (T = 1 ; T <= tests ; ++T)
{
    scanf("%d" , &Ac);
    scanf("%d" , &Aj);

    events.clear();

    for (i = 1 ; i <= Ac ; ++i)
    {
        scanf("%d" , &a);
        scanf("%d" , &b);
        events.push_back(make_pair(make_pair(a , b) , 0));
    }

    for (i = 1 ; i <= Aj ; ++i)
    {
        scanf("%d" , &a);
        scanf("%d" , &b);
        events.push_back(make_pair(make_pair(a , b) , 1));
    }

    sort(events.begin() , events.end());
    M = events.size();

    p[0] = p[1] = 0;
    while (must[0].size()) must[0].pop();
    while (must[1].size()) must[1].pop();
    sum[0] = sum[1] = 0;
    add = moves = 0;

    for (i = 0 ; i < M ; ++i)
    {
        p[events[i].second] += events[i].first.second - events[i].first.first;

        if (events[i].second == events[(i + 1) % M].second)
        {
            if (i < M - 1) val = events[(i + 1) % M].first.first - events[i].first.second;
            else val = 24 * 60 + events[(i + 1) % M].first.first - events[i].first.second;

            if (val) must[events[i].second].push(val);
            sum[events[i].second] += val;
        }
        else
        {
            if (i < M - 1) val = events[(i + 1) % M].first.first - events[i].first.second;
            else val = 24 * 60 + events[(i + 1) % M].first.first - events[i].first.second;

            add += val;
            moves++;
        }
    }

    while (1)
    {
        have[0] = p[0] + sum[0];
        have[1] = p[1] + sum[1];
        if (have[0] >= have[1])
        {
            if (have[0] - have[1] <= add) break;
            u = must[0].top();
            must[0].pop();
            sum[0] -= u;
            add += u;
            moves += 2;
        }
        else
        {
            if (have[1] - have[0] <= add) break;
            u = must[1].top();
            must[1].pop();
            sum[1] -= u;
            add += u;
            moves += 2;
        }
    }

    printf("Case #%d: %d\n" , T , moves);
}

return 0;
}

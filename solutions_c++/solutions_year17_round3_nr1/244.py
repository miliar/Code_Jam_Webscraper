#include<bits/stdc++.h>

using namespace std;

int N, K;
pair < int, int > pancake[1009];
long double PI = acos (-1.0), ans, val[1009];
multiset < long long > S;

int main ()
{
freopen ("input", "r", stdin);
//freopen ("output", "w", stdout);
ofstream g("output");

int Tests;
scanf ("%d\n", &Tests);
for (int test_id = 1; test_id <= Tests; test_id ++)
{
    //printf ("Case #%d: ", test_id);
    g << "Case #" << test_id << ": ";
    scanf ("%d %d", &N, &K);
    for (int i=1; i<=N; i++)
        scanf ("%d %d", &pancake[i].first, &pancake[i].second);
    sort (pancake + 1, pancake + N + 1), reverse (pancake + 1, pancake + N + 1);
    S.clear ();
    for (int i=N - K + 2; i<=N; i++)
        S.insert (2LL * pancake[i].first * pancake[i].second);
    for (int i=N - K + 1; i>=1; i--)
    {
        long long s = 2LL * pancake[i].first * pancake[i].second;
        int steps = K - 1;
        for (auto j = S.rbegin (); j != S.rend () && steps > 0; j++, steps --)
            s += (*j);
        long long curr = s + 1LL * pancake[i].first * pancake[i].first;
        if (i == N - K + 1 || curr > ans)
            ans = curr;
        ///
        S.insert (2LL * pancake[i].first * pancake[i].second);
    }
    long double ans2 = (long double) PI * ((long double) ans);
    g << setprecision (20) << ans2 << '\n';
}
return 0;
}

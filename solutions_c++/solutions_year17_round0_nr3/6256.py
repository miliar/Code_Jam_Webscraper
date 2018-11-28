#include<bits/stdc++.h>

using namespace std;

int N, K;

set < pair < pair < int, int >, int > > S2;
set < int > S;

pair < pair < int, int >, int > getDists (int st, int dr)
{
    int mij = (st + dr) >> 1;
    int a = mij - st - 1, b = dr - mij - 1;
    return {{-min (a, b), -max (a, b)}, mij};
}

int main ()
{
freopen ("input", "r", stdin);
freopen ("output", "w", stdout);

int Tests;
scanf ("%d\n", &Tests);
for (int test_id = 1; test_id <= Tests; test_id ++)
{
    printf ("Case #%d: ", test_id);
    scanf ("%d %d", &N, &K);
    S.clear (), S.insert (0), S.insert (N + 1);
    S2.clear (), S2.insert (getDists (0, N + 1));
    pair < int, int > lst;
    while (K --)
    {
//        for (auto it = S2.begin (); it != S2.end (); it ++)
  //          printf ("(%d, %d) %d\n", it->first.first, -it->first.second, it->second);
        auto curr = S2.begin ();
        lst = curr->first;
        int pos = curr->second;
        S2.erase (curr);
        auto it2 = S.lower_bound (pos);
        auto it1 = it2; it1 --;
        if ((*it1) + 1 != pos) S2.insert (getDists (*it1, pos));
        if (pos + 1 != (*it2)) S2.insert (getDists (pos, *it2));
        //printf ("%d %d %d\n", *it1, pos, *it2);
        //lst = {pos - (*it1) - 1, (*it2) - pos - 1};
        S.insert (pos);
    }
    printf ("%d %d\n", -lst.second, -lst.first);
}
return 0;
}

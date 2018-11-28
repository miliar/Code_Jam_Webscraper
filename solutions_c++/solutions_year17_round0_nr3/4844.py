# include <cstdio>
# include <queue>
# include <algorithm>

using namespace std;

priority_queue <pair <int, int>> pq;

int n, k;

void solve ()
{
    pair <int, int> crr;
    int idx, l, r;
    scanf ("%d%d", &n, &k);
    while (!pq.empty ())
        pq.pop ();
    pq.push ({n, -1});
    while (k --)
    {
        crr = pq.top ();
        pq.pop ();
        l = -crr.second;
        r = crr.first + l - 1;
        idx = (l + r) >> 1;
        pq.push ({idx - l, -l});
        pq.push ({r - idx, -(idx + 1)});
    }
    printf ("%d %d\n", max (idx - l, r - idx), min (idx - l, r - idx));
}

int main ()
{
    int t, idt;
    scanf ("%d", &t);
    for (idt = 1; idt <= t; idt ++)
    {
        printf ("Case #%d: ", idt);
        solve ();
    }
    return 0;
}

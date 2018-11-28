#include <bits/stdc++.h>

using namespace std;

#define mp make_pair

typedef pair <long long, long long> pii;
typedef pair<long long, pair <long long, long long>> ppii;
typedef long long ll;

int main () {
    int t, caso = 1;
    scanf ("%d", &t);
    while (t--) {
        ll n, k;
        pii result;
        scanf ("%lld %lld", &n, &k);
        priority_queue <ppii> q;
        q.push (mp (n+1, mp (0, n+1)));
        while (k--) {
            //printf ("k = %d\n", k);
            ll m, psf, pss;;
            ppii p = q.top ();
            q.pop ();
            psf = p.second.first;
            pss = p.second.second;
            m = (psf + pss) / 2;
            
            q.push (mp (m - psf, mp (psf, m)));
            q.push (mp (pss - m, mp (m, pss)));
            
            //printf ("m = %lld %lld %lld %lld\n", m, psf, pss, p.first);
            result = mp (max (m - psf, pss - m)-1,
                min (m - psf, pss - m)-1);
            //printf ("oi %d\n", k);
        }
        printf ("Case #%d: %lld %lld\n", caso++, result.first, result.second);
    }
    return 0;
}

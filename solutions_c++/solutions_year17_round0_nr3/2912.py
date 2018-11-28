#include <bits/stdc++.h>
using namespace std;

void bruteforce()
{
    int a, k; cin >> a >> k;
    multiset<int> ranges;
    ranges.insert(a);
    int lastMin;
    int lastMax;
    for(int i = 0; i < k; ++i)
    {
        auto last = --ranges.end();
        int r = *last - 1;
        ranges.erase(last);
        lastMin = r/2;
        lastMax = (r + 1)/2;
        ranges.insert(lastMin);
        ranges.insert(lastMax);
    }
    cout << lastMax << " " << lastMin;
}

void solve()
{
    int64_t a, k; cin >> a >> k;
    int64_t b = a;
    int64_t na = 1, nb = 0;
    int64_t s = 1;
    //cout << endl;
    while(k > s)
    {
        a -= 1;
        b -= 1;
        if(a == b)
        {
            a /= 2;
            b -= a;
            na = nb = na + nb;
        }
        else
        {
            if(a % 2)   // 11 12
            {
                a /= 2;
                b /= 2;
                nb *= 2;
                nb += na;
            }
            else        // 12 13
            {
                a /= 2;
                b -= a;
                na *= 2;
                na += nb;
            }
        }
        // int64_t na1 = 0, nb1 = 0;
        // if(a % 2)
        // {
        //     na1 += na;
        //     nb1 += na;
        // }
        // else
        // {
        //     na1 += na*2;
        // }
        // if(b % 2)
        // {
        //     na1 += nb;
        //     nb1 += nb;
        // }
        // else
        // {
        //     nb1 += nb*2;
        // }
        // a /= 2;
        // b = (b + 1)/2;
        // na = na1;
        // nb = nb1;
        k -= s;
        s *= 2;
        //cout << k << "\t" << a << ": " << na << "\t" << b << ": " << nb << endl;
    }
    if(nb && k <= nb) swap(a, b);
    cout << a/2 << ' ' << (a - 1)/2;
    // 50 +1
    // 24 25 +2
    // 11 + 12*3 +4
    // 5*5 + 6*3 +8
    // 2*13 + 3*3 +16

    // 31 +1
    // 15 15 +2
    // 7 7 +4
    // 3 3 +8
    // 1 1
}

int main()
{
	int t; cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
        solve();
        //bruteforce();
		cout << endl;
	}
	return 0;
}

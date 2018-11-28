#include <bits/stdc++.h>
using namespace std;
#define fr first
#define sc second
#define mp make_pair
#define pI pair <int, int>
#define pb push_back
#define vI vector <int>
#define LL long long
int T, P;
LL n, k;
map <LL, LL> M;
int main()
{
    cin >> T;
    while (P ++, T --)
    {
        cin >> n >> k;
        M.clear();
        M[n] = 1;
        while (k)
        {
            map <LL, LL> :: iterator it = M.end();
            it --;
            LL a = it -> fr, b = it -> sc;
            LL a0 = (a - 1) / 2, a1 = a - 1 - a0;
            M.erase(it);
            if (b >= k)
            {
                cout << "Case #" << P << ": ";
                cout << max(a0, a1) << " " << min(a0, a1) << "\n";
                k = 0;
            }
            else
            {
                M[a0] += b;
                M[a1] += b;
                k -= b;
            }
        }
    }
}

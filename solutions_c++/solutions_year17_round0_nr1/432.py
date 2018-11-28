#include <bits/stdc++.h>


#define f(i, a, b) for(int i = a; i <= b; i++)
#define fd(i, a, b) for(int i = a; i >= b; i--)
#define fin ""
#define fou ""
#define mp make_pair
#define fi first
#define se second
#define pb push_back

using namespace std;


typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

int n, t, k;
string s;

int main()
{
    ios_base::sync_with_stdio(0);
    cin >> t;
    f(tt, 1, t)
    {
        cin >> s >> k;
        n = s.size();
        int res = 0;
        f(i, 0, n - k)
            if (s[i] == '-')
            {
                res++;
                f(j, i, i + k - 1)
                    if (s[j] == '+') s[j] = '-'; else s[j] = '+';
            }
        f(i, 0, n - 1)
            if (s[i] != '+') res = -1;
        cout << "Case #" << tt << ": ";
        if (res == -1) cout << "IMPOSSIBLE" << endl; else cout << res << endl;
    }
}

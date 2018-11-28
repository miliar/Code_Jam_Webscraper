#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define f first
#define sec second
#define fro for
#define itn int
#define pb push_back
#define pii pair<int,int>
#define pll pair<ll,ll>

vector <int > Vec;
int n, k, t;
int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        cin >> n >> k;
        Vec.clear();
        Vec.pb(n);
        for (int j = 0; j < n; j++)
        {
            if (Vec[j] % 2 == 1)
            {
                Vec.pb((Vec[j] - 1) / 2);
                Vec.pb((Vec[j] - 1) / 2);
            }
            else
            {
                Vec.pb((Vec[j] - 1) / 2);
                Vec.pb((Vec[j] - 1) / 2 + 1);
            }
        }
        sort(Vec.rbegin(), Vec.rend());
        cout << "Case #" << i << ": ";
        if ((Vec[k - 1] - 1) % 2 == 0)
        {
            cout << (Vec[k - 1] - 1) / 2 << " " << (Vec[k - 1] - 1) / 2 << endl;
        }
        else
        {
            cout << (Vec[k - 1] - 1) / 2 + 1 << " " << (Vec[k - 1] - 1) / 2 << endl;
        }

    }

    return 0;
}

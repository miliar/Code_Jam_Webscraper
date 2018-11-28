/// This code is a pure govnocode
#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = 50;

int isTidy(int x)
{
    int a = x % 10; x /= 10;
    int b = x % 10; x /= 10;
    int c = x % 10; x /= 10;
    int d = x % 10; x /= 10;

    return (d <= c) && (c <= b) && (b <= a);

}

int main()
{
    freopen("input_r.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int T;
    cin >> T;

    for (int _t = 1; _t <= T; _t++)
    {
        int N;
        cin >> N;

        int ans = 1;
        for (int i = 1; i <= N; i++)
        {
            if (isTidy(i))
            {
                ans = i;
            }
        }

        cout << "Case #" << _t << ": " << ans << endl;
    }

    return 0;
}

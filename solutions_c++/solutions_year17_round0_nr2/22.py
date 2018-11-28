#include <bits/stdc++.h>
using namespace std;
#define LL long long
int T, P;
LL n;
const int N = 20;
int lst[N], cnt;
LL C[N][N];
int main()
{
    cin >> T;
    while (P ++, T --)
    {
        cin >> n; cnt = 0;
        while (n) {lst[++ cnt] = n % 10; n /= 10;} lst[0] = 10;
        LL ans = 0;
        for (int i = cnt; i >= 1; )
        {
            int j = i;
            while (lst[j] == lst[j - 1]) j --;
            if (lst[j - 1] > lst[i]) i = j - 1;
            else
            {
                lst[i] --;
                while (-- i) lst[i] = 9;
            }
        }

        for (int i = cnt; i >= 1; -- i)
            ans = ans * 10 + lst[i];
        cout << "Case #" << P << ": " << ans << "\n";
    }
}

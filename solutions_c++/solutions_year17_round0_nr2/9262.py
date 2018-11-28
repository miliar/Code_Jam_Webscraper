#include <bits/stdc++.h>

using namespace std;

vector <int> a;

int main()
{
    int t;
    cin >> t;
    for (int k = 1; k <= t; k++)
    {
        a.clear();
        long long n,cop;
        cin >> n;
        cop = n;
        while (n > 0)
        {
            a.push_back(n % 10);
            n = n / 10;
        }
        reverse(a.rbegin(),a.rend());

        int l = -1;
        for (int i = 0; i < a.size() - 1; i++)
            if (a[i] > a[i + 1])
            {
                l = i;
                break;
            }
        if (l < 0)
            cout << "Case #" << k << ": " << cop << endl;
        else
        {
            while (l > 0 && a[l - 1] == a[l])
                l--;
            a[l]--;

            for (int i = l + 1; i < a.size(); i++)
                a[i] = 9;

            long long ans = 0;
            for (int i = 0; i < a.size(); i++)
                ans = ans * 10 + a[i];
            cout << "Case #" << k << ": " << ans << endl;
        }
    }
}

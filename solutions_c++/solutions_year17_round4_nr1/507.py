#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        int n, k;
        cin >> n >> k;

        vector<int> a(k);
        for (int i = 0; i < n; i++)
        {
            int x;
            cin >> x;
            a[x % k]++;
        }

        int m = a[0];

        if (k == 2)
        {
            m += (a[1] + 1) / 2;
        }
        else if (k == 3)
        {
            if (a[1] < a[2])
                swap(a[1], a[2]);

            m += a[2];
            a[1] -= a[2];
            m += (a[1] + 2) / 3;
        }
        else if (k == 4)
        {
            m += a[2] / 2;
            a[2] %= 2;

            if (a[1] < a[3])
                swap(a[1], a[3]);

            m += a[3];
            a[1] -= a[3];
            m += (a[1] + 2 * a[2] + 3) / 4;
        }

        cout << "Case #" << tt << ": " << m << endl;
    }

    return 0;
}

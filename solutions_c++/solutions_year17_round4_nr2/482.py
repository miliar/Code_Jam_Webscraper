#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        int n, m, k;
        cin >> n >> k >> m;

        vector<int> a(k);
        vector<int> b(n, 0);
        for (int i = 0; i < m; i++)
        {
            int x, y;
            cin >> x >> y;
            a[y - 1]++;
            b[x - 1]++;
        }

        int result = 0;
        for (int i = 0; i < k; i++)
            result = max(result, a[i]);

        for (int i = 0, s = 0; i < n; i++)
        {
            s += b[i];
            result = max(result, (s + i) / (i + 1));
        }

        int promo = 0;

        for (int i = 0; i < n; i++)
            promo += max(0, b[i] - result);

        cout << "Case #" << tt << ": " << result << " " << promo << endl;
    }

    return 0;
}

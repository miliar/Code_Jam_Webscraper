#include <bits/stdc++.h>

using namespace std;

bool b[1007];
int le[1007], ri[1007];

int main()
{
    ifstream cin("in.in");
    ofstream cout("out.txt");
    ios_base::sync_with_stdio(0);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        int n, k;
        cin >> n >> k;
        for (int i = 1; i <= n; i++)
            b[i] = 0, le[i] = 0, ri[i] = n + 1;

        for (int it = 0; it < k - 1; it++){
            int j = -1;
            for (int i = 1; i <= n; i++)
                if (!b[i] && (j == -1 || min(i - le[i], ri[i] - i) > min(j - le[j], ri[j] - j)  || min(i - le[i], ri[i] - i) == min(j - le[j], ri[j] - j) && max(i - le[i], ri[i] - i) > max(j - le[j], ri[j]  - j)))
                    j = i;
            b[j] = 1;
            for (int i = 1; i <= j; i++)
                ri[i] = min(ri[i], j);
            for (int i = j + 1; i <= n; i++)
                le[i] = max(le[i], j);
        }

        int j = -1;
        for (int i = 1; i <= n; i++)
            if (!b[i] && (j == -1 || min(i - le[i], ri[i] - i) > min(j - le[j], ri[j] - j)  || min(i - le[i], ri[i] - i) == min(j - le[j], ri[j] - j) && max(i - le[i], ri[i] - i) > max(j - le[j], ri[j]  - j)))
                j = i;
        cout << "Case #" << t << ": " << max(j - le[j], ri[j] - j) - 1 << ' ' << min(j - le[j], ri[j] - j) - 1 << '\n';
    }
    return 0;
}

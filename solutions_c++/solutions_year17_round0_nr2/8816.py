#include <bits/stdc++.h>
using namespace std;
string to_string(int n)
{
    stringstream ss;
    ss << n;
    string s = ss.str();
    return s;
}
int main()
{
    long long n, cn, ci, t, tidy;
    cin >> t;
    for (long long ii = 1; ii <= t; ii++)
    {
        cin >> n;
        for (long long i = n; i >= 1; i--)
        {
            ci = i;
            string ccc = to_string(ci);
            cn = 0;
            for (long long iii = 0; iii < ccc.size() - 1; iii++)
            {
                if (ccc[iii] - '0' <= ccc[iii + 1] - '0')cn++;
                else break;
            }

            if (cn == ccc.size() - 1)
            {
                tidy = i;
                break;
            }

        }
        cout << "Case #" << ii << ": " << tidy << endl;
    }

    return 0;
}

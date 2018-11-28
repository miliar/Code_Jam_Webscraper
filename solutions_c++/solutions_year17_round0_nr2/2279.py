#include <bits/stdc++.h>
using namespace std;

using vi = vector<int>;

void solve(int t)
{
    string s; cin >> s;

    int n = s.size();

    vi v(10, INT_MAX);

    for(int i = 0; i < n - 1; i++)
    {
        char cur = s[i];
        char next = s[i + 1];

        auto& first_i = v[cur - '0'];
        first_i = min(first_i, i);

        if(cur > next)
        {
            if(cur == '1')
            {
                s = string(n - 1, '9');
                break;
            }

            s[first_i]--;

            for(int j = first_i + 1; j < n; j++) s[j] = '9';
            break;
        }
    }

    cout << "Case #" << t << ": " << s << '\n';
}

int main()
{
    ios_base::sync_with_stdio(0);

    int t; cin >> t;

    for(int i = 1; i <= t; i++) solve(i);

    return 0;
}

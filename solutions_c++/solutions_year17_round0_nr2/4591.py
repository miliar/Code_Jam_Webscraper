#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl
#define pb push_back
using namespace std;
typedef long long ll;

const int MAXN = 100005;

void cans(int test, int ans)
{
    cout << "Case #" << test << ": " << ans << endl;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        string s;
        cin >> s;
        s = '0' + s;
        for (int i = 0; i + 1 < s.length(); i++)
        {
            if (s[i] > s[i+1])
            {
                int j = i-1;
                while (s[j] == s[i]) j--;
                s[j+1]--;
                for (int k = j+2; k < s.length(); k++)
                {
                    s[k] = '9';
                }
                break;
            }
        }

        cout << "Case #" << tt << ": ";
        int j = 0;
        while (s[j] == '0') j++;
        while (j < s.length())
        {
            cout << s[j]; j++;
        }
        cout << endl;
    }

    return 0;
}


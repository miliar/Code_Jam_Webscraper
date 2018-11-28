#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define TASK "payment"
#define X first
#define Y second
#define mp make_pair
#define inb push_back
#define eps 1e-9

int main()
{
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	//freopen("poker.in", "r", stdin);
    //freopen("poker.out", "w", stdout);
    int t;
    cin >> t;
    string s;
    int k;
    int p = 0;
    while(t--)
    {
        cin >> s >> k;
        int ans = 0;
        int i = 0;
        while(i < s.size() && s.size() - i >= k)
        {
            while(i < s.size() && s[i] == '+') ++i;
            if (s.size() - i < k) break;
            for(int j = i; j < i + k; ++j)
                if (s[j] == '-') s[j] = '+';
                else s[j] = '-';
            ++ans;
        }
        cout << "Case #" << p + 1 << ": ";
        bool f = 0;
        for(int i = 0; i < s.size(); ++i) if (s[i] == '-') f = 1;
        if (f) cout << "IMPOSSIBLE\n";
        else cout << ans << '\n';
        ++p;
    }
}

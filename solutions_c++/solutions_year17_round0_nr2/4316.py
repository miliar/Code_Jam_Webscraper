#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define f first
#define sec second
#define fro for
#define itn int
#define pb push_back
#define pii pair<int,int>
#define pll pair<ll,ll>

int n, k, ans;
string s, s1;

string solve(string s)
{
    int k;
    for (int i = 0; i < s.size() - 1; i++)
    {
        if (s[i] < s[i + 1]) k = i + 1;
        else if (s[i] > s[i + 1])
        {
            s[k]--;
            for (int j = k + 1; j < s.size(); j++) s[j] = '9';
        }
    }
    while (s[0] == '0') s.erase(s.begin());
    return s;
}


int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> s;
        cout << "Case #" << i << ": " << solve(s) << endl;
    }

    return 0;
}

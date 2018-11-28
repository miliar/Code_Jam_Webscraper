#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <string>
#include <cstring>
#include <complex>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair

string solve()
{
    string s;
    cin >> s;
    int p = 0;
    while(p < (int)s.length() - 1 && s[p] <= s[p + 1]) p++;
    if (p == (int)s.length() - 1) return s;
    while(p > 0 && s[p] == s[p - 1]) p--;
    s[p]--;
    for (int i = p + 1; i < (int)s.length(); i++)
        s[i] = '9';
    if (p == 0 && s[0] == '0')
        return s.substr(1, (int)s.length());
    else
        return s;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cout << "Case #" << i + 1 << ": " << solve() << endl;
    }

    return 0;
}

#include <bits/stdc++.h>

using namespace std;

#define FROM_FILE freopen("input.txt", "r", stdin)
#define TO_FILE freopen("output.txt", "w", stdout)

#define ull unsigned long long
#define ll long long

#define pb push_back
#define mp make_pair

#define PI 3.1415926535
#define INF 1e9
#define EPS 1e-6
#define prv(v) for (int iqiq = 0; iqiq < v.size(); iqiq++) cout << v[iqiq] << " "; cout << "\n"


bool check(const string& s)
{
    for (int i = s.length() - 1; i >= 1; --i)
        if (s[i] < s[i - 1])
            return false;
    return true;
}

string solve(string& s)
{
    for (int i = s.length() - 1; i >= 0; --i) {
        if (check(s))
            break;
        s[i] = '9';
        int j = i - 1;
        s[j]--;
        while (s[j] < '0') {
            s[j] = '9';
            j--;
            s[j]--;
        }
    }
    while (s[0] == '0')
        s.erase(0, 1);
    return s;
}

int main()
{
    //FROM_FILE;
    //TO_FILE;

    int tt;
    cin >> tt;
    for (int Case = 1; Case <= tt; Case++) {
        string s;
        cin >> s;
        cout << "Case #" << Case << ": " << solve(s) << "\n";
    }

    return 0;
}

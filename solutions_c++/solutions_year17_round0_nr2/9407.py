#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i < (int)(b); ++i)

#define TRACE(x...)
#define PRINT(x...)
#define WATCH(x) TRACE(cout << #x << " = " << x << endl )

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<ll> vll;
typedef vector<vll> vvll;

bool check(string& s)
{
    for(int i = 1; i < s.size(); i++)
        if(s[i] < s[i-1])
            return false;
    return true;
}

void solveBack(string& s)
{
    for(int i = s.size(); i >= 0; i--)
    {
        if(s[i] > s[i+1])
        {
            s[i + 1] = '9';
            s[i] -= 1;
        }
    }
}

void solveFd(string& s)
{
    for(int i = 1; i < s.size(); i++)
    {
        if(s[i] < s[i-1])
        {
            s[i] = '9';
        }
    }
}

int main()
{
    int test;
    cin >> test;
    for1(t, test)
    {
        printf("Case #%d: ", t);
        string s;
        cin >> s;

        if(!check(s))
        {
            solveBack(s);
            if(s[0] == '0')
            {
                s.erase(s.begin());
                for(auto& p : s)
                    p = '9';
            }
            else
            {
                solveFd(s);
            }
        }

        cout << s << endl;

    }
    return 0;
}
#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef long long int ll;
typedef vector< pair<int, int> > vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long int> vll;
typedef pair<int, int> pii;

const ll INF = 1e18;
const int inf = 1e9;
const int MOD = 1e9 + 7;
const int nax = 1000000 + 10;

int main()
{
    ios::sync_with_stdio(0);

    freopen("input1.in", "r", stdin);
    freopen("output1.txt", "w" , stdout);

    int t;
    int test = 0;
    cin >> t;
    while(t--)
    {
        string s;
        int k;
        cin >> s >> k;
        int len = s.length();
        int moves = 0, flag = 0;
        for(int i = 0, j = k - 1; j < len ; i++, j++)
        {
            if(s[i] == '-')
            {
                for(int z = i; z <= j; z++)
                    {
                        if(s[z] == '-') s[z] = '+';
                            else s[z] = '-';
                    }
                moves++;
            }
        }
        for(int i = 0; i < len; i++)
        {
            if(s[i] != '+')
                flag = 1;
        }

        cout << "Case #" << ++test <<": ";
        if(flag == 1) cout << "IMPOSSIBLE" << endl;
        else cout << moves << endl;
    }

    return 0;
}

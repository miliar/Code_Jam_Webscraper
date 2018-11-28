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

bool istidy(int n)
{
    int flag = 0;
    int prev = 10;

    while(n)
    {
        int dig = n % 10;
        n /= 10;
        if(dig > prev)
            flag = 1;
        prev = dig;
    }
    return !flag;
}

int main()
{
     ios::sync_with_stdio(0);

    freopen("input1.in", "r", stdin);
    freopen("output2.txt", "w" , stdout);

    int t, test = 0;
    cin >> t;
    while(t--)
    {
        int n; cin >> n;
        for(int i = n; i > 0; i--)
        {
            if(istidy(i))
            {
                cout << "Case #" << ++test <<": ";
                cout << i <<endl;
                break;
            }
        }
    }
    return 0;
}

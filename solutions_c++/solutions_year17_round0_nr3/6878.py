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
     freopen("input1.in", "r", stdin);
    freopen("output4.txt", "w" , stdout);
    ios::sync_with_stdio(0);
    int t, test = 0; cin >> t;
    while(t--)
    {
        int n, k;
        cin >> n >> k;
        set<int> set1;
        set1.insert(0);
        set1.insert(n+1);

        int ansmaxlr,ansminlr;
        for(int counter = 1; counter <= k; counter++)
        {
            int ans,maxlr = -1,minlr = -1;
            for(int  i = 1; i <= n; i++)
            {
                if(set1.find(i) != set1.end()) continue;
                set<int>::iterator itr = lower_bound(set1.begin(), set1.end(), i);
                int maxi = *itr;
                itr--;
                int mini = *itr;
                int r = maxi - i - 1;
                int l = i - mini - 1;
                int curmaxlr = max(l,r);
                int curminlr = min(l,r);

                if(minlr == curminlr)
                {
                    if(curmaxlr > maxlr)
                    {
                        maxlr = curmaxlr;
                        ans = i;
                    }
                }
                else if(minlr < curminlr)
                {
                    minlr = curminlr;
                    maxlr = curmaxlr;
                    ans = i;
                }
            }

            set1.insert(ans);
            if(counter == k)
            {
                ansmaxlr = maxlr;
                ansminlr = minlr;
            }
        }
        cout << "Case #" << ++test <<": ";
        cout << ansmaxlr << " " << ansminlr << endl;
    }
    return 0;
}

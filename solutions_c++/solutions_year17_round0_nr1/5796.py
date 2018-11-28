#include <bits/stdc++.h>
#include <cstdio>
#include <cstdlib>
#define sz(a) int((a).size())
#define pb push_back
#define mt make_tuple
#define eb emplace_back
#define mp make_pair
#define all(c) begin(c),end(c)
#define present(c,x) (find(all(c),x) != end(c))
#define rep(i,a,b) for(int (i) = (a) ; (i) < (b) ;(i)++)
#define INF 2000000007
#define LINF 9000000000000000007
#define MOD 1000000007
#define MAX 100005
#define ios ios_base::sync_with_stdio(0)
#define readf(x) freopen(x, "r", stdin)
#define writef(x) freopen(x, "w", stdout)
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector< ii > vii;
typedef long long ll;
int s, k;
string pancakes;
char flip(char c)
{
    return c == '+' ? '-' : '+';
}
int main()
{
    freopen("A-large.in", "r+", stdin);
    freopen("Aout.txt", "w+", stdout);
    int t;
    cin >> t;
    for(int i = 0 ; i < t ; i++)
    {
        cin >> pancakes >> k;
        int size = pancakes.length();
        int ans = 0;
        for(int i = 0 ; i < size - k + 1; i++)
        {
            if(pancakes[i] == '-')
            {
                ans++;
                for(int j = 0 ; j < k ; j++)
                {
                    pancakes[i + j] = flip(pancakes[i + j]);
                }
            }
        }
        cout << "CASE #" << i + 1 << ": ";
        if(pancakes.find('-') != -1)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << ans << endl;
    }
}

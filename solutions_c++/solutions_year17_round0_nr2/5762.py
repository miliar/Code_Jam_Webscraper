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
int main()
{
    freopen("B-large.in", "r+", stdin);
    freopen("Bout.txt", "w+", stdout);
    int t;
    cin >> t;
    for(int i = 0 ; i < t ; i++)
    {
        string num;
        cin >> num;
        int size = num.length();
        for(int k = 0 ; k < size - 1 ; k++)
        {
            bool swapped = false;
            for(int j = 0 ; j < size - 1 ; j++)
            {
                if(num[j] > num[j + 1])
                {
                    swapped = true;
                    num[j++] -= 1;
                    for(; j < size ; j++)
                    {
                        num[j] = '9';
                    }
                    break;
                }
            }
            if(!swapped)
                break;
        }
        cout << "CASE #" << i + 1 << ": ";
        for(char c : num)
            if(c != '0')
                cout << c;
        cout << endl;
    }
}

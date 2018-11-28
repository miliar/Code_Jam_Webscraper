#include <bits/stdc++.h>
using namespace std;

#define pi 2.0*acos(0.0)
#define ri reverse_iterator
#define pq priority_queue
#define mp make_pair
#define ub upper_bound
#define er equal_range
#define nl '\n'
#define f first
#define lb lower_bound
#define mem(a, b) memset(a, b, sizeof(a))
#define q queue
#define s second
#define big INT_MAX
#define small INT_MIN
#define pb push_back
#define inp freopen("in.txt", "r", stdin)
#define out freopen("out.txt", "w", stdout)

typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef pair <long long, long long> pll;
typedef pair <long long, int> pli;

int main()
{
    inp;
    out;
    int a[1000], j = 0;
    for(int i = 1; i <= 999; i++)
    {
        int x, y, z;
        x = i%10;
        y = (i%100)/10;
        z = i/100;
        if(x >= y && y >= z)
        {
            a[j] = i;
            j++;
        }
    }
    //for(int i = 0; i < 1000; i++) cout << a[i] << " ";
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        int n;
        cin >> n;
        for(int jj = 0; jj < 1000; jj++)
        {
            if(a[jj] > n)
            {
                cout << "Case #" << i << ": " << a[jj-1] << "\n";
                break;
            }
        }
    }
}

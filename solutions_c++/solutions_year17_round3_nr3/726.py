/* ***************************
Author: Abhay Mangal (abhay26)
*************************** */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <numeric>
#include <utility>
#include <bitset>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
 #define tr(container, it) \
    for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define maX(a,b) (a) > (b) ? (a) : (b)
#define pii pair< int, int >
#define pip pair< int, pii >
#define pll pair < ll, ll >
#define pill pair< int, pll >
#define FOR(i,n) for(int i=0; i<(int)n ;i++)
#define REP(i,a,n) for(int i=a;i<(int)n;i++)
#define pb push_back
#define mp make_pair
#define pi 3.14159265358979323846
typedef long long ll;
int n,k;
double u,U;
double P[55];
int main()
{
    freopen("C-small-1-attempt2.in","r",stdin);
    freopen("C-small-1-attempt2.out","w",stdout);
    int t;
    scanf("%d",&t);
    int kas = 1;
    while(t--)
    {
        cout << "Case #" << kas++ << ": ";
        cin >> n >> k;
        cin >> u;
        U = (u*100000.0);
        //if(kas == 17)
           // cout << u << " " << U << endl;
        FOR(i,n)
        {
            double pp;
            cin >> pp;
            double PP = (pp*100000.0);
            P[i] = PP;
        }
        while(U > 0)
        {
            U--;
            int minPos = 0;
            int minVal = P[0];
            FOR(i,n)
            {
                if(P[i] < minVal)
                {
                    minVal = P[i];
                    minPos = i;
                }
            }
            P[minPos]++;
        }
        FOR(i,n)
        {
            P[i] = min(P[i], 100000.0);
        }
        long double ans = 1;
        FOR(i,n)
        {
            ans = ans * P[i];
            ans = ans / 100000.0;
        }
        //cout << ans << endl;
        //printf("%.8lf\n",ans);
        cout << fixed << setprecision(12) << ans << endl;
    }
    return 0;
}

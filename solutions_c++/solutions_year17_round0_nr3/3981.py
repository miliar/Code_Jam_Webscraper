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
typedef long long ll;
int main()
{

    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    int kas = 1;
    while(t--)
    {
        ll n,k;
        cin >> n >> k;
        cout << "Case #" << kas++ << ": ";
        priority_queue<int> P;
        P.push(n);
        int lx, ly;
        for(int i=0;i<k;i++)
        {
            int elem = P.top();
            P.pop();
            int a = elem/2;
            int b = elem/2;
            if(elem % 2 == 0)
                b--;
            lx = max(a,b);
            ly = min(a,b);
           // cout << i << " " << lx << " " << ly << endl;
            if(a > 0)
            P.push(a);
            if(b > 0)
            P.push(b);
        }
        cout << lx << " " << ly << endl;
    }
    return 0;
}

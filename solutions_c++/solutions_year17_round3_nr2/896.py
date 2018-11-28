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
int C,J;
int startC[5],endC[5];
int startJ[5],endJ[5];
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int t;
    scanf("%d",&t);
    int kas = 1;
    while(t--)
    {
        cout << "Case #" << kas++ << ": ";
        cin >> C >> J;
        FOR(i,C)
        cin >> startC[i] >> endC[i];
        FOR(i,J)
        cin >> startJ[i] >> endJ[i];
        if(C == J || (C+J == 1))
            cout << 2 << endl;
        else
        {
            if(C == 2)
            {
                int min1 = min(startC[0],startC[1]);
                int max1 = max(endC[0], endC[1]);
                int min2 = max(startC[0],startC[1]);
                int max2 = min(endC[0], endC[1]) + 1440;
                if(max1 - min1 <= 720 || max2 - min2 <= 720)
                    cout << 2 << endl;
                else
                    cout << 4 << endl;
            }
            else
            {
                int min1 = min(startJ[0],startJ[1]);
                int max1 = max(endJ[0], endJ[1]);
                int min2 = max(startJ[0],startJ[1]);
                int max2 = min(endJ[0], endJ[1]) + 1440;
                if(max1 - min1 <= 720 || max2 - min2 <= 720)
                    cout << 2 << endl;
                else
                    cout << 4 << endl;
            }
        }
    }
    return 0;
}

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
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    int kas = 1;
    while(t--)
    {
        string s;
        cin >> s;
        int k;
        cin >> k;
        cout << "Case #" << kas++ << ": ";
        vector<int> V;
        for(int i=0;i<s.length();i++)
        {
            if(s[i] == '+')
                V.pb(1);
            else
                V.pb(0);
        }
        int n = V.size();
        int ans = 0;
        for(int i=n-1;i>=k-1;i--)
        {
            if(V[i] == 0)
            {
                for(int j=i,cnt=0;cnt<k;cnt++,j--)
                {
                    V[j] = 1 - V[j];
                }
                ans++;
            }
            /*
            for(int x=0;x<n;x++)
                cout << V[x] << " ";
            cout << endl;*/
        }
        int gg = 1;
        for(int i=0;i<n;i++)
        {
            if(V[i] == 0)
            {
                gg = 0;
                break;
            }
        }
        if(gg)
            cout << ans << endl;
        else
            cout << "IMPOSSIBLE"  << endl;
    }
    return 0;
}

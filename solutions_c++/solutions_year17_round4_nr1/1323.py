#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <limits>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <map>
#include <set>
#define PI (acos(-1.0))
#define Abs(a) (((a)<0) ? (-(a)) :(a) )
#define rep(i,n) for((i)=0;(i)<(n);(i)++)
#define Rep(i,n) for(int i=0;i<(n);i++)
#define Rrep(i,n) for(int i=((n)-1);i>=0;i--)
#define rrep(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define Pii pair<int,int>
#define PB push_back
#define Size(x) ((int)(x.size()))
using namespace std;
typedef long long mint;
typedef unsigned long long umint;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("Aout.txt", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        int n,p;
        cin >> n >> p;
        int val;
        int tot[5] = {0};
        Rep(i,n)
        {
            cin >> val;
            tot[val % p]++;
        }
        printf("Case #%d: ", t);
        if(p == 2)
        {
            cout << tot[0] + (tot[1])/ 2 + (tot[1]%2) << endl;
        }
        else if(p == 3)
        {
            int ans = tot[0];
            int cur = min(tot[1], tot[2]);
            ans += cur;
            tot[1] -= cur;
            tot[2] -= cur;
            ans += (tot[1] / 3);
            ans += (tot[2] / 3);
            tot[1] -= 3 * (tot[1] / 3);
            tot[2] -= 3 * (tot[2] / 3);
            //cout << ans << " " << tot[0] << " " << tot[1] << endl;
            if(tot[1] + tot[2])
            {
                ans++;
            }
            cout << ans << endl;
        }
        else
        {
            int ans = tot[0];
            ans += tot[2] / 2;
            tot[2] -= 2*(tot[2] / 2);
            int cur = min(tot[1], tot[3]);
            ans += cur;
            tot[1] -= cur;
            tot[3] -= cur;
            if(tot[2] and max(tot[1], tot[3]) >= 2)
            {
                ans++;
                tot[2]--;
                if(tot[1])
                {
                    tot[1] -= 2;
                }
                else
                {
                    tot[3] -= 2;
                }
            }
            ans += (tot[1]/4);
            tot[1] -= 4*(tot[1]/4);
            ans += (tot[3]/4);
            tot[3] -= 4*(tot[3]/4);
            if(tot[1] + tot[2] + tot[3])
            {
                ans++;
            }
            cout << ans << endl;
        }
    }
}


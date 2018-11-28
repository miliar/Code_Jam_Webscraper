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
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    int kas = 1;
    while(t--)
    {
        string s;
        cin >> s;
        int valid = 1;
        int last = 0;
        int pos = -1;
        for(int i=0;i<s.length();i++)
        {
            int cur = s[i] - '0';
            if(cur < last)
            {
                valid = 0;
                pos = i;
                break;
            }
            last = cur;
        }
        cout << "Case #" << kas++ << ": ";
        if(valid)
            cout << s << endl;
        else
        {
            for(int i=pos;i<s.length();i++)
                s[i] = '9';
            for(int i=pos-1;i>=0;i--)
            {
                if(i == 0)
                {
                    int cur = s[i] - '0';
                    if(cur <= 1)
                    {
                        s = s.substr(1);
                        break;
                    }
                    s[i] = cur - 1 + '0';
                }
                else
                {
                    if(s[i] == s[i-1])
                    {
                        s[i] = '9';
                    }
                    else if(s[i] > s[i-1])
                    {
                        s[i]--;
                        break;
                    }
                    else
                        assert(0);
                }
            }
            cout << s << endl;
        }
    }
    return 0;
}

#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
#include <string.h>
#include <queue>
#include <set>
#include <map>
#include <math.h>
#include <stdio.h>
#include <vector>
#include <functional>
#include <bitset>
#include <iomanip>
#define ll long long
#define pi acos(-1.0)
#define pb push_back
#define MS0(ar) memset(ar,0,sizeof ar)
#define MS1(ar) memset(ar,-1,sizeof ar)
#define ff first
#define ss second
#define pii pair<int,int>
#define pll pair<ll,ll>
#define ind(a) scanf("%d",&a)
#define inf(a) scanf("%lf",&a)
#define inl(a) scanf("%lld",&a)
#define ins(a) scanf("%s",a)
#define pd(a) printf("%d\n",a)
#define pl(a) printf("%lld\n",a);
#define bitcnt(x) __builtin_popcountll(x)
#define mod 1000000007
const int MAX = 1e5 + 10;
using namespace std;
int get_ans(string s, int k)
{
    int l = s.length();
    int cnt = 0;
    for (int i = 0 ; i + k - 1 < l; i ++)
    {
        if (s[i] == '-')
        {
            for (int j = i; j <= i + k - 1 ; j ++)
            {
                if (s[j] == '+')
                    s[j] = '-';
                else
                    s[j] = '+';
            }
            cnt ++;
        }
       // cout << s << endl;
    }
    for (int i = 0 ; i < l; i ++) {
        if (s[i] == '-')
            cnt = -1;
    }
    return cnt;
}
int main()
{

    ios_base::sync_with_stdio(0);
    cin.tie(0);
#ifdef LOCAL_PROJECT
    freopen("../input.txt", "r", stdin);
    freopen("../output1.txt", "w", stdout);
#endif
    int t,k;
    string s;
    cin >> t;
    for (int i = 1; i <= t; i ++)
    {
        cin >> s >> k;
        //cout << s << endl;
        cout << "Case #" << i << ": " ;
        if (get_ans(s, k) == -1)
        {
            cout << "IMPOSSIBLE" << endl;
        }
        else
            cout << get_ans(s, k) << endl;
    }
    return 0;
}
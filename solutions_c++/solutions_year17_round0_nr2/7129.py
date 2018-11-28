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
string get_ans(ll x)
{
    string s_x = "", ans = "";
    while (x > 0)
    {
        s_x = char(x % 10 + '0')+ s_x;
        x /= 10;
    }
    if (s_x.length() <= 1)
        return s_x;
    int len = s_x.length();
    for (int i = len - 1; i >= 1;) {
        if (s_x[i] < s_x[i - 1])
        {
            int k = i - 1;
            while (s_x[k] == '0' && k >= 0)
                k--;
            s_x[k]--;
            for (int j = k + 1; j <= len - 1 ; j ++)
                s_x[j] = '9';

            i = k;
        }
        else
            i--;
    }
    int i = 0 ;

    while(s_x[i] == '0')
        i++;
    for(int j = i ; j < len; j++)
        ans += s_x[j];
    return ans;
}
int main()
{

    ios_base::sync_with_stdio(0);
    cin.tie(0);
#ifdef LOCAL_PROJECT
    freopen("../input.txt", "r", stdin);
    freopen("../output1.txt","w",stdout);
#endif
    int t;
    ll n;
    cin >> t;
    for (int i = 1; i <= t; i ++)
    {
        cin >> n;
        cout << "Case #" << i << ": " << get_ans(n) << endl;
    }
    return 0;
}
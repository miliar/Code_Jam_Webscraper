#include <bits/stdc++.h>
 
using namespace std;

using llong = long long;
using ld = long double;
using ii = pair<int,int>;
using ull = unsigned long long;


#define endl "\n"
#define fi first
#define se second
#define left LEVO
#define right PRAVO
#define time CHAS
#define prev PAPEREDNIKXD
#define next NASTUPNIKXD
#define pb push_back
#define deb cout<<"CHECK\n";
 
#define elif else if
#define cclear cout<<flush;
#define fclear fflush(stdout);
#define files freopen("melman.in","r",stdin);freopen("melman.out","w",stdout);
#define kchay ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
 
const llong over999 = 1e8;
const double eps = 1e-16;
const double Pi = acos(-1);
const llong md = 1e9+7;
/*****()***********************************************************/

int n;
string s;
int a[1010], y;

void change(int x, int y)
{
    for(int i=x;i<x+y;i++)
    {
        a[i]=1-a[i];
    }
}

bool check()
{
    for(int i=0;i<n;i++)
    {
        if(!a[i])return false;
    }
    return true;
}

main() {
    kchay;
    int test;
    cin >> test;
    for(int tcase = 1; tcase<=test; tcase++)
    {
        int ans=0;
        
        cout << "Case #" << tcase << ": ";
        cin >> s;
        cin >> y;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-')a[i]=0; else a[i]=1;
        }
        n = (int)s.length();
        for(int i=0;i<n-y+1;i++)
        {
            if(a[i]==0)change(i, y), ans++;
        }
        
        if(check()) cout << ans << endl;  else cout << "IMPOSSIBLE\n";
    }
    return 0;
}
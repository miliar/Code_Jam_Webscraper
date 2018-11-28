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

string s;

int check(string s)
{
    for(int i=1;i<s.length();i++)
    {
        if(s[i]<s[i-1])return i;
    }
    return -1;
}

void make_9(int x)
{
    for(int i=x;i<s.length();i++)
    {
        s[i]='9';
    }
}

void dec(int x)
{
    if(x==0)
    {
        s[x]--;
        return;
    }
    if(s[x]==s[x-1])
    {
        s[x]='9';
        dec(x-1);
    } else {
        s[x]--;
    }
}

main() {
    kchay;
    int test;
    cin >> test;
    for(int tcase = 1; tcase<=test; tcase++)
    {
        cout << "Case #" << tcase << ": ";
        cin >> s;
        int z = check(s);
        if(z==-1)
        {
            cout << s << endl;
            continue;
        }
        
        make_9(z);
        dec(z-1);
        while(s[0]<='0')s.erase(s.begin());
        cout << s << endl;
        
    }
    return 0;
}
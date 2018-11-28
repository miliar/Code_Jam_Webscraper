#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<complex>
#include<ctime>
#include<functional>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vi;
typedef vi::iterator vit;
typedef set<ll> si;
typedef si::iterator sit;
typedef vector<pii> vpi;
typedef pair<int, char> pci;
typedef vector<pci> vpci;

#define sq(x) ((x)*(x))
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
#define LL "%I64d"
//#define LL "%lld"
#define RLL(x) scanf(LL,&(x))


void test(int T)
{
    string s;
    cin>>s;
    for(int i = s.length() - 1; i >= 1; --i)
        if(s[i] < s[i-1])
        {
            --s[i-1];
            for(int j = i; j < s.length(); ++j)
                s[j] = '9';
        }
    if(s[0] == '0')
        s.erase(s.begin(), s.begin()+1);
    printf("Case #%d: %s\n", T, s.c_str());
    
}

int main()
{
    freopen("/Users/olpet/Downloads/GCJ/b.in", "r", stdin);
    freopen("/Users/olpet/Downloads/GCJ/b.out", "w", stdout);
    int n;
    cin>>n;
    for(int i = 0; i < n; ++i)
        test(i+1);
    return 0;
}

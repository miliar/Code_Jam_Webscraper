#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<array>
#include<vector>
#include<map>
#include<utility>
#include<bitset>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<utility>
using namespace std;
typedef long long ll;
typedef long double ld;
#define mod 1000000007
#define vec vector<long long>
#define arl(n) array<long long,n>
#define ard(n) array<double,n>
#define sc(n) scanf("%lld",&n)
#define prn(n) printf("%lld\n",n)
#define prs(n) printf("%lld ",n)
#define pr() printf("\n")
#define pb push_back
#define mp make_pair
int main()
{
    ll t;
    sc(t);
    ll tt=1;
    while(t--)
    {
        string a;
        cin>>a;
        ll l = a.length();
        bool b=0;
        for(ll i=0;i<(l-1);i++)
        {
            if(a[i]>a[i+1])
            {
                if(a[i]=='1')
                {
                    b=1;
                    break;
                }
                else
                {
                    ll j=i;
                    while(j>0)
                    {
                        if(a[j-1]!=a[i])
                        break;
                        else
                        j--;
                    }
                    a[j]--;
                    for(j=j+1;j<l;j++)
                    a[j]='9';
                    break;
                }
            }
        }
        printf("Case #%lld: ",tt);
        if(b)
        {
            for(ll i=0;i<(l-1);i++)
            printf("9");
        }
        else
        {
            for(ll i=0;i<l;i++)
            printf("%c",a[i]);
        }
        printf("\n");
        tt++;
    }
    return 0;
}
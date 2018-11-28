#include<bits/stdc++.h>
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
typedef unsigned long long ull;
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
using namespace std;
#define ll long long

int main()
{   ll t,o=1;
    cin>>t;
    while(t--)
    {   cout<<"Case #"<<o<<": ";
        ll a,b,c[2][2],i=0;
        cin>>a>>b;
        for(;i<a;)
        {    cin>>c[i][0]>>c[i][1];
            i++;
        }
        i=0;
        for(;i<b;)
        {   cin>>c[i+a][0]>>c[i+a][1];
            i++;
        }
        if(c[1][0]<c[0][0])
        {   i=c[1][0];
            c[1][0]=c[0][0];
            c[0][0]=i;
            i=c[1][1];
            c[1][1]=c[0][1];
            c[0][1]=i;
        }
        if(a==2 || b==2)
        {   if(c[1][1]-c[0][0]<=720 || c[1][0]-c[0][1]>=720)
                printf("2\n");
            else
                printf("4\n");
        }
        else
            printf("2\n");
        o++;
    }
    return 0;
}

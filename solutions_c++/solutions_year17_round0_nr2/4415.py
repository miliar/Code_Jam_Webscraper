#include <bits/stdc++.h>
#define slld(x) scanf("%lld",&x)
#define sd(x) scanf("%d",&x)
#define prd(x) printf("%d",x)
#define plld(x) printf("%lld",x)
#define nl printf("\n");
#define spc printf(" ");
#define forl(i,n) for(__typeof(n) i=0;i<n;i++)
#define forll(i,n,m) for(__typeof(n) i=n;i<=m;i++)
#define s1d(a,n) for(__typeof(n) i=0;i<n;i++) scanf("%lld",&a[i])
#define s2d(a,n,m) for(__typeof(n) i=0;i<n*m;i++) scanf("%lld",&a[i/m][i%m])
#define vi vector<int>
#define vlli vector<long long int>
#define ite(x,ty,i) x <ty> :: iterator i
#define pii pair<int,int>
#define prlld pair<lli,lli>
#define mp make_pair
#define pb push_back
#define ll long long
#define pi 3.14159265358979323846
#define MAX 100005
#define mycode int t; cin>>t; while(t--)
typedef long long int lli;
using namespace std;
int main()
{
	int que=0;
    mycode
    {
    	que++;
        lli num;
        cin>>num;
        int a[30];
        for (int i = 0; i < 30; ++i)
        {
            a[i]=0;
        }
        int p=29;
        while(num!=0)
        {
            a[p]=(num%10);
            num/=10;
            p--;
        }
        bool tidy=true;
        int mini=0;
        while(tidy)
        {
            for (int i = 0; i < 29; ++i)
            {
                if (a[i]>a[i+1])
                {
                    a[i]--;
                    for (int j = i+1; j < 30; ++j)
                    {
                        a[j]=9;
                    }
                }
            }
            tidy=false;
            for (int i = 0; i < 29; ++i)
            {
                if (a[i]>a[i+1])
                {
                    tidy=true;
                    i=30;
                }
            }
        }
        lli cnt=0;
        for (int i = 0; i < 30; ++i)
        {
            cnt*=10;
            cnt=a[i]+cnt;
        }
        cout<<"Case #"<<que<<": "<<cnt,nl
    }
    return 0;
}

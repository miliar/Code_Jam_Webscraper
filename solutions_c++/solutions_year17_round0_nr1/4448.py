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
        char a[1005];
        cin>>a;
        int a_sz;
        a_sz=strlen(a);
        int b[a_sz];
        for (int i = 0; i < a_sz; ++i)
        {
        	if (a[i]=='+')
        		b[i]=1;
        	else
        		b[i]=0;
        }
        int sz;
        cin>>sz;
        int lpl=a_sz-sz;
        int cnt=0;
        for (int i = 0; i <= lpl; ++i)
        {
        	if (b[i]==0)
        	{
        		for (int j = 0; j < sz; ++j)
        		{
        			b[i+j]=(b[i+j]+1)%2;
        		}
        		cnt++;
        	}
        }
        for (int i = lpl; i < a_sz; ++i)
        {
        	if (b[i]==0)
        		cnt=-1;
        }
        if (cnt!=-1)
        	cout<<"Case #"<<que<<": "<<cnt,nl
    	else
    		cout<<"Case #"<<que<<": IMPOSSIBLE",nl
    }
    return 0;
}

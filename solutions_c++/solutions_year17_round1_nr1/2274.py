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
        int r,c;
        cin>>r>>c;
        char a[r][c],b[r][c];
        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < c; ++j)
            {
                cin>>a[i][j];
                b[i][j]=a[i][j];
            }
        }
        bool change=false;
        int mxu,mxd;

        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < c; ++j)
            {
                //cout<<"Chk 1",nl;
                change=false;
                mxd=j;
                mxu=j;
                if (a[i][j]!='?'&&b[i][j]!='?')
                {
                    for (int k = j-1; k >= 0 && a[i][k]=='?'; --k)
                    {
                        change=true;
                        a[i][k]=a[i][j];
                        mxu=k;
                    }
                    for (int k = j+1; k < c && a[i][k]=='?'; ++k)
                    {
                        change=true;
                        a[i][k]=a[i][j];
                        mxd=k;
                    }

                //cout<<"Chk 2",nl;
                    change=false;
                    for (int k = i-1; k >= 0; --k)
                    {
                        for (int p = mxu;p <=mxd; ++p)
                        {
                            if (a[k][p]!='?')
                            {
                                change=true;
                                p=mxd;
                                k=0;
                            }
                        }
                        if (!change)
                        {
                            for (int p = mxu;p <=mxd; ++p)
                            {
                                a[k][p]=a[k+1][p];
                            }
                        }
                    }

                //cout<<"Chk 3",nl;
                    change=false;
                    for (int k = i+1; k < r; ++k)
                    {
                        for (int p = mxu;p <=mxd; ++p)
                        {
                            if (a[k][p]!='?')
                            {
                                change=true;
                                p=mxd;
                                k=r;
                            }
                        }
                        if (!change)
                        {
                            for (int p = mxu;p <=mxd; ++p)
                            {
                                a[k][p]=a[k-1][p];
                            }
                        }
                    }
                }
            }
        }
        

        cout<<"Case #"<<que<<":",nl
        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < c; ++j)
            {
                cout<<a[i][j];
            }
            nl
        }
    }
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<int> vi;

const ll INF=1e18;

const int mod=1000000007;

char maxchar (ll x, ll y, ll z)
{
    if (x>=y && x>=z)
        return 'R';
    else if (y>=z && y>=x)
        return 'Y';
    else
        return 'B';
}

int main()
{
    ll t,n,m,i,j,k,l;
    FILE *f1,*f2;

    f1=fopen("input.txt","r");
    f2=fopen("output.txt","w");
    fscanf (f1,"%lld",&t);
    for (ll q=1;q<=t;++q)
    {
        fscanf (f1,"%lld",&n);
        ll r,o,y,g,b,v;
        fscanf (f1,"%lld %lld %lld %lld %lld %lld",&r,&o,&y,&g,&b,&v);
        if (o==0 && g==0 && v==0)
        {
            m=(n/2);
            if (r>m || y>m || b>m)
                fprintf (f2,"Case #%lld: IMPOSSIBLE\n",q);
            else
            {
                char str[n+5],c;
                ll f=0;
                c=maxchar(r,y,b);
                if (c=='R')
                    f=1;
                else if (c=='Y')
                    f=2;
                else
                    f=3;
                for (i=0;i<n;i+=2)
                {
                    str[i]=c;
                    if (f==1)
                    {
                        r--;
                        if (r==0)
                            break;
                    }
                    else if (f==2)
                    {
                        y--;
                        if (y==0)
                            break;
                    }
                    else if (f==3)
                    {
                        b--;
                        if (b==0)
                            break;
                    }
                }
                if (i<n)
                {
                    c=maxchar(r,y,b);
                    if (c=='R')
                        f=1;
                    else if (c=='Y')
                        f=2;
                    else
                        f=3;
                    for (j=i+2;j<n;j+=2)
                    {
                        str[j]=c;
                        if (f==1)
                        {
                            r--;
                            if (r==0)
                                break;
                        }
                        else if (f==2)
                        {
                            y--;
                            if (y==0)
                                break;
                        }
                        else if (f==3)
                        {
                            b--;
                            if (b==0)
                                break;
                        }
                    }
                }
                if ((f==1 && r==0) || (f==2 && y==0) || (f==3 && b==0))
                    c=maxchar(r,y,b);
                for (i=1;i<n;i+=2)
                {
                    str[i]=c;
                    if (f==1)
                    {
                        r--;
                        if (r==0)
                            break;
                    }
                    else if (f==2)
                    {
                        y--;
                        if (y==0)
                            break;
                    }
                    else if (f==3)
                    {
                        b--;
                        if (b==0)
                            break;
                    }
                }
                c=maxchar(r,y,b);
                if (c=='R')
                    f=1;
                else if (c=='Y')
                    f=2;
                else
                    f=3;
                for (j=i+2;j<n;j+=2)
                {
                    str[j]=c;
                    if (f==1)
                    {
                        r--;
                        if (r==0)
                            break;
                    }
                    else if (f==2)
                    {
                        y--;
                        if (y==0)
                            break;
                    }
                    else if (f==3)
                    {
                        b--;
                        if (b==0)
                            break;
                    }
                }
                str[n]='\0';
                fprintf (f2,"Case #%lld: %s\n",q,str);
            }
        }
    }

    fclose(f1);
    fclose(f2);

	return 0;
}

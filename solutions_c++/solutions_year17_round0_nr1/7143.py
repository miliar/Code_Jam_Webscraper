#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<int> vi;

#define INF INT_MAX

const int mod=1000000007;

int main()
{
    ll t,n,m,i,j,k,l,x,y,z,f;
    FILE *f1,*f2;

    f1=fopen("input.txt","r");
    f2=fopen("output.txt","w");

    fscanf (f1,"%lld",&t);
    for (ll q=1;q<=t;++q)
    {
        char str[10009],cp[10009];
        fscanf (f1,"%s %lld",str,&k);
        strcpy(cp,str);
        n=strlen(str);
        x=z=f=l=0;
        for (i=0;str[i]!='\0';++i)
        {
            if (str[i]=='-')
            {
                x++;
                y=0;
                m=i+k;
                for (j=i;j<i+k && str[j]!='\0';++j)
                {
                    y++;
                    if (str[j]=='-')
                        str[j]='+';
                    else
                    {
                        str[j]='-';
                        if (m==i+k)
                            m=j;
                    }
                }
                i=m-1;
            }
        }
        if (y==k)
        {
            z=x;
            l=1;
        }
        x=0;
        for (i=n-1;i>=0;--i)
        {
            if (cp[i]=='-')
            {
                x++;
                m=i-k;
                f=1;
                y=0;
                for (j=i;j>(i-k) && j>=0;--j)
                {
                    y++;
                    if (cp[j]=='-')
                        cp[j]='+';
                    else
                    {
                        cp[j]='-';
                        if (m==i-k)
                            m=j;
                    }
                }
                i=m+1;
            }
        }
        if (y==k)
        {
            z=min(z,x);
            l=1;
        }

        if (f==1 && l==1)
            fprintf (f2,"Case #%lld: %lld\n",q,z);
        else if (f==0)
        {
            z=0;
            fprintf (f2,"Case #%lld: %lld\n",q,z);
        }
        else if (l==0)
            fprintf (f2,"Case #%lld: IMPOSSIBLE\n",q);
    }
    fclose(f1);
    fclose(f2);
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<int> vi;

#define INF INT_MAX

const int mod=1000000007;

void tidynumber(char *str, ll m)
{
    ll i,j;
    for (i=1;i<m;++i)
    {
        if (str[i]<str[i-1])
        {
            str[i-1]=char(str[i-1]-1);
            for (j=i;j<m;++j)
                str[j]='9';
            break;
        }
    }
    return;
}

bool isValid (char *str, ll m)
{
    ll i;
    for (i=1;i<m;++i)
        if (str[i]<str[i-1])
            return false;
    return true;
}

int main()
{
    ll t,n,m,i,j,k,l,x,y,z;
    FILE *f1,*f2;

    f1=fopen("input.txt","r");
    f2=fopen("output.txt","w");

    fscanf (f1,"%lld",&t);
    for (ll q=1;q<=t;++q)
    {
        char str[30];
        fscanf (f1,"%s",str);
        m=strlen(str);
        while (!isValid(str,m))
            tidynumber(str,m);
        n=0;
        for (i=0;str[i]!='\0';++i)
        {
            n*=10;
            n+=str[i]-'0';
        }
        fprintf (f2,"Case #%lld: %lld\n",q,n);
    }
    fclose(f1);
    fclose(f2);
	return 0;
}

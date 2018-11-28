
/***************************
 * 
 * Aditya Gangwar
 * MNNIT, ALLAHABAD
 * 
 * *************************/

#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mod 1000000007
#define li long int
#define lli long long int
#define ulli unsigned lli
#define fup(i,a,b) for(i=a;i<b;i++)
#define fdn(i,a,b) for(i=a;i>=b;i--)
#define wl while
#define mp make_pair
#define test li t;scanf("%ld",&t);wl(t--)
#define testf li t,tt;scanf("%ld",&t);for(tt=1;tt<=t;tt++)
#define si(i) scanf("%d",&i);
#define sl(i) scanf("%ld",&i);
#define sll(i) scanf("%lld",&i);
#define sull(i) scanf("%llu",&i);
#define pi(i) printf("%d\n",i);
#define pl(i) printf("%ld\n",i);
#define pll(i) printf("%lld\n",i);
#define pull(i) printf("%llu\n",i);
typedef pair<li, pair<li,li> > P;


//-----------------------------------------------------------------------



int main()
{
    testf
    {
        li k, c=0,i,j;
        string a;
        cin>>a;
        sl(k);
        fup(i,0,a.length())
        {
            if(a[i]=='+')
            {
                
            }
            else
            {
                c++;
                if(i+k-1>=a.length())
                {
                    break;
                }
                fup(j,0,k)
                {
                    if(i+j<a.length())
                    {
                        if(a[i+j]=='-')
                            a[i+j]='+';
                        else
                            a[i+j]='-';
                    }
                }
            }
        }
        int flag=0;
     cout<<"Case #"<<tt<<": "; 
        fup(i,0,a.length())
        {
            if(a[i]=='-')
            flag=1;
        }
        if(flag==1)
        {
            cout<<"IMPOSSIBLE\n";
        }
        else
        {
            cout<<c<<"\n";
        }
    }
    return 0;
}
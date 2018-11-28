
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
        li k, c=0,i,j,n;
        
        sl(n);
        for(i=n;i>=1;i--)
        {
            j=i;
            li prev=j%10;
            j/=10;
            int flag=0;
            while(j!=0)
            {
                if(prev<j%10)
                {
                    flag=1;
                    break;
                }
                prev=j%10;
                j/=10;
            }
            if(flag==0)
            {
                
                cout<<"Case #"<<tt<<": "<<i<<"\n";break;
            }
        }
        
      
        
    }
    return 0;
}
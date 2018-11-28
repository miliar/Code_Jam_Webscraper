#include <iostream>
#include <cstdio>
using namespace std;
long long int cpy,test,t,n,p,sol;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>t;
    for (long long int test = 1;test <= t;test++)
    {
        cin>>n;
        cpy = n;
        p=1;
        sol=0;
       // cout<<n<<" ";
        while (cpy)
        {
            if (cpy%10==0)
            {
                cpy--;
                sol = p-1+p*(cpy%10);
            }
            else
                sol = p*(cpy%10)+sol;
            p*=10;
            cpy/=10;
        }
        p=1;
        //cout<<sol<<" ";
        while (sol)
        {
            if ((sol%10)<(sol%100/10))
            {
                sol=sol-(sol%10)-1;
                cpy =p-1+p*(sol%10);
            }
            else
                cpy = p*(sol%10)+cpy;
            p*=10;
            sol/=10;
        }
        cout<<"Case #"<<test<<":"<<" "<<cpy;
        cout<<'\n';
    }
}

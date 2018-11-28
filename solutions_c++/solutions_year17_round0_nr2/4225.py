#include<iostream>
#include<fstream>
#define ull unsigned long long
using namespace std;
ifstream in("B-large.in");
ofstream out("B-large.out");
int le(ull n)
{
    int c=0;
    while(n>0)
    {
        c++;
        n/=10;
    }
    return c;
}
ull shift(ull n, int p)
{
    while(p--)
        n*=10;
    return n;
}
int numat(ull n,int idx)
{
    n/=shift(1, idx);
    n%=10;
    return n;
}
ull doit(ull n){
        int len=le(n);
        len-=1;
        ull ans=n;
        while(len--)
        {
            //cout<<numat(n,len+1)<<" "<<numat(n,len)<<" "<<len<<endl;
            if(numat(n,len+1)>numat(n,len))
            {
                ans=n;
                //cout<<ans<<endl;
                ans/=shift(1, len+1);
                //cout<<ans<<endl;
                ans--;
                //cout<<ans<<endl;
                ans*=shift(1, len+1);
                                //cout<<ans<<endl;

                ans+=shift(1, len+1)-1;
                                //cout<<ans<<endl;

                return ans;
            }
        }
        return ans;
}
bool notok(ull n)
{
    ull p=n%10;
    n/=10;
    while(n>0)
    {
        if(n%10 > p)
            return true;
        p=n%10;
        n/=10;
    }
    return false;
}
int main()
{
    int t;
    in>>t;
    for(int c=1; c<=t; c++)
    {
        ull n;
        in>>n;
        while(notok(n))
            n=doit(n);
        out<<"Case #"<<c<<": "<<n<<endl;
    }
}

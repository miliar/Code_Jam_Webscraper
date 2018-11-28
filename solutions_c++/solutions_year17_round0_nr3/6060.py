#include <bits/stdc++.h>
using namespace std;
long long int power(long long int a,long long int b)
{
    if(b==0)
        return 1;
    long long int res;
    if(b%2==0)
    {
        res=power(a,b/2);
        return res*res;
    }
    else
    {
        res=power(a,(b-1)/2);
        res=res*res;
        return res*a;
    }

}
int main()
{
    int t,q=1;
    cin>>t;
    while(t--)
    {
        long long int n,k;
        cin>>n>>k;
        long long int max,po=(long long int) (log(k) / (double)log(2) ),   x=power(2,po);
        max=n-k-x;
        double res = max /(double) (2*x) ;
       // cout<<res<<" "<<max<<endl;
        if(max % (2*x) == 0)
           {
            max = max /(double)(2*x) + 1;
            }
        else
        {
            max = ceil(max /(double) (2*x) );
        }
        long long int min;
        if(res - (long long int)res >=.5 )
            min = ceil(res);
        else
            min = res;
        printf("Case #%d: %lld %lld\n",q,max,min);
        q++;
    }
    return 0;
}
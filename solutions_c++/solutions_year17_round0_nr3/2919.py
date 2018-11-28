#include <iostream>
#include<bits/stdc++.h>
using namespace std;
pair<long long ,long long>ans2;
int main()
{
  freopen("in.txt" , "r" , stdin);
   freopen("out.txt" , "w" , stdout);
    int t,m = 1;
    cin>>t;
    while(t--)
    {
        long long n,k;
        scanf("%lld%lld" , &n , &k);
        long long x = 1 , mini , maxi , num1  = 1, num2 = 0 , num3 = 1;
        if(n&1) mini = maxi = (n-1)/2;
        else mini = n/2 - 1 ,  maxi = n/2 , num1 = 0  ,  num2 = 1 , num3 = 0;
        while(1)
        {
            if(k>x)
            {
                k-=x , x*=2;
                long long y = num1 , z = num2 , w = num3;
                if(maxi & 1)
                {
                    num1=y*2 + z;
                }
                else
                {
                    num1 = 0;
                    num2 = y*2 + z;
                }
                if(mini & 1)
                {
                    num3=w*2+z;
                }
                else
                {
                    num3 = 0;
                   num2 = w*2 + z;
                }
                if(maxi & 1) maxi = (maxi-1)/2;
                else maxi = (maxi)/2;

                if(mini & 1) mini =  (mini-1)/2;
                else  mini = (mini-1)/2 ;
            }
            else
            {
                if(k<=num1) ans2 = {maxi , maxi};
                else if(k<=num1+num2) ans2 = {maxi , mini};
                else ans2 = {mini , mini};
                break;
            }

        }
        printf("Case #%d: %lld %lld\n" , m++ , ans2.first , ans2.second);
    }
    return 0;
}

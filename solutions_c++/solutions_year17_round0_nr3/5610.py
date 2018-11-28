#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.in", "r" , stdin);
    freopen("output.out", "w", stdout);
    int caseno=0,t;
    cin>>t;
    long long int ci=1;
    while(caseno++<t)
    {
        long long int n,k,left,right,odd=0,even=0,num=1,l=0;
        cin>>n>>k;
        left=n;
        right=n;
        if(n%2==0)
            even=1;
        else
            odd=1;
        cout<<"Case #"<<caseno<<": ";
        while(1)
        {
            if(num>=k)
            {
                if(left%2==0)
                {
                    if(k>odd)
                    {
                        cout<<left/2<<" "<<max(l,left/2-1)<<"\n";
                    }
                    else
                    {
                        cout<<right/2<<" "<<max(l,right/2)<<"\n";
                    }
                    break;
                }
                else
                {
                    if(k<=even)
                    {
                        cout<<right/2<<" "<<max(l,right/2-1)<<"\n";
                    }
                    else
                    {
                        cout<<left/2<<" "<<max(l,left/2)<<"\n";
                    }
                    break;
                }
            }
            else
            {
                k-=num;
                num*=2;
            }
            long long int e1=even;
            long long int o1=even;
            if(left%2==1)
            {
                if((left/2)%2==0)
                    e1+=2*odd;
                else
                    o1+=2*odd;
            }
            else if(right%2==1)
            {
                if((left/2)%2==0)
                    e1+=2*odd;
                else
                    o1+=2*odd;
            }
            left=(left-1)/2;
            right/=2;
            odd=o1;
            even=e1;
        }
    }
    return 0;
}

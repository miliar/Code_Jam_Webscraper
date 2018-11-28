#include<bits/stdc++.h>
using namespace std;
int t,T;
long long n,k,i,p,v1,v2,f1,f2,ans1,ans2;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld%lld",&n,&k);

        map <long long,long long> m1,m2;
        m1[n]=1LL;
        i=0LL; p=1LL;
        while(1)
        {
            if(i+p<k)
            {
                for(auto i:m1)
                {
                    m2[(i.first>>1LL)]+=i.second;
                    m2[(i.first>>1LL)-!(i.first&1LL)]+=i.second;
                }
            }
            else
            {
                v1=-1LL;
                for(auto i:m1)
                {
                    if(v1==-1LL)
                    {
                        v1=i.first;
                        f1=i.second;
                    }
                    else
                    {
                        v2=i.first;
                        f2=i.second;
                    }
                }

                if(m1.size()>1 and i+f2>=k) //using v2
                {
                    ans1=ans2=v2>>1LL;
                    ans2-=!(v2&1LL);
                }
                else //using v1
                {
                    ans1=ans2=v1>>1LL;
                    ans2-=!(v1&1LL);
                }
                break;
            }
            m1=m2; m2.clear();
            i+=p; p<<=1LL;
        }

        printf("Case #%d: %lld %lld\n",++T,ans1,ans2);
    }
}

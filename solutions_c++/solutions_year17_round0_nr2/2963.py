#include <bits/stdc++.h>
using namespace std;
const int MAXD=20;
int T,last,digit,digits[MAXD];
long long N,M,ans;
bool poss;
long long query(int curr,int last,bool eq) {
    if (curr==digit) {
        return 1;
    }
    long long ans = 0;
    if (eq) {
        for (int i=last;i<=digits[curr];i++)
        {
            ans+=query(curr+1,i,eq && digits[curr]==i);
        }
    } else {
        for (int i=last;i<=9;i++){
            ans+=query(curr+1,i,0);
        }
    }
    return ans;
}
bool monotone(long long num)
{
    int temp=9;
    while (num)
    {
        if (num%10 > temp)
        {
            return false;
        }
        temp=num%10;
        num/=10;
    }
    return true;
}
void check(long long N,long long ans) {
    int last=9;
    long long temp;
    if (!monotone(ans))
    {
        printf("%lld %lld\n",N,ans);
    }
    for (long long i=ans+1;i<=N;i++)
    {
        if (monotone(i))
        {
            printf("%lld %lld %lld\n",N,ans,i);
            break;
        }
    }
}
int main()
{
    freopen("tidy2.in","r",stdin);
    freopen("tidy2.out","w",stdout);
    scanf("%i",&T);
    for (int i=0;i<T;i++) {
        scanf("%lld",&N);
        M=N;
        digit=0;
        while (M) {
            digits[digit++]=M%10;
            M/=10;
        }
        reverse(digits,digits+digit);
        ans=0;
        last=0;
        for (int i=0;i<digit;i++) {
            poss=true;
            for (int j=i+1;j<digit;j++)
            {
                if (digits[j]<digits[i])
                {
                    poss=false;
                }
                else if (digits[j]>digits[i]){
                    break;
                }
            }
            if (poss)
            {
                ans*=10;
                ans+=digits[i];
            } else {
                ans*=10;
                ans+=digits[i]-1;
                for (int j=i+1;j<digit;j++)
                {
                    ans*=10;
                    ans+=9;
                }
                break;
            }
        }
        //check(N,ans);
        printf("Case #%i: %lld\n",i+1,ans);
    }
}

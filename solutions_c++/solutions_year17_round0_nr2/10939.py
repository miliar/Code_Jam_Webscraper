#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("tidy1.txt","w",stdout);
    int t,x=1;
    scanf("%d",&t);
    while(t--)
    {
        unsigned long long int n,ans=0;
        int j=0,p,l,arr[18];
        scanf("%llu",&n);
        unsigned long long int k=n;
        while(k!=0)
        {
           k=k/10;
           j++;
        }
        p=j-1;

        while(n!=0)
        {
            l=n%10;
            arr[p]=l;
            n=n/10;
            p--;
        }
        for(int i=j-1;i>0;i--)
        {
            if(arr[i-1]>arr[i])
            {
                arr[i-1]=arr[i-1]-1;
                for(int m=i;m<j;m++)
                    arr[m]=9;
            }
        }
        for(int i=0;i<j;i++)
            ans= (ans*10)+arr[i];
            printf("Case #%d: %llu\n",x,ans);
            x++;
    }
    return 0;
}

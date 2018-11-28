#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<string>
using namespace std;
typedef long long ll;

int a[200],b[200];

int check(int x)
{
    int a=x%10;
    x/=10;
    int b=x%10;
    x/=10;
    int c=x%10;
    x/=10;
    int d=x%10;
    x/=10;
    if(d<=c&&c<=b&&b<=a)
        return 1;
    return 0;
}

int main()
{
    //freopen("B-small-attempt7.in","r",stdin);
    //freopen("B-large.out-1.txt", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++)
    {
        int n;
        scanf("%d",&n);
        for(int i=n;i>0;i--)
        {
            if(check(i))
            {
                printf("Case #%d: %d\n",ca,i);
                break;
            }
        }
//        ll n;
//        int cnt=0;
//        scanf("%I64d",&n);
//        while(n)
//        {
//            b[cnt++]=n%10;
//            n/=10;
//        }
//        for(int i=0;i<cnt;i++)
//            a[i]=b[cnt-1-i];
//        for(int i=1;i<cnt;i++)
//        {
//            if(a[i]<a[i-1])
//            {
//                if(i-2<0)
//                {
//                    a[i-1]--;
//                    for(int j=i;j<cnt;j++)
//                    {
//                        a[j]=9;
//                    }
//                    break;
//                }
//                else
//                {
//                    int tmp=0;
//                    for(int j=i-2;j>=0;j--)
//                    {
//                        if(a[j]!=a[j+1])
//                        {
//                            tmp=1;
//                            a[j+1]--;
//                            for(int k=j+2;k<cnt;k++)
//                                a[k]=9;
//                            break;
//                        }
//                    }
//                    if(tmp==1)
//                        break;
//                    if(tmp==0)
//                    {
//                        for(int k=1;k<cnt;k++)
//                            a[k]=9;
//                        a[0]=0;
//                        break;
//                    }
//                }
//                break;
//            }
//        }
//        printf("Case #%d: ",ca);
//        int flag=0;
//        for(int i=0;i<cnt;i++)
//        {
//            if(flag==0&&a[i]!=0)
//            {
//                flag=1;
//            }
//            if(flag)
//            {
//                printf("%d",a[i]);
//            }
//        }
//        printf("\n");
    }
    return 0;
}

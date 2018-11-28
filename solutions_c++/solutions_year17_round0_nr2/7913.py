#include <bits/stdc++.h>

#define MOD 1000000009

using namespace std;

int main()
{
    freopen("D:/codes/in.txt","r",stdin);
    freopen("D:/codes/out.txt","w",stdout);

    int t,i,j,k;
    long long n,ans;
    int a[20];

     scanf("%d",&t);
     int tc=t;
     while(t--)
     {
        scanf("%lld",&n);
        i=0;
        while(n>0)
        {
            a[i++]=n%10;
            n/=10;
        }
        k=i;
        //for(int l=0;l<k;++l)cout<<a[l]; cout<<endl;

        for(j=i-1;j>=0;--j)
        {
            //9998 9989 9899 8999
            //8999 9899 9989 9998
            if(a[j] > a[j-1])
            {
                a[j]-=1;
                for(int l=j-1;l>=0;--l)
                    a[l]=9;
                j=i;
                //for(int l=0;l<k;++l)cout<<a[l]; cout<<endl;
            }
        }

        if(a[k-1]==0)
            --k;
        printf("Case #%d: ",tc-t);
        for(int l=k-1;l>=0;--l)cout<<a[l]; cout<<endl;

     }

	return 0;

}

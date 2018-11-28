#include<bits/stdc++.h>
using namespace std;



int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("2.txt","w",stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d: ",ti++);
        int a[6];
        scanf("%*d");
        for(int i=0;i<6;i++)
            scanf("%d",a+i);
        a[1]=a[2];
        a[2]=a[4];
        int c=max(a[0],max(a[1],a[2]));
        if(c>a[0]+a[1]+a[2]-c)
            puts("IMPOSSIBLE");
        else
        {
            char s[]="RYB";
            if(a[0]<a[1])
                swap(a[0],a[1]),swap(s[0],s[1]);
            if(a[0]<a[2])
                swap(a[0],a[2]),swap(s[0],s[2]);
            int last=-1;
            while(a[0]+a[1]+a[2])
            {
                int f=0,d=0;
                for(int i=0;i<3;i++)
                    if(i!=last)
                    {
                        if(a[i]>f)
                        {
                            f=a[i];
                            d=i;
                        }
                    }
                last=d;
                a[d]--;
                putchar(s[d]);
            }
            puts("");
        }
    }
	return 0;
}

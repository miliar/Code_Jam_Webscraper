//
//  main.c
//  CJ
//
//  Created by Anmol mishra on 08/04/17.
//  Copyright ÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ© 2017 Anmol mishra. All rights reserved.
//

#include <stdio.h>

int fun(int n)
{
    int a,b,c,k;
    int temp=0,i;
    for(i=1;i<=n;i++)
    { k=i;
		if(i==1000)
{	temp=999;
break;
}
        a=k%10;
        k=k/10;
        b=k%10;
        k=k/10;
        c=k%10;
        if(a>=b && b>=c)
            temp=i;
    }
    return temp;
}
int main()
{
    int t;
    int n;
    int i;
    int ans;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d",&n);
        ans=fun(n);
        printf("Case #%d: %d\n",i+1,ans);
    }
    return 0;
}
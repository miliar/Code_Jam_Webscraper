//
//  main.c
//  CJ 1
//
//  Created by Anmol mishra on 08/04/17.
//  Copyright ÃÂ© 2017 Anmol mishra. All rights reserved.
//

#include <stdio.h>
#include <string.h>
//#define + 1
int size,count=0,s,flag=0;
char str[1000];
void fun(char st[])
{
    int j=0;
    int i;
    for(j=0; (st[j])!='\0';j++)
    {
        if(flag==1)
        {
            
            break;
        }
        
        else if(st[j]=='-')
           {
            for(i=j;i<j+size;i++)
            {
                if(j+size>strlen(st))
                {
                    flag=1;
                    //printf("IMPOSSIBLE\n");
                    i=j+size;
                }
                else
                {
                if(st[i]=='-')
                    st[i]='+';
                else
                    st[i]='-';
                }
                
            }count++;
            fun(str);
           }
    }
}
int main() {
    int n,i;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        count=0;
    scanf("%s %d",str,&size);
        fun(str);
        
        if(flag==0)
               printf("Case #%d: %d\n",i+1,count);
        else
            printf("Case #%d: IMPOSSIBLE\n",i+1);
        flag=0;
    }
    return 0;
}
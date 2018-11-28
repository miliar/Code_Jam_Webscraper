#include <stdio.h>
#include<bits/stdc++.h>using namespace std;
void findsuitable(char arr[],int b)
{ int i,j,k,v;
    j=0;
        while(arr[j]!='?')
        {
            j++;

            if(j>b-1)
            return;
        }
        k=j;
        while(arr[k]=='?')
        {
            k++;
            if(k>b-1)
            return;
        }
        for(v=j;v<=k;v++)
        arr[v]=arr[k];
    findsuitable(arr,b);
}
void moresuitable(char arr[],int b)
{int j,k,v;
    j=b-1;
        while(arr[j]!='?')
        {
            j--;

            if(j<0)
            return;
        }
        k=j;
        while(arr[k]=='?')
        {
            k--;
            if(k<0)
            return;
        }
        for(v=j;v>=k;v--)
        arr[v]=arr[k];

           moresuitable(arr,b);

}
void check(char str[][26],int b,int a,int k)
{int j,i,h;

     if(k==0)
     { h=0;
         while(str[h][0]=='?')
            h++;

         for(i=0;i<=h-1;i++)
         {
             for(j=0;j<=b-1;j++)
             str[i][j]=str[h][j];
         }
     }
     else if(k==(a-1))
     {   for(j=0;j<=b-1;j++)
         str[k][j]=str[k-1][j];
     }
     else
     {    for(j=0;j<=b-1;j++)
         str[k][j]=str[k-1][j];

     }

}

int main(void) {
    freopen("input6.txt","r",stdin);
    freopen("output6.txt","w",stdout);
    int a,b,i,j,k,v,flag,flag1,flag2,t,u,test; char str[26][26];
    scanf("%d",&test);
    for(u=0;u<=test-1;u++)
    {
    scanf("%d",&a);
    scanf("%d",&b);
    for(i=0;i<=a-1;i++)
    scanf("%s",&str[i]);

    for(i=0;i<=a-1;i++)
    {
        findsuitable(str[i],b);
    }

     for(i=0;i<=a-1;i++)
    {
        moresuitable(str[i],b);
    }
    //label:
    //flag=0;
    for(i=0;i<=a-1;i++)
    {
        if(str[i][0]=='?')
        {
        check(str,b,a,i);
        }
    }

    printf("Case #%d: \n",u+1);

    for(i=0;i<=a-1;i++)
    {
        for(j=0;j<=b-1;j++)
        printf("%c",str[i][j]);
        printf("\n");
    }

        printf("\n");
    }
	return 0;
}


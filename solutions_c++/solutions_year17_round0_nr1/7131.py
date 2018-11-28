#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

void stringflip(char str[],int startI,int k);

int main()
{
    int t,len,p,flips,k;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        p=0;
        flips=0;
        char str[1001];
        cin>>str;
        len=strlen(str);
        len--;
        cin>>k;
        while(p<=len-k+1)
        {
            if(str[p]=='-')
            {
                stringflip(str,p,k);
                flips++;
            }
            p++;
        }
        int flag=0;
        for(int i=len;i>len-k+1;i--)
        {
            if(str[i]=='-')
            {
               flag=1;
               break;
            }

        }
        if(flag==1)
        {
            printf("Case #%d: IMPOSSIBLE\n",z);
        }
        else
            printf("Case #%d: %d\n",z,flips);

    }
    return 0;
}

void stringflip(char str[],int startI,int k)
{
    for(int i=0;i<k;i++,startI++)
    {
        if(str[startI]=='+')
            str[startI]='-';
        else
            str[startI]='+';
    }
}

#include <stdio.h>
#include <iostream>
using namespace std;

bool needReduce(char num[])
{
    for(int i=0;num[i];i++)
    {
        if(num[i] > '1') return false;
        if(num[i] < '1') return true;
    }
    return false;
}

bool isTidy(char num[])
{
    for(int i=1;num[i];i++)
    {
        if(num[i-1] < num[i]) return false;
    }
    return true;
}

void makeReduce(char num[],int index)
{
    if(num[index] > '0') num[index]--;
    else
    {
        num[index] = '9';
        makeReduce(num,--index);
    }
}

void makeReset(char num[],int index)
{
    for(int i=index;num[i];i++) num[i] = '9';
    makeReduce(num,--index);
    
    if(index > 0)
    {
        if(num[index-1] > num[index]) makeReset(num,index);
    }
}

int main()
{
    int t;
    scanf("%d",&t);
    for(int _=1;_<=t;_++)
    {
        int len=0;
        char num[22];
        scanf("%s",num);
        
        while(num[++len]);
        
        if(needReduce(num))
        {
            printf("Case #%d: ",_);
            for(int i=1;num[i];i++) printf("9");
            puts("");
        }
        else
        {
            int index = 0;
            
            for(int i=1;num[i];i++)
            {
                if(num[index] != num[i]) index = i;
                if(num[i-1] > num[i]) makeReset(num,index);
            }
            printf("Case #%d: %s\n",_,num);
        }
    }
}

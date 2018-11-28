#include<iostream>
#include<cstdio>
#include<cstring>
void strfix(char str[],int p);
using namespace std;
int main()
{
    int t,len,p;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        char str[20];
        cin>>str;
        len=strlen(str);
        p=len-2;
        while(p>=0)
        {
            if(str[p]>str[p+1])
                strfix(str,p);
            p--;
        }
        p=0;
        while(str[p]=='0')
            p++;
        printf("Case #%d: %s\n",z,str+p);
    }
    return 0;
}

void strfix(char str[],int p)
{
    (int)str[p]--;
    p++;
while(str[p]!='\0')
    {
        str[p]='9';
        p++;
    }
}

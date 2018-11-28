#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
using namespace std;

int funcky(char str[],int l,int k)
{
    int count=0;
    for(int i=0;i<l;i++)
    {
        if(str[i]=='-')
        {
            if(i+k-1<l)
            {
                count++;
                for(int j=i;j<i+k;j++)
                {
                    if(str[j]=='-')
                        str[j]='+';
                    else
                        str[j]='-';
                }
            }
        }
    }

    int flag=0;
    for(int i=0;i<l;i++)
    {
        if(str[i]=='-')
            {flag=1;break;}
    }
    if(flag==0)
        return count;
    else
        return -1;
}

int main()
{
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        char str[1005];
        int k,l;
        scanf("%s %d",str,&k);
        l=strlen(str);
        int ans=funcky(str,l,k);
        if(ans<0)
            cout<<"Case #"<<test<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<test<<": "<<ans<<endl;
    }
	return 0;
}

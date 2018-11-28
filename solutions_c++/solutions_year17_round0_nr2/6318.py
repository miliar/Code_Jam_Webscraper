#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>

using namespace std;

void fun(int arr[],int l)
{
    int flag=0,index=l-1;
    for(int i=l-1;i>=1;i--)
    {
        if(arr[i] >= arr[i-1])
        {
            if(flag==0)
            {
                flag=1;
                index=i;
            }
            else
                continue;
        }
        else
        {
            arr[i-1]--;
            flag=0;
            for(int j=i;j<=index;j++)
                arr[j]=9;
            index--;
        }
    }
}


int main()
{
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        long long int n,n1,ans=0;
        int arr[20]={0};
        char str[20];
        int count=0;

        scanf("%s",str);
        int l=strlen(str);
        for(int i=0;i<l;i++)
        {
            arr[i]=str[i]-'0';
        }

        fun(arr,l);

        for(int i=0;i<l;i++)
        {
            ans=(ans*10)+arr[i];
        }
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
    return 0;
}

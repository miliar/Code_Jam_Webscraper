#include<bits/stdc++.h>
using namespace std;
int main()
{
int t;
cin>>t;
int test=1;
while(t--)
{
    char a[1010];
   long long  int k,n,c=0;
     long long int flag=0;
     cin>>a>>k;
     n=strlen(a);
    for(long long int i=0;i<n-k;i++)
    {
        if(a[i]=='+')
            continue;
        else if(a[i]=='-')
        {
            for(long long int j=i;j<i+k;j++)
            {
                if(a[j]=='+')
                    a[j]='-';
                else if(a[j]=='-')
                        a[j]='+';

            }
            c++;
        }
    }

    for(long long int i=n-k;i<n-1;i++)
    {
        if(a[i]==a[i+1])
            continue;
        else
        {
            flag=1;
            break;
        }
    }
    if(flag==1)
        cout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;
    else if(flag==0&&a[n-1]=='+')
        cout<<"Case #"<<test<<": "<<c<<endl;
    else if(flag==0&&a[n-1]=='-')
        cout<<"Case #"<<test<<": "<<c+1<<endl;


        test++;

}
return 0;
}

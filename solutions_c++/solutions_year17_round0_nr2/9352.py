#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    int i,j,t,l,flag=0,eq;
    char a[30];
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>a;
        l=strlen(a);
        if(l==1){}
        else
        {
            for(j=1,flag=0;j<l;j++)
            {
                if(a[j-1]<a[j]) flag=1,eq=0;
                else if(a[j-1]==a[j])   eq++;
                else if(a[j-1]>a[j] && flag==0)
                {
                    if(a[0]=='1')
                    {
                        for(j=0;j<l-1;j++)  a[j]='9';
                        a[j]='\0';
                    }
                    else
                    {
                        a[0]-=1;
                        for(j=1;j<l;j++)    a[j]='9';
                    }
                }
                else if(a[j-1]>a[j])
                {
                    j-=eq;
                    a[j-1]-=1;
                    for(j;j<l;j++)  a[j]='9';
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<a<<endl;
    }
    return 0;
}

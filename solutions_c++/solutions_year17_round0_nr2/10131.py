#include<bits/stdc++.h>
using namespace std;
int main()
{

    int a[50],i,t,k,j,m,f,b,flag=0;
    long long int x,temp;
    string s;
    cin>>t;
    for(i=0;i<t;i++){
        cin>>x;
    temp=x;
    stringstream ss;
    ss<<x<<endl;
    s=ss.str();
    k=s.length()-1;
    for(j=k-1;j>=0;j--)
    {
        a[j]=temp%10;
        temp=temp/10;
    }
        while(a[j]==0 && j>=0)
        {
flag=1;
            j--;
        }
        if(flag)
        {
        a[j]-=1;
        m=j+1;
        while(m<k)
        {
                a[m]=9;
                m++;
        }
        }
    for(j=k-1;j>0;j--)
    {
        while(a[j]>=a[j-1] && j>0)
        {
            j--;
        }
        if(j!=0)
        {
        a[j-1]-=1;
        f=j;
        while(f<k)
        {
        a[f]=9;
        f++;
        }
        }
    }
    cout<<"Case #"<<i+1<<": ";
    for(b=0;b<=k-1;b++)
    {
        while(a[b]==0 && b<k)
            b++;
        cout<<a[b];
    }
    cout<<endl;
}

    }

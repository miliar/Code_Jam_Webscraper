#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int i,j,k,l,m,n,t,x,y;
    string a;
    cin>>t;
    for(l=1;l<=t;l++)
        {
        x=0;
        cin>>a>>k;
        n=a.size();
        for(i=n-1;i>=0;i--)
        {
            if(a[i]=='-')
                {
                break;
            }
        }
        n=i+1;
        m=0;
        if(n<=0)
            {
            x=1;
        }
        else
            {
        for(i=0;i<n-k+1;i++)
            {
            if(a[i]=='-')
                {
                m++;
                for(j=0;j<k;j++)
                    {
                    if(a[i+j]=='-')
                        {
                        a[i+j]='+';
                    }
                    else
                        {
                        a[i+j]='-';
                    }
                }
            }
        }
        for(i=n-k+1;i<n&&i>=0;i++)
            {
            if(a[i]!=a[i-1])
                {
                x=0;
                break;
            }
        }
        if(i==n)
            {
            if(n>0&&a[n-1]=='-')
                {
                m++;
            }
            x=1;
        }
        }
        cout<<"Case #"<<l<<": ";
        if(x==0)
            {
            cout<<"IMPOSSIBLE\n";
        }
        else if(x==1)
            {
            cout<<m<<endl;
        }
        
    }
    return 0;
} 

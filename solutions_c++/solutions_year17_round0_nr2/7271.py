#include<bits/stdc++.h>
using namespace std;
int main()
{
    int u;
    cin>>u;
    int q=1;
    while(q<=u)
    {
        long long int m;
        cin>>m;
        int c[19],j=0,k,i;
        for(i=0;i<=18;i++)
            c[i]='$';
        while(m!=0)
        {
            c[j]=m%10;
            m=m/10;
            j++;
        }
        for(i=1;i<j;i++)
        {
            if(c[i]>c[i-1])
            {
                c[i]=c[i]-1;
                for(k=0;k<=i-1;k++)
                   c[k]=9;
                }
        }
        cout<<"Case #"<<q<<": ";
        q++;
        int h=0;
        for(i=j-1;i>=0;i--)
        {
            if(c[i]==0)
            h++;
            else
                break;
        }
        for(i=j-1-h;i>=0;i--)
        {
          cout<<c[i];
        }
          cout<<"\n";
    }
}

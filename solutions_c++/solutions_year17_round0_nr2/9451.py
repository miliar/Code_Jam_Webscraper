#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t,n,i,j,no,x,y;
    freopen("inp3.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>n;
        for(j=n;j>=1;j--)
        {
            y=j;
            x=y%10;
            y/=10;
            while(y>0)
            {
                no=y%10;
                if(no>x)
                    break;
                y/=10;
                x=no;
            }
            if(y==0)
                break;
        }
        cout<<"Case #"<<i+1<<": "<<j<<endl;
    }
}

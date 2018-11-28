#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
	int t;
    cin>>t;
    int x=1;
    while(x<=t)
    {
        string a;
        cin>>a;
        int n=a.length();
        if(n==1)
        {
            cout<<"Case #"<<x<<": ";
            cout<<a<<endl;
            x++;
            continue;
        }
        else
        {
            int i=n-1;
            if(a[n-1]=='0')
            {
                while(a[i]=='0')
                {
                    a[i]='9';
                    i--;
                }
                a[i]=a[i]-1;
            }
            int flag=0;
            while(flag==0)
            {
            for(i=0;i<n-1;i++)
            {
                if(a[i]>a[i+1])
                {
                    flag=0;
                    a[i]=a[i]-1;
                    for(int j=i+1;j<n;j++)
                    a[j]='9';
                    break;
                }
                else
                    flag=1;
            }
            }
            int flag1=0;
            cout<<"Case #"<<x<<": ";
            for(int i=0;i<n;i++)
            {
                if((a[i]=='0')&&(flag1==0))
                    continue;
                else
                    flag1=1;
                cout<<a[i]-'0';
            }
            cout<<"\n";
        }
        x++;
    }

	return 0;
}


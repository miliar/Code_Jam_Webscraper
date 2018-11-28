#include<iostream>
using namespace std;
int main()
{     int t,tt;
       cin>>t;
       tt=t;
       while(t--)
       {
           string a;
       int f=0,g=0,k,c=0,j=0;
       cin>>a>>k;
        int n=a.length();
       for(int i=0;a[i]!='\0';i++)
        if(a[i]=='-')
        {
            f=1;
            break;
        }
        if(f==0)
        cout<<"Case #"<<tt-t<<": "<<'0'<<endl;
        else
        {
            for(int i=0;i<n;i++)
            if(a[i]=='-')
            {
                c++;
                for(int j=i;j<=(i+k-1) && (i+k-1)<n ;j++)
                {
                if(a[j]=='+')
                a[j]='-';
                else
                a[j]='+';
                }
            }
            for(int i=0;a[i]!='\0';i++)
        if(a[i]=='-')
        {
            g=1;
            break;
        }
         if(g!=1)
            cout<<"Case #"<<tt-t<<": "<<c<<endl;
            else
                cout<<"Case #"<<tt-t<<": "<<"IMPOSSIBLE"<<endl;
        }

	   }
	return 0;
}

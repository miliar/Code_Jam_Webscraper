#include <bits/stdc++.h>
using namespace std;

int main() {
	long long int T,m,n,i,j,d,x,flag,y;
	int a[19];
	cin >> T;y=1;
	while(T--)
{
    cin >> n;
    cout <<"Case #"<<y<<": ";y++;
    m=n;
    i=0;
   flag=1;
    while(m)
    {
       d=m%10;
       a[i++]=d;
       m=m/10;
    }
    for(j=0;j<=(i-1)/2;j++)
    {
        int t=a[j];
        a[j]=a[i-1-j];
        a[i-1-j]=t;
    }
     for(j=0;j<=i-2;j++)
    {
        if(a[j]>a[j+1])
        {
                flag=0;
                if(j==0)
                {
                if(a[0]!=1)        cout << a[j]-1;
                for(j=1;j<=i-1;j++) cout << "9";
                }
                else
                {
                    while(j!=0 && a[j]-1<a[j-1])
                    {
                        j=j-1;
                    }
                     if(j==0)
                                                      {
                                                          if(a[0]!=1)        cout << a[j]-1;
                                                          for(j=1;j<=i-1;j++) cout << "9";
                                                        }
                   else
                   {
                       for(x=0;x<j;x++)cout << a[x];
                       cout << a[j]-1;
                       for(x=j+1;x<=i-1;x++) cout << "9" ;
                   }
                }
          
            break;
            
        }
        
    }
    if(flag==0)cout << endl;
    else cout << n << endl;
  
   
}	return 0;
}

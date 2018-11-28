#include <iostream>
#include <fstream>
using namespace std;

int main() {
	// your code goes here

	int t,digits,j,k,num,a[5],b[5],s;
	int m,n;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n;
		digits=0;
		j=0;
		for(m=n;m!=0;m=m/10)
		{
			digits++;

		}
		m=n;
		k=0;
		s=9;
		for(j=digits;j>0;j--)
		{
		    a[j]=m%10;
			m=m/10;
			if(a[j]<s)
			    s=a[j];
		}
		for(j=1;j<=digits;j++)
		{
		    if(k == 1)
		    {
		        b[j]=9;
		    }
		    else if(a[j]>s)
		    {   if(a[j]>=a[j+1])
                {
                    k=1;
                    b[j] = a[j]-1;
                    continue;
                }
                else
                {
                    b[j] = a[j];

                }
		    }
		    else
		    {
		        b[j] = s;
		        s= a[j+1];
		        for(m=j+1;m<=digits;m++)
                {
                    if(a[m]<s)
                    s=a[m];
                }
            }
		}
		cout<<"Case #"<<i<<": ";
		for(j=1;j<=digits;j++)
		{
		    if(j==1 && b[j]==0)
		        continue;
		    cout<<b[j];
		}
		cout<<endl;
	}
	return 0;
}

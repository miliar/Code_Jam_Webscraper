#include<iostream>
using namespace std;
int main()
{
	freopen("B-small-attempt3.in", "r", stdin);
    // freopen("B-large.in", "r", stdin);
    freopen("outputb.txt", "w", stdout);
	int t, x = 1,n,num,m,r,i=0,f;
    cin>>t;
    while(t--)
	 {

    	cout<<"Case #"<<x++<<": ";
    	cin>>num;
    	n=num;
    	if(num %10 == num) 	///logic for len=1
		{
    		cout<<num;
    	}
    	else
    	{	
    		int a[50];
    		while(n!=0)
    		{
    			m=n;
    			i = 0;
    			while(m!=0)
    			{
    				a[i]= r=m%10;
    				m = m/10;
    				i++;
    			}
				i--;
				for(int j=0;j<=i-1;j++)
				{
					if(a[j]>=a[j+1])
					{
						f=0;
					}	
					else
					{
						f=1;
						break;
					}
				}
				if(f == 0) 
				{
					
					cout<<n;
					cout<<"\n";
					break;
				}
				else 
				{
					
					n--;
				}
			}
		}
	}
	return 0;
}

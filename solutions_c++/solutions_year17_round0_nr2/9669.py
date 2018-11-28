#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int tc,t;
	unsigned long long int n;
	int arr[22];
	//cout<<"hey"<<endl;
	cin>>t;

	for(tc=1;tc<=t;tc++)
	{
  		cin>>n;
  		int i=0;
  		while(n)
  		{
  			arr[i++]=n%10;
  			n/=10;
  			
  		}

  		int l=i;
  		cout<<"Case #"<<tc<<": ";
  		if(l==1) //unit digit cases
  			cout<<arr[0]<<endl;
  		else
  		{
	  		i=l-1;
	  		while(i>0)
	  		{
	  			if(arr[i-1]<arr[i])
	  			{
	  				arr[i]=arr[i]-1;
	  				int j=i-1;
	  				while(j>=0)
	  				{
	  					arr[j--]=9;
	  				}
	  				if(i+1<=l-1)
	  				{
	  					i=i+1;
	  					continue;
	  				}
	  				else
	  					break;
	  			}

	  			i--;
	  		}
	  		i=l-1;
	  		while(i>=0)
	  		{
	  			if(arr[i]!=0)
	  				cout<<arr[i];
	  			i--;

	  		}
	  		cout<<endl;
  		}
  		
  		

	}
	
	return 0;
}
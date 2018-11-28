#include<iostream>
using namespace std;
int main()
{
  int t;
  cin>>t;
  int m=0;
  while(t--)
  {
    m++;
  	int k,r1,r;
  	int rev=0;
  	cin>>k;
  	for(int i=k;i>0;i--)
  	{
  		int n=i;
  		rev=0;
  		r1=n%10;
  		n=n/10;
  		for( ;n>0;n=n/10)
  		{
  			r=r1;
  			r1=n%10;
  			if(r<r1)
  				break;

  		}
  		
  		if(n==0)
  		{
  			cout<<"Case #"<<m<<": "<<i<<endl;
  			break;
  		}

  	}
  }

return 0;

}
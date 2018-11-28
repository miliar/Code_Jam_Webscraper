#include <iostream>
#include <string.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
	   int n,flag=0,ans;
	   cin>>n;
	   for(int j=n;j>=1;j--)
	   {
	      int next=j;
	      while(next != 0) 
	      { int val=next%10;
	        next /= 10; 
	        int val2=next%10;
	        if(val2>val)
	        {
	        flag=0;
	        break;
	        }
	        if(val>=val2)
	        flag=1;
	      }
	      if(flag)
	      {
	      ans=j;
	      break;
	      }
	   }
	   cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}

#include<iostream>
#include<string>

using namespace std;

int main()
{
  int t,d,n;
  cin>>t;
  for(int j=1;j<=t;j++)
    {
      cin>>d>>n;
      int k,s;
      double slowtime = 0;
      for(int i=0; i<n; i++)
	{
	  cin>>k>>s;
	  double time = (double) (d-k)/s ;
	  
	  if (time > slowtime)
	    slowtime = time;

	}
      printf("Case #%d: %f\n",j,(double) d/slowtime);
    }
  
}

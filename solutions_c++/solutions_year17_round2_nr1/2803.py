#include<bits/stdc++.h>

using namespace std;

int main()
{
  int t;
  cin>>t;
  for(int q=1;q<=t;q++)
  {
  	int n,count=0,i;
  	double max=0,d,s,k;
  	cin>>d>>n;
  	for(i=0;i<n;i++)
  	{
  	    cin>>k>>s;
  	    if((d-k)/s>max)
  	        max=(d-k)/s;
  	}
    double cspeed= d/max;
    cout<<"Case #"<<q<<": ";
    printf("%06f\n", cspeed);
  }
  return 0;
}

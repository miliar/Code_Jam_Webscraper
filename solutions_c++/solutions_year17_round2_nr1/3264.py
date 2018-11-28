#include <bits/stdc++.h>
using namespace std;

int main() 
{
  long long int T,t,d,n,k,s,i;
  double res,time,min;
  for(cin>>T, t = 1; t <= T; t++)
  {
  	//if(t==44){
  	min = 0;
  	cin >> d >> n;
  	//cout << "d n " << d <<" "<<n <<"\n";
  	for(i=0;i<n;i++)
  	{
  		cin>>k>>s;
  	//	cout << "k s "<<k<<" "<< s << "\n";
  		time = (double)(d - k)/s;
  		if(time>min)
  			min = time;
  	//	cout << "min " << min << "\n";
  	}
  	res = d/min;
  	cout<<"Case #"<<t<<": ";
  	printf("%6f\n",res);
  }
//}
}

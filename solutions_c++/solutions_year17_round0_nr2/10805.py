#include <iostream>
using namespace std;
int main() {
 long long int t, n,a,j,k;
  cin >> t;
  for(j=0;j<t;j++)
  {
  	cin>>n;
  	a=n;
  	long long int m[20],result;
  	m[0]=9;
  	int i=0;
  	//int ok=0;
  	for(k=a;k>0;k--)
  	{
  	    n=k;i=0,
  	    while(n)
      	{
      		m[++i]=n%10;
      		n=n/10;
      		if(m[i-1]>=m[i]){
      		    continue;
      		}
      		else
      		{
      			break;
      		}
    	}
    	if(n<10 && m[i-1]>=m[i]){
    	    //flag=1;
    	    cout << "Case #" << j+1 << ": "  << " " << k << endl;
    	    break;
    	}

	}
   }
  return 0;
}


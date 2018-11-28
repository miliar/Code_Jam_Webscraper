#include <iostream>
#include <string>
using namespace std;
 
int main()
{
	int t,it=1;
	cin>>t;
	while(it<=t)
	{
		long long int k,n,q,r,v=1,max, min, div;
		cin>>n>>k;
		while(v<k)
		{
			v*=2;
			v++;
		}
		q=(n-v)/(v+1);
		r=(n-v)%(v+1);
		div=(v+1)/2;
		min=q;
		if(r>div)
		{
			if((k-(div-1))<=(r-div))
			{
				min++;
			}
		}

		max=q;

		if((k-(div-1))<=r)
			{
				max++;
			}

				
		cout << "Case #" << it << ": "<< max << " " << min << endl;
		
		it++;
		

	}
	
 
 
 
	return 0;
} 
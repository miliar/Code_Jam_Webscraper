// Tidy Numbers

#include<iostream>
#include<string>
using namespace std;

int main()
{
	int t;
	cin>>t;
	//fflush(system.in);
	string n;
	for( int i=1; i<=t; i++ )
	{
		cin>>n;
			
			for( int j=n.size()-2; j>=0; j-- )
			{
				if(n[j]>n[j+1])
				{	
					n[j] = n[j]-1;
					for( int k=j+1; k<n.size(); k++ )
						n[k] = '9';
				}
			}	
		n.erase(0, min(n.find_first_not_of('0'), n.size()-1));
		cout<<"Case #"<<i<<": "<<n<<endl;
	}
	return 0;
}

#include <iostream>

using namespace std;

int main() {

		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
		long long int t;
		cin>>t;

		for(int k = 0 ; k < t ; k ++)
		{
			long long int n;
			cin>>n;	
			
			while(n > 0)
			{
				long long int temp = n;
				long long int prev = temp % 10;
				temp = temp / 10;
				long long int temp2;
				
				while(temp>0)
				{
					temp2 = temp % 10;
					if(temp2 <= prev)
					{
						prev = temp2;
						temp = temp / 10;
					}
					else
						break;
				}
				if(temp == 0)
					break;
				n--;
			}
			cout<<"Case #"<<k+1<<": "<<n<<endl;	
		}
		return 0;
	}





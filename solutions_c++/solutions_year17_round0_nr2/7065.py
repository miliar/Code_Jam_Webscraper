#include <iostream>
#include <math.h>

using namespace std;

int main () {
	unsigned int t;
	cin >> t;
	for (int i1 =1;i1<=t;i1++) {
		unsigned long long int n;
		cin >>n;
		if (n/10 == 0) {		
			cout <<"Case #"<<i1<<": "<<n<<endl;
		}	
		else  {
			int count = 1;
			unsigned long long int n1 = n;
			while (1) {
				if (n1/10 == 0)
				{
					break;
				}
				int lastBit = n1%10;
				int secondLasTBIT = (n1/10)%10;
				if (secondLasTBIT > lastBit)	
				{
					unsigned long long int n2 = n1/10;
					unsigned long long int n3 = pow(10,count);
					n = (n2 * n3)  - 1;

				}
				n1 = n/(unsigned long long int)pow(10,count);
				
				count++;
			}
		cout <<"Case #"<<i1<<": "<<n<<endl;
		}

	}
	return 0;
}
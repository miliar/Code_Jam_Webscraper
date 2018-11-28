#include <iostream>

using namespace std;

int main()
{
	int t;
	long int n, temp;
	
	cin >> t;
	
	for(int i=0;i<t;i++){
		cin >> n;
		
		if(n>=0 && n<=9)
		{
			cout << "Case #" << i+1 << ": " << n << endl;
		}
		else if(n>9)
		{
			temp = n;
			while(temp!=0){		
				if((temp % 10) >= ((temp / 10) % 10))
				{
					temp /= 10;
				}
				else{
					n = n - 1;
					temp = n;
				}
			}
			if(temp == 0 )cout << "Case #" << i+1 << ": " << n << endl;
		}
	}
}

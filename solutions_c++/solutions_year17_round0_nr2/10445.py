#include <iostream>

#include <cmath>

using namespace std;


unsigned GetNumberofDigits(unsigned i){

	return i > 0 ? (int)log10((double)i)+1:1;
}


int main(){
	int tc;
	int N;
	int test=1;
	int value;
	unsigned size;
	int currentvalue;
	cin >> tc;
	while(tc--){
		cin>>N;
		size=GetNumberofDigits(N);
		for (int i = N; i > 0; i--)
		{
			value=i%10;
			int j = 1;
			while ( j < size)
			{
				currentvalue=(i / (int)pow(10,j))%10;
				if(value < currentvalue){
					break;
				}
				
				value=currentvalue;
				j++;
			}
			

			if(j==size){
				cout <<"Case #"<<test<<": "<<i << endl;
				break;
			}
	
		}
		test++;

	}




	return 0;
}
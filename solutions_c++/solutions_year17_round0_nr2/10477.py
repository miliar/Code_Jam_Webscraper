#include <iostream>

using namespace std;

bool numIsTidy( int n){
	int tmp = 10;
	int test;
	
	while(n > 0){
		test = n % 10;
		if(tmp < test)
			return false;
		tmp = test;
		n = n / 10;
	}
	return true;
}

int main(){
	int t;
	 int n;
	
	cin >> t;
	
	for(int i = 1; i <= t; i++){
		cin >> n;
		
		while(n > 0){
			if(numIsTidy(n)){
				cout << "Case #" << i << ": " << n << endl;
				break;
			}
			else
				n--;
		}
	}
  
  return 0;
}


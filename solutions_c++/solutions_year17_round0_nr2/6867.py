#include <iostream>


using namespace std;


bool isTidy(long long num){

	while(num >= 10){
		if(num % 10 < (num / 10) % 10) return false;
		num = num / 10;
	}
	return true;
}


int main(){
	int T;
	int num;
	cin >> T;

	for(int i = 0; i < T; i++){
		cin >> num;
		while(!isTidy(num)) num--;
		cout << "Case #" << i+1 << ": " << num << endl;
	}


}

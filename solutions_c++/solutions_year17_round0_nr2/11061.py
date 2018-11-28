#include <iostream>
#include <string>

using namespace std;

bool isTidy(long num){
	string str = to_string(num);
	for(int i = 1; i < str.length(); ++i){
		if(str[i] < str[i-1])
			return false;
	}
	return true;
}

int main(int argc, char const *argv[]){
	int cases;
	cin >> cases;
	for(int cse = 1; cse <= cases; ++cse){
		long num;
		cin >> num;
		for(long i = num; i > 0; --i){
			if(isTidy(i)){
				cout << "Case #" << cse << ": "<< i << endl; 
				break;
			}
		}

	}
	return 0;
}
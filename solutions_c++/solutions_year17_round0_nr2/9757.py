#include <iostream>
using namespace std;

bool isTidy(string s){
	int size = s.size();
	if(size == 1){
		return true;
	}
	for(int i=1; i<size; i++){
		if(s[i]<s[i-1]){
			return false;
		}
	}
	return true;
}

int main(){
	unsigned long long int t, n;
	cin >> t;
	for(int i=1; i<=t; i++){
		cin >> n;
		for(unsigned long long int j=n; j>=0; j--){
			if(isTidy(to_string(j))){
				cout << "Case #" << i << ": " << j << endl;
				break;
			}
		}
	}
	return 0;
}

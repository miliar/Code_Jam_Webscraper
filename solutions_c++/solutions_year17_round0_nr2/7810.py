#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main(){
	string num;
	int t, T, i, j;
	
	cin >> T;
	t = T;
	
	while(t--){
		cin >> num;
		
		if(num.length() == 1){
			cout << "Case #" << T-t << ": " << num << endl;
			continue;
		}
		
		for(i=0; i < num.length(); i++){
			
			
			if(num[i] < num[i-1]){
				j = i;
				while(num[j] < num[j-1]){
					num[j] = '9';
					num[j-1] -= 1;
					j--;
				}
				break;
			}	
		}
		
		for(; i<num.length(); i++)	num[i] = '9';
		
		if(num[0] == '0') cout << "Case #" << T-t << ": " << num.substr(1) << endl;
		else cout << "Case #" << T-t << ": " << num << endl;
	}
	
	return 0;
}

#include<iostream>
#include<string>

using namespace std;

int main(){
	int TC;
	cin >> TC;
	
	for (int iTC = 0; iTC < TC; iTC++){
		string input;
		cin >> input;
//		
//		bool check = false;
//		bool check2= true;
//		
		cout << "Case #" << iTC+1 << ": ";
//		
//		for(int i = 0; i < input.length(); i++){
//			if((input[i] != '0') && (input[i] != '1')){
//				check = true;
//				break;
//			}  
//			
//			if(input[i] == '0'){
//				check2 = false;
//			}
//			
//		}
//		
//			if((!check) && (check2)){
//				
//				for(int i = 0 ; i < input.length()-1; i++){
//					cout << 9;
//				}
//				cout << endl;
//				continue;
//			}
		
		for(int i = input.length() - 1; i > 0; --i){
			if(input[i-1] > input[i]){
				input[i-1] -=1;
				for(int j = i; j < input.length(); ++j){
					input[j] = '9';
				}
			}
		
		} 
		
		for(int i = 0; i < input.length(); ++i){
			if(input[i] == '0'){
				continue;
			} else {
				cout << input[i];
			}
		}
		
		cout << endl;
	}
	
	return 0;
}

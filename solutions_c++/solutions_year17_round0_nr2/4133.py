#include <iostream> 
#include <fstream> 
#include <cstdlib> 
#include <algorithm> 
#include <string> 
using namespace std;  

bool isTidy(string &s){
	for (int i = 0; i < s.size()-1; i++){
		if (s[i] > s[i+1]) return false;  
	}
	return true;  
}

int main(){
	int t; 
	cin >> t;  
	for (int test = 1; test <= t; test++){
		string n; 
		cin >> n;  
		if (n.size() == 1){
			cout << "Case #" << test << ": " << n << endl; 
		}else if (isTidy(n)){
			cout << "Case #" << test << ": " << n << endl; 
		}else{
			int idx = 0; 
			for (int i = 0; i < n.size()-1; i++){
				if (n[i] > n[i+1]){
					idx = i;  
					break; 
				}
			}
			int val = n[idx]-'0';  
			val--;  
			n[idx] = char(val+'0');  
			// all indexes after idx should be fixed to 9. 
			for (int i = idx+1; i < n.size(); i++){
				n[i] = '9';  
			}
			// check if indexes before idx maintain the tidy property  
			for (int i = idx; i >= 1; i--){
				if (n[i] < n[i-1]){
					n[i] = '9';  	
					val = n[i-1]-'0';  
					val--;  
					n[i-1] = char(val+'0');   
				}
			} 
			// get rid of leading zeroes if there's any.  
			int i = 0;  
			while (n[i] == '0'){
				i++;  
			} 
			cout << "Case #" << test << ": " << n.substr(i) << endl; 
		}
	}
	return 0; 
}
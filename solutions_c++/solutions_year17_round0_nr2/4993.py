#include <iostream>
#include <vector>
#include <string>

using namespace std;

void sol(string& a){

	int n = a.size();
	int i = 0;
	for(; i < a.size() - 1; ++i){
		if(a[i] > a[i + 1]) break;
	}

	if(i == a.size() - 1){
		return;
	} 

	else{
		for(int j = i + 1; j < n; ++j){
			a[j] = '9';
		}
		if(a[i] == '1'){
			for(int j = 0; j <= i; ++j){
				a[j] = '9';
			}
			a = a.substr(1);
			return;
		}else{
			a[i] = (a[i] - '0') - 1 + '0';
			sol(a);
		}
		
	}
}

int main(){
	int t;
	cin >> t;
	
	string a; 
	for(int i = 0; i < t; ++i){
		cin >> a;

		sol(a);
		cout << "Case #" << i+1 << ": " << a << endl;
	}
}
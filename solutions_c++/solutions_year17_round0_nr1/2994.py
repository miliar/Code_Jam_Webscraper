#include <iostream>
using namespace std;


int main(){
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++){
		string inp;
		int k;
		cin >> inp >> k;
		int ans = 0;
		//cout << inp << endl;
		for (int i=0;i<inp.length();i++){
			if (inp[i] == '-'){
				if (i+k > inp.length()){
					ans = -1;
					break;
				}
				ans++;
				for (int j=0;j<k;j++)
					inp[i+j] = (inp[i+j] == '-' ? '+' : '-');
				
			}
		}
		cout << "Case #" << test << ": ";
		if (ans == -1) 
			cout << "IMPOSSIBLE";
		else 
			cout << ans;
		cout << endl;
	}
	
	
	return 0;
}
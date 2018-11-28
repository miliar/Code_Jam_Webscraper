#include <iostream>
#include <string>

using namespace std;

int main (){
	int t, k;
	string s;
	
	cin >> t;
	int p = t;
	while(t--){
		cin >> s >> k;
		bool a = false;
		int count = 0;
		for (int i=0 ; i<s.length() ; i++){
			if ( s[i] == '-') {
				
				if (s.length() - i >= k) {
					
					count++;
					
					for (int j=0 ; j<k ; j++){
						if (s[i+j] == '+')
							s[i+j] = '-';
						else
							s[i+j] = '+';
					}
					
				}
				else{
					a=true;
				}
				
			}
		}
		
		if (a) {
			cout << "Case #" << p - t << ": IMPOSSIBLE" << endl;
		}
		else{
			cout << "Case #" << p - t << ": "<< count << endl;
		}
		
	}
}

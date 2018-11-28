#include <iostream>
#include <string>

using namespace std;

int main(){
	int T, k, count;
	string s;
	cin >> T;
	for( int i = 1; i<=T; i++ ){
		cin >> s;
		cin >> k;
		count = 0;
		for (int j = 0; j < s.length() && k<=s.length(); ){
			if( s.at(j) == '+' ){
				s.erase(0, 1);
			}else{
				for(int z=0; z<k; z++){
					if( s.at(z) == '+' ){
						s.at(z) = '-';
					} else {
						s.at(z) = '+';
					}
				}
				count++;
			}
		}
		if( s.length()==0 ){
			cout << "Case #" << i << ": " << count << endl;
		} else{
			if( s.find("-") == s.npos ){
				cout << "Case #" << i << ": " << count << endl;
			} else{
				cout << "Case #" << i << ": IMPOSSIBLE" << endl;
			}
		}
	}
	return 0;
}
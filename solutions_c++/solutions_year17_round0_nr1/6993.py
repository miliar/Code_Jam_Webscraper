//Irvin Gonzalez
//
// Oversized Pancake Flipper
//


#include <iostream>
#include <string>

using namespace std;

void ans() {
    string s; 
    cin >> s;
    int k;
    cin >> k;
    int flip = 0;
    for(int i = 0; i < s.size(); ++i) {
    	if(s[i] == '-') {
		++flip;
		if((i+k) > s.size()) {
			cout << "IMPOSSIBLE";
			return; }
		for(int j = 0; j < k; ++j) {
			if(s[i + j] == '-')
			       s[i + j] = '+';
		        else 
			       s[i + j] = '-'; }
	}	
    }
    cout << flip;
}
int main() {

	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		ans();
		cout << endl; }
	return 0;
}

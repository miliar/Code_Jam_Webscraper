#include <iostream>

using namespace std;

int main()
{
	int T; cin >>T;
	
	for(int cs{1}; cs <= T; ++cs) {
		string s; cin >>s;
		int l = s.length();
		for(int i = l-2; 0 <= i; --i) {
			if(s[i] > s[i+1]) {
				s[i] -= 1;
				for(int j = i+1; j < l; j++) {
					s[j] = '9';
				}
			}
		}
		int i{0};
		while(s[i] == '0' and i < s.length() ) {
			++i;
		}
		cout <<"Case #" <<cs <<": " <<&s[i] <<endl;
	}
	return 0;
}


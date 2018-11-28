#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int N;
	cin >> N;
	for(int n = 1 ; n <= N ; n++) {
		string s;
		cin >> s;
		reverse(s.begin(), s.end());

		s += "0";
		for(int i = 0 ; i < s.size() - 1 ; i++) {
			if (s[i] < s[i+1]) {
				for(int j = 0; j <= i ; j++) {
					s[j] = '9';
				}
				s[i+1]--;
			}
		}

		reverse(s.begin(), s.end());
		while (s[0] == '0') {
			s.erase(0, 1);
		}				
		
		cout<<"Case #"<<n<<": "<<s<<endl;
	}
	return 0;
}
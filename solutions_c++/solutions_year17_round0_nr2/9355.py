#include <iostream>
#include <string>

using namespace std;

int t, m, p, i;
string s, v;

int main() {
	cin >> t;
	m = t;

	while(t--) {
		cin >> s;

		p = s.length();

		for(i = s.length()-1; i > 0; --i){
			if(s[i-1] > s[i]){
				v = s.substr(i-1, 1);
				s.replace(i-1, 1, to_string(std::stoi(v)-1));
				p = i;			
			}
		}

		for(i = p; i < s.length(); ++i)
			s.replace(i, 1, to_string(9));

		for(i = 0; i < s.length(); ++i)
			if(s[i] == '0')
				s.erase(0, 1);

		cout << "Case #" << m-t  << ": "<< s << endl;
	}
}
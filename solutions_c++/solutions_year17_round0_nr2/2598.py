#include <iostream>
#include <string>

using namespace std;

bool check(string s) {
	for (int i=0; i<s.size()-1; i++)
		if (s[i] > s[i+1]) return false;
	
	return true;
}

int main()
{
	int TM;
	cin >> TM;
	for (int T=1; T<=TM; T++) {
		string s,t;
		cin >> s;
		
		if (check(s))
			cout << "Case #" << T << ": " << s << "\n";
		else {
			for (int i=s.size()-1; i>=0; i--) {
				if (s[i] == '0') continue;
				t = s;
				t[i] = s[i]-1;
				for (int j=i+1; j<s.size(); j++)
					t[j] = '9';
				if (check(t)) {
					if (t[0] == '0')
						cout << "Case #" << T << ": " << t.substr(1) << "\n";
					else
						cout << "Case #" << T << ": " << t << "\n";
					break;
				}
			}
		}
	}
}

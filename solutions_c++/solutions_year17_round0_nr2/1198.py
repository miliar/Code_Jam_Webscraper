#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define endl '\n'

void main() {
	std::ios::sync_with_stdio(false);
	
	
	int t, n, m;
	string s;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.



	for (int i = 1; i <= t; ++i) {
		cin >> s;
		
		for ( int j = 1; j < s.size(); j++)
		{
			if (s[j] < s[j - 1]) {
				s[j - 1]--;

				int k = j - 1;
				while (k>0 && s[k]<s[k-1])
				{
					s[k-1]--;
					k--;
				}

				


				for (size_t l = k+1; l < s.size(); l++)
				{
					s[l] = '9';
				}


				break;
			}
		}
		
		
		if (s[0] == '0') {
			s.erase(s.begin());
		}


		cout << "Case #" << i << ": " << s << endl;
		
	}
}
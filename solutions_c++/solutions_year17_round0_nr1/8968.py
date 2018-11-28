#include <iostream>
#include <algorithm>    // std::find
#include <string>

using namespace std;

int main()
{
	int cases, k, count;
	string s;
	cin >> cases;
	for (int c = 0; c < cases; ++c)
	{	
		count = 0;
		cin >> s >> k;
		for (int i = 0; i <= s.length() - k; i++) {
			if(s[i] == '-') {
				for(int j = 0; j < k; j++) {
					if (s[i  + j] == '-') {
						s[i + j] = '+';
					} else {
						s[i + j] = '-';
					}
				}
				count++;
			}
		}
		bool possible = true;
		for (int i = 0; i < s.length(); i++) {
			if(s[i] == '-') {
				possible = false;
			}
		}
		if (possible) {
			cout << "Case #" << c + 1 << ": " << count << endl;
		} else {
			cout << "Case #" << c + 1 << ": " << "IMPOSSIBLE" << endl;
		}		
	}
	return 0;
}
#include <iostream>
#include <set>
#include <string>
using namespace std;
int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		string s;
		int size;
		cin >> s;
		cin >> size;
		int count = 0;
		bool impossible = false;
		for (int j = 0; j < s.length(); ++j) {
			if (s.compare(j, 1, "-") == 0) {// flip
				if (j + size - 1 < s.length()) {
					
					for (int k = j; k < j+size; k++){
						if (s.compare(k, 1, "-") == 0) {
							s.replace(k, 1, "+");
						}
						else {
							s.replace(k, 1, "-");
						}
                   }
					count++;
				}
				else {
					
						cout << "Case #" << i << ": IMPOSSIBLE" << endl;
						impossible = true;
						break;
					
				}
			}
			
		}
		if (!impossible) {
			cout << "Case #" << i << ": " << count << endl;
		}
		

		
	}


	cin.get();
	cin.get();
	return 0;
}

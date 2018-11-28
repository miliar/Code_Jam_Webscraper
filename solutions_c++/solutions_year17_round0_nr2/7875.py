#include <iostream>
#include <string>

using namespace std;

int main(){
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t){
		cout << "Case #" << t << ": ";
		string n;
		cin >> n;
		int s = int(n.size());
		bool b = false;
		for (int i = 0; not(b) and i < s - 1; ++i){
			if (n[i] > n[i + 1]){
				b = true;
				int j;
				for (j = i - 1; j >= 0 and n[j] == n[i]; --j);
				--n[j + 1];
				for (j = j + 2; j < s; ++j) n[j] = '9';
			}
		}
		if (n[0] == '0') n.erase(0, 1);
		cout << n;
		cout << endl;
	}
	return 0;
}

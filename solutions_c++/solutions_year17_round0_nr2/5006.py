#include <iostream>
#include <fstream>

using namespace std;
int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	freopen("in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, counter = 1;
	cin >> t;
	while (t--) {
		string s;
		cin >> s;
		int tmp = -1;
		string output_string;
		for (int i = 0; i < (int) s.size(); i++) {
			if (i + 1 < (int) s.size() && s[i] > s[i + 1]) {
				tmp = i;
				for (int j = i;j >= 0 && s[j] > s[j + 1]; j--) {
					s[j]--;
					tmp = j;
				}
				break;
			}
		}
		for (int i = 0; i < (int) s.size(); i++) {
			if (tmp == -1 || i <= tmp ) {
				if(output_string.size() == 0 && s[i] == '0')
					continue;
				output_string += s[i];
				continue;
			}
			output_string += '9';
		}
		cout << "Case #" << counter << ": " << output_string << "\n";
		counter++;
	}
}

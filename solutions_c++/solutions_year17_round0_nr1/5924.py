#include <iostream>
#include <string>
using namespace std;

string find_solution(string s, int k) {
	int count = 0;
	int i = 0;
	while (i < s.size()) {
		if (s[i] == '+') i++;
		else if (i+k-1 >= s.size()) {
//			cout << s << endl;
//			cout << i << endl;
			return "IMPOSSIBLE";
		}
		else {
			for (int j = 0; j < k; j++){
				if (s[i+j] == '-') s[i+j] = '+';
				else s[i+j] = '-';
			}
			count++;
			i++;
		}
	}
	return to_string(count);
}
int main(int argc, char *argv[]) {
	int n;
	string s;
	int k;
	cin >> n;
	for (int i = 0; i < n; i++){
		cin >> s >> k;
		string ans = find_solution(s, k);
		cout << "Case #" << i+1 << ": " << ans << endl;
	} 
}
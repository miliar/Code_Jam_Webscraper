#include <iostream>
#include <string>
#include <math.h>
using namespace std;

long long int find_solution(long long int x) {
	string s = to_string(x);
	while (true){
		s = to_string(stoll(s));
		int i = 0;
		while (i+1 < s.size() && s[i] <= s[i+1]) i++;
		if (i == s.size() - 1) return stoll(s);
	
		while (s[i] == '1' && i > 0) i--;
		s[i] = s[i] - 1;
		for (int j = i+1; j < s.size(); j++) {
			s[j] = '9';
		}
	}
}
int main(int argc, char *argv[]) {
	int n;
	string s;
	long long int k;
	cin >> n;
	for (int i = 0; i < n; i++){
		cin >> k;
		long long int ans = find_solution(k);
		cout << "Case #" << i+1 << ": " << ans << endl;
	} 
}
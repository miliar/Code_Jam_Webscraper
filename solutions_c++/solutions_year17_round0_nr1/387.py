#include<iostream>
#include<vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int T;
	cin >> T;
	
	for(int TCASE = 0; TCASE < T; TCASE++) {
		cout << "Case #" << TCASE+1 << ": ";
		
		string s;
		int k;
		cin >> s >> k;
		
		int result = 0;
		
		for(int i=0;i<(int)s.size();i++) {
			if(s[i] == '-') {
				result++;
				if(i+k > (int)s.size()) {
					result = -1;
					break;
				}
				
				for(int j=0;j<k;j++)
					s[i+j] = (s[i+j]=='+' ? '-' : '+');
			}
		}
		
		if(result == -1)
			cout << "IMPOSSIBLE\n";
		else
			cout << result << '\n';
	}
	
	return 0;
}
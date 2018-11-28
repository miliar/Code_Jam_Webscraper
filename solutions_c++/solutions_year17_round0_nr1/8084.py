#include <iostream>
#include <string>
#include <vector>
using namespace std;

class solution {
public:
	string flip(string s, int k) {
		vector<int> cake(s.size(), -1);
		for (int i = 0; i < s.size(); i++) {
			if(s[i] == '+')
				cake[i] = 1;
		}
		int cnt = 0;
		for (int i = 0; i <= s.size()-k; i++) {
			if (cake[i] == -1) {
				cnt++;
				for (int j = 0; j < k; j++) {
					cake[i+j] = -cake[i+j];
				}
			}	
		}
		if (cake != vector<int>(s.size(),1)) 
			return "IMPOSSIBLE";
		return to_string(cnt);
	}
};

int main() {
	string s;
	int cnt,k;	
	solution A;
	cin>>cnt;
	for (int i = 1; i<=cnt; i++) {
		cin >> s >> k;
		cout<<"Case #" << i << ": " << A.flip(s,k) << endl;
	}
}
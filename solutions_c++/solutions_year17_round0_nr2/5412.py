#include <iostream>

using namespace std;

int main(){
	string s;
	int t;
	cin >> t;
	for(int j = 1; j <= t;j++){
		int a, b, c;
		bool order = false;
		cin >> s;
		while(true){
		order = true;
		bool change = true;
		for(int i = 0; i < s.size() - 1; i++){
			a = (int)(s[i] - '0');
			b = (int)(s[i + 1] - '0');
			while(a > b){
				b--;
				if(b < 0){
					b = 9;
					if(change){
						a--;
					}
					change = false;
				}
				s[i + 1] =  (char)(b + '0');
				s[i] =  (char)(a + '0');
				order = false;
			}
		}
		if(order) break;
	}
		for(int i = 0; i < s.size(); i++){
			if(s[i] != '0') break;
			s.erase(i, i+1);
		}
		cout << "Case #" << j << ": " << s << endl;
	}
}
#include <iostream>
#include <string> 

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		string N, Y;
		cin >> N;
		Y += N[0];
		for(int i = 1; i < N.size(); i++) {
			if(Y[i - 1] <= N[i]) 
				Y += N[i];
			else {
				for(int j = i - 1; j >= 0; j--) {
					Y[j]--;
					if(j == 0 or Y[j - 1] <= Y[j])
						break;
					Y.pop_back();
				}
				while(Y.size() < N.size())
					Y += '9';
				break;
			}
		}
		if(Y[0] == '0') Y = Y.substr(1);
		printf("Case #%d: %s\n", t, Y.c_str());
	}
}

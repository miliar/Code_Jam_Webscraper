#include <iostream>
#include <string>
using namespace std;

int main(){
	string N;
	int T, j;
	size_t leading0;
	cin >> T;
	for (int t = 1; t <= T; ++t){
		cin >> N;
		N = "0" + N;
		for (int i = 1; i < N.length(); ++i){
			if (N[i] < N[i-1]){ //decreasing
				j = i - 1;
				while(N[j-1] == N[i-1]) --j;
				N[j] = N[j] - 1;
				for (j = j + 1; j < N.length(); ++j) N[j] = '9';
				break;
			}
		}
		leading0 = N.rfind('0');
		cout << "Case #" << t << ": ";
		if (leading0 == string::npos) cout << N << endl;
		else cout << N.substr(leading0 + 1) << endl;
	}
}
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

string find_tidy_number(string N) {
	if (N.length() == 1) {
		return N;
	}
	vector<int> Num;
	for (int i = 0; i < N.length(); i++) {
		Num.push_back(int(N[i] - '0'));
	}
	vector<int> newNum = Num;
	while (true) {
		newNum = Num;	
		sort(newNum.begin(), newNum.end());
		if (Num == newNum) {
			string result = "";
			while (true) {
				if (Num[0] == 0 and Num.size() > 1) {
					Num.erase(Num.begin(), Num.begin()+1);
				} else {
					break;
				}
			}
			for (int i = 0; i < Num.size(); i++) {
				result += to_string(Num[i]);
			}
			return result;
		}
		for (int i = Num.size()-1; i >= 0; i--) {
			if (Num[i] == 0 and i-1 >= 0) {
				Num[i] = 9;
			} else {
				Num[i] -= 1;
				break;	
			}
		}
	}
	
	for (int i = 0; i < N.length(); i++) {
		int j = N.length() - 1 - i;
		if (int(N[i]) > int(N[i+1]) || int(N[j]) < int(N[j-1])) {
			N = to_string(stoi(N) - 1);
		}	
		if (i >= j) {
			break;
		}
	}
	return N;
}

int main() {
	int T;
	string N;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> N;
		string output = find_tidy_number(N);
		cout << "Case #" << i << ": " << output << endl;
	}
	return 1;
}

#include<cstring>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

string e, digits;
int n, m;

vector<char> solve(string digit) {
	vector<char> temp;
	const char* dig = digit.c_str();
	int count = 1;
	if (digit.length() >= 2) {
		for (int i = 0; i < digit.length() - 1; i++) {
			if (dig[i] <= dig[i + 1]) {
				temp.push_back(dig[i]);
			}
			else { 
				temp.push_back(dig[i] - 1);
				string str(temp.begin(), temp.end());
				if (dig[i] - 1 < dig[i - 1]) temp = solve(str);
				count = i + 1;
				break; 
			}
			count = i + 1;
		}
		if (count == digit.length() - 1 && dig[count - 1] <= dig[count]) {
			temp.push_back(dig[count]);
			count++;
		}
		for (int j = count; j < digit.length(); j++)
			temp.push_back('9');
		return temp;
	}
	else { 
		temp.push_back(digit[0]);
		return temp; 
	}

}

int main() { 
	int cases;
	cin >> cases;
	for (int cc = 1; cc <= cases; ++cc) {
		cin >> digits;
		vector<char> sol = solve(digits);
		cout << "Case #" << cc << ": ";
		for (int i = 0; i < sol.size(); i++) {
			if (i == 0 && sol[i] == '0') continue;
			cout << sol[i];
		}
		cout << endl;
	}
	system("PAUSE");
	return 0;
}


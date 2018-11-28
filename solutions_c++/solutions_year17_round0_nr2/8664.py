#include <iostream>
#include <string>
#include <vector>

using namespace std;

string calcTidy(string &str);


int charToInt(char a)
{
	int i = a - '0';
	return i;
}

int main() {
	int T;
	cin >> T;
	string tmp;
	vector<string> num;
	for (int i = 0; i < T; i++) {
		cin >> tmp;
		num.push_back(tmp);
	}
	for (int i = 0; i < T; i++)
	{
		
		cout << "Case #" << i + 1 << ": " << calcTidy(num[i]) << endl;
	}
	return 0;
}

string calcTidy(string &str) {
	int i = str.length() - 1;
	int j = i - 1;
	while (i > 0) {
		if (str[i] < str[j]) {
			str[i] = '9';
			int tmp = str[j];
			if (tmp == 0) {
				tmp = 9;
			}
			else tmp--;
			str[j] = tmp;
		}
		i--; j--;
	}
	i = str.length() - 1;
	j = i - 1;
	for (int k = 0; k < str.length(); k++)
	{
		i = str.length() - 1;
		j = i - 1;
		while (i > 0) {
			if (str[i] < str[j]) {
				str[i] = '9';
			}
			i--; j--;
		}
	}
	if (str[0] == '0') {
		str.erase(0, 1);
	}
	
	
	return str;
}

#include<iostream>
#include<algorithm>
#include<math.h>
#include<string>
#include<string.h>
#include<cstdio>
using namespace std;
int stringtoint(const char ca[]) {
	int num = 0;
	int stlen = strlen(ca);
	for (int i = 0; i < stlen; i++) {
		num *= 10;
		num += ca[i] - '0';
	}
	return num;
}
int main() {
	int NoOfTestCases;
	cin >> NoOfTestCases;
	cin.clear();
	cin.ignore();
	for (int j = 0; j < NoOfTestCases; j++) {
		bool flag = true;
		string st;
		getline(std::cin, st);
		int delim = st.find(' ');
		string token = st.substr(0, delim);
		int stlen = strlen(st.c_str()), toklen = strlen(token.c_str());
		int size = stringtoint(st.substr(delim+1, stlen).c_str()), count = 0;
		for (int i = 0; i < toklen - size + 1; i++) {
			if (token[i] == '-') {
				count += 1;
				for (int k = i; k < i + size; k++)
					if (token[k] == '+')
						token[k] = '-';
					else
						token[k] = '+';
			}
		}
		for (int i = 0; i < toklen; i++)
			if (token[i] == '-') {
				flag = false; break;
			}
		if (flag) cout << "Case #" << j + 1 << ": " << count << endl;
		else cout << "Case #" << j + 1 << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
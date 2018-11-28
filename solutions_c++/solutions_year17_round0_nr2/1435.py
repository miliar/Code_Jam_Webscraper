#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <string.h>
#include <stack>
#include <list>

#define IMAX 1234567890

long long arr[19];

using namespace std;

int main(int argc, const char * argv[]) {
	int t_c = 0;
	cin >> t_c;


	long long k = 0;
	for (long long i = 1; i <= 18; i++) arr[i] = k * 10LL + 1;

	for (int z = 1; z <= t_c; z++) {

		string s;
		cin >> s;

		stack<int> st;
		st.push(0);

		for (int i = 1; i < s.size(); i++) {
			if (s[i - 1] > s[i]) {
				int k = st.top(); st.pop();
				s[k] = s[k] - 1;
				for (int j = k + 1; j < s.size(); j++) {
					s[j] = '9';
				}
				break;
			}
			else if (s[i - 1] < s[i]) {
				st.push(i);
			}
		}

		cout << "Case #" << z << ": ";
		//if (s[0] == '0') cout << s.substr(1, s.size()) << endl;
		//else cout << s << endl;
		cout << to_string(stoll(s)) << endl;
	}
	return 0;
}
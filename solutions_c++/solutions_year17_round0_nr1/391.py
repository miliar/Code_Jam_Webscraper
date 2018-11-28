#include<iostream>
#include<string>
#include <sstream>
using namespace std;

string remove(string A) {
	int p = 0;
	while (p < A.length() && A.at(p) == '+') {
		p++;
	}
	return A.substr(p);
}


string turnon(string T, int k) {
	string s;
	for (int i = 0; i < k; i++) {
		char c = T.at(i) == '+' ? '-' : '+';
		s += c;
	}
	s += T.substr(k);
	return s;
}

string find(string A, int k) {
	
	int count = 0;
	string tmp = A;	
	while (!tmp.empty() && tmp.length() >= k) {
		tmp = remove(tmp);
		if (tmp.length() >= k) {			
			tmp = turnon(tmp, k);	
			count++;
		}		
	}		
	return tmp.empty() ? to_string(count) : "IMPOSSIBLE";	
}
int main()
{
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++)
	{
		string str;
		int K;
		cin >> str >> K;
		cout << "Case " << "#" << tc << ":" << " ";
		string out = find(str, K);
		cout << out << endl;
	}
	return 0;
}

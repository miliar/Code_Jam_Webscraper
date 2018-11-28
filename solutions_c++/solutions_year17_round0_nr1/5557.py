#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

map<string, bool> mark;
vector<string> panQ;
vector<int> lenQ;


bool isGood(string s){
	for (int i = 0; i < s.size(); ++i)
		if(s[i] != '+')
			return false;
	return true;
}

string flip(string s, int n, int start) {
	string result = s;
	// cerr << s << " " << n << " " << start << endl;
	for (int i = start; i < n+start; ++i){
		if (s[i] == '-')
			result[i] = '+';
		else
			result[i] = '-';
	}
	// cerr << "s is " << result << endl;
	return result;
}

int solve(int n){

	for (int i = 0; i < panQ.size(); ++i)
	{
		string s = panQ[i];
		int len = lenQ[i];
		mark[s] = true;
		// cerr << "checking " << s << "    len : " << n << endl;

		if (isGood(s))
			return len;
		for (int k = 0; k <= s.size() - n; ++k)
		{
			string fliped = flip(s, n, k);
			// cerr << "generated flip " << fliped << endl;
			if (!mark[fliped]) {
				mark[fliped] = true;
				panQ.push_back(fliped);
				lenQ.push_back(len+1);
			}
		}
	}


	return -1;
}

int main(){
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		string start;
		int n;
		cin >> start >> n;
		panQ.clear();
		lenQ.clear();
		mark.clear();
		lenQ.push_back(0);
		panQ.push_back(start);

		int result = solve(n);

		cout << "Case #" << test+1 << ": ";
		if (result == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << result << endl;
	}
}
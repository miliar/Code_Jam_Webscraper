#include <iostream>
#include <map>
#include <string>
#include <algorithm>
#include <vector>



using namespace std;


vector<string> p;
vector<int> l;
map<string, bool> mark;



string flip(string s, int n, int begin) {
	string res = s;
	for (int i = begin; i < n+begin; ++i){
		if (s[i] == '-'){
			res[i] = '+';
		}
		else{
			res[i] = '-';
		}
	}
	return res;
}

bool check(string s){
	for (int i = 0; i < s.size(); ++i)
		if(s[i] != '+')
			return false;
	return true;
}


int solve(int n){

	for (int i = 0; i < p.size(); ++i)
	{
		string s = p[i];
		int len = l[i];
		mark[s] = true;

		if (check(s))
			return len;
		for (int k = 0; k <= s.size() - n; ++k)
		{
			string fliped = flip(s, n, k);
			if (!mark[fliped]) {
				mark[fliped] = true;
				p.push_back(fliped);
				l.push_back(len+1);
			}
		}
	}


	return -1;
}

int main(){
	int test;
	cin >> test;
	int c=1;
	while (test--)
	{
		string begin;
		int n;
		cin >> begin >> n;
		p.clear();
		l.clear();
		mark.clear();
		l.push_back(0);
		p.push_back(begin);

		int res = solve(n);

		cout << "Case #" << c++ << ": ";
		if (res == -1){
			cout << "IMPOSSIBLE" << endl;
		}
		else{
			cout << res << endl;
		}
	}
	return 0;

}
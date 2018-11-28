#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int helper(string &s, int start, int n){
	if(n > s.length())
		return -1;
	if(start == s.length() - n){
		int i = start + 1;
		for(; i < s.length() && s[i] == s[start]; ++i);
		if(i != s.length())
			return -1;
		return s[start] == '+'? 0 : 1;
	}
	int cnt = 0;
	if(s[start] == '-'){
		for(int j = start+1; j < start + n; ++j){
			s[j] = s[j] == '+'?'-':'+';
			cnt = 1;
		}
	}
	int tail =  helper(s, start + 1, n);
	if(tail == -1)
		return -1;
	return tail + cnt;
}

int main(){
	ifstream fin("A-small-attempt0.in", std::ifstream::in);
	ofstream fout("1.out", std::ifstream::out);
	int t;
	fin >> t;
	for(size_t i = 0; i < t; ++i){
		cout<<i<<endl;
		string s;
		int n;
		fin>>s;
		fin>>n;
		cout<<s<<endl;
		cout<<n<<endl;
		int result = helper(s, 0, n);
		if(result == -1)
			fout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
		else
			fout<<"Case #"<<i+1<<": "<<result<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

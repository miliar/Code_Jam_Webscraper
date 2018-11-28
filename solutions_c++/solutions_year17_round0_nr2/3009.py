#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>

using namespace std;


string str;

vector<string> v;

void gera(string str, int idx){
	v.push_back(str);
	if(str.length() == 18) return ;

	for(int i = idx; i < 10; i++){
		gera(str + to_string(i), i);
	}

}

bool func(const string &a, const string &b){
	if(a.length() == b.length()) return a < b;

	return a.length() < b.length();
}

int main(){

	int t;

	gera("", 1);	

	sort(v.begin(), v.end(), func);
	scanf("%d", &t);
	int caso = 1;
	while(t--){
		cin >> str;
		int idx = lower_bound(v.begin(), v.end(), str, func) - v.begin();

		if(v[idx] == str && idx < v.size())
			printf("Case #%d: %s\n", caso, v[idx].c_str());
		else printf("Case #%d: %s\n", caso, v[idx-1].c_str());
		caso++;
	}
	

	
	return 0;
}
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <unordered_map>
#include <unordered_set>

using namespace std;
typedef long long ll;

bool check(string a, string b){
	stringstream out;
	out<<a<<" "<<b;
	ll aa, bb;
	out>>aa>>bb;
	return aa <= bb;
}

string fill(string ans, int ind, char numb){
	for(int i=ind; i<ans.size(); i++){
		ans[i] = numb;
	}
	return ans;
}

string func(string str){
	int k = str.size();
	if(k == 1){
		return str;
	}
	string ans = string(k, '1');
	if(!check(ans, str)){
		return string(k-1, '9');
	}

	ans = string(k, '9');
	for(int i=0; i<str.size(); i++){
		for(int j=9; j>=1; j--){
			char ch = j + '0';
			if(i != 0){
				if(str[i-1] > ch){
					break;
				}
			}
			ans = fill(ans, i, ch);
			if(check(ans, str)){
				break;
			}
		}
	}
	return ans;
}

int main(){

#ifdef _CONSOLE
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int countTest;
	cin>>countTest;	
	for(int test = 1; test <= countTest; test++){
		string str;
		cin>>str;

		string ans = func(str);

		printf("Case #%d: %s\n", test, ans.c_str());

		cerr<<test<<"\n";
	}
	
	return 0;
}


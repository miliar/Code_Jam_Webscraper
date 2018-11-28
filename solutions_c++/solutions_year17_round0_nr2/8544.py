#include<iostream>
#include<queue>
#include<vector>
#include<cmath>
#include<string>
using namespace std;
long long sToLL(const string& s){
	long long ret = 0;
	for (int i = 0; i < s.size(); ++ i){
		ret = ret * 10 + s[i] - '0';
	}
	return ret;
}
int main(){
	int t;
	string s;
	cin >> t;
	for (int z = 1; z <= t; ++ z){
		cin >> s;
		for (int i = 0; i + 1 < s.size(); ++ i){
			if (s[i+1] < s[i]){
				for (int j = i; j >= 0; -- j){
					if (s[j] == '0') s[j] = '9';
					else{
						s[j] --;
						if (j == 0 || s[j] >= s[j-1])
							break;
						s[j] = '9';
					}
				}
				for (int j = i + 1; j < s.size(); ++ j){
					s[j] = '9';
				}
				break;
			}
		}
		cout << "Case #" << z << ": " << sToLL(s) << endl;
	}
	return 0;
}
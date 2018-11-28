#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
using namespace std;

int main(){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w+", stdout);
	int T; cin>>T;
	for (int t = 0; t < T; t++){
		string s; cin>>s;
		string res = "";
		string secure = "";
		for (int x = 0; x < s.size(); x++){
			int act = s[x] - '0';
			int next = s[x+1]-'0';
			if (x == s.size()-1){
				res += s[x];
				break;
			}
			if (x == 0 || (s[x]-'0') - 1 >= (s[x-1]-'0')){
				char m = s[x] - 1;
				secure = res + m;
				for (int y = 0; y < s.size() - x - 1; y++){
					secure += "9";
				}
			}
			if (next < act){
				res = secure;
				break;
			}else{
				res += s[x];
			}
		}
		long long r = 0;
		for (int x = 0; x < res.size(); x++){
			r *= 10LL;
			r += res[x] - '0';
		}
		cout << "Case #" << t+1 << ": " << r << endl;
	}
}
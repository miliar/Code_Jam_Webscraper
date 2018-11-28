#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;


int main(){
	int T;
	cin >> T;
	for(int tc=1; tc <= T; ++tc){
		string s;
		cin >> s;
		for(int i=(int)s.size()-2; i >= 0; --i){
			if(s[i+1] < s[i]){
				--s[i];
				for(int j=i+1; j<s.size(); ++j){
					s[j] = '9';
				}
			}
		}
		long long l = 33;
		istringstream(s) >> l;

		cout << "Case #" << tc << ": " << l << endl;
	}
}
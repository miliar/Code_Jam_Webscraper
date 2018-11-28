#include <iostream>
#include <vector>
#include <sstream>
#include <utility>
#include <set>
#include <queue>
#include <fstream>

using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");
#define cout fout
#define cin fin

int main(){
	int t;
	cin >> t;
	for(int o = 0 ; o < t ; ++o){
		string s;
		int k;
		cin >> s >> k;
		bool flag = true;
		int ans = 0;
		for(int i = 0 ; i < s.size() ; ++i){
			if(s[i] == '-'){
				++ans;
				if(i + k > s.size()){
					flag = false;
					break;
				}
				for(int j = i ; j < i + k ; ++j){
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}

		cout << "Case #" << o + 1 << ": ";

		if(flag) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
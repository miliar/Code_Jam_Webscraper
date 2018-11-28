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
		cin >> s;

		bool flag = true;
		while(flag){
			flag = false;
			for(int i = 0 ; i < s.size() - 1 ; ++i){
				if(s[i] > s[i + 1]){
					flag = true;
					if(s[i] > 0){
						s[i] = (char)(s[i] - 1);
						for(int j = i + 1 ; j < s.size() ; ++j) s[j] = '9';
						break;
					}
				}
			}
		}
		cout << "Case #" << o + 1 << ": ";
		int ii = 0;
		while(s[ii] == '0') ++ii;
		for(int i = ii ; i < s.size() ; ++i) cout << s[i];
		cout << endl;
	}

	return 0;
}
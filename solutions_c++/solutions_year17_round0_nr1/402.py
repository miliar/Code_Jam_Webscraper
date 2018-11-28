#include <iostream>
#include <fstream>
#include <string>
#include <set>

using namespace std;

//#define ifs cin
//#define ofs cout
ifstream ifs("A-large.in");ofstream ofs("1.out");
//ifstream ifs("B-large-practice.in");ofstream ofs("2.out");

void solve(int time){
	string str;
	ifs >> str;
	int k;
	ifs >> k;
	int ans = 0;
	for(int i = 0;i < str.length()-k+1;i++){
		if(str[i] == '-'){
			for(int j = i;j < i+k;j++){
				if(str[j] == '-')str[j] = '+';
				else str[j] = '-';
			}
			ans++;
		}
	}
	for(int i = 0;i < str.length();i++){
		if(str[i] == '-'){
			ofs << "Case #" << time << ": IMPOSSIBLE" << endl;
			return;
		}
	}
	ofs << "Case #" << time << ": " << ans << endl;
}

int main() {
	int t;
	ifs >> t;
	cout << "start" << endl;
	for(int i = 1;i <= t;i++){
		solve(i);
	}
	cout << "fin" << endl;
	return 0;
}

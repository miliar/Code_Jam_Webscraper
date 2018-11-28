#include <iostream>
#include <fstream>
#include <string>
#include <set>

using namespace std;

//#define ifs cin
//#define ofs cout
//ifstream ifs("B-small-attempt0.in");ofstream ofs("1.out");
ifstream ifs("B-large.in");ofstream ofs("2.out");

void solve(int time){
	long long ans = 99999999999999999;
	ifs >> ans;
	for(long long i = 1;i < ans;i*=10){
		long long t = ans/i%10;
		long long o = ans/i/10%10;
		if(t < o){
			ans -= ans%(i*10)+1;
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

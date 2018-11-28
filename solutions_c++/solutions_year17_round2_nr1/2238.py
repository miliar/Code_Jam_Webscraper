//Irvin Gonzalez


#include <iostream>
#include <string>

using namespace std;
void solve() {
	long des;
	int n;
	cin >> des >> n;
	double time = 0;
	for(int i = 0; i < n; ++i) {
		long pos;
		long sp;
		cin >> pos >> sp;
		double curtime = (double)(des - pos)/sp;
		if(curtime > time)
			time = curtime; }
	cout << fixed << (des/time);
	
}
int main() {

	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl; }
	return 0;
}

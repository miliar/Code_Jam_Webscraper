#include <cfloat>
#include <climits>
#include <cmath>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

typedef unsigned long long ulint;
typedef long long lint;
typedef long double lubb;

lubb run(ulint DEST, ulint NUM, const vector<ulint>& START, const vector<ulint>& SPEED) 
{
	lubb slowtime = 0.0;
	for (ulint i = 0; i < NUM; i++) {
		ulint dist = DEST - START[i];
		lubb dtime = ((long double) dist / (long double) SPEED[i]);
		slowtime = (slowtime > dtime) ? slowtime : dtime;
	}
	lubb newspeed = ((long double) DEST / slowtime);
	return newspeed;
}

void test() {
	ulint D, N;
	cin >> D >> N;

	vector<ulint> START(N);
	vector<ulint> SPEED(N);

	for (ulint i = 0; i < N; i++) {
		cin >> START[i] >> SPEED[i];
	}

	lubb result = run(D, N, START, SPEED);
	
	cout.precision(10);
	cout << fixed;
	//cout << (int)result << ' ';
	cout << result;// << ' ' << result << ' ' << result << ' ';
}	

int main() {
	unsigned long T;
	cin >> T;
	for(unsigned long i = 1; i<=T; i++) {
		cout << "Case #" << i << ": ";
		test();	
		cout << endl;
	}
	return 0;
}

#include <iostream>
#include <string>
using namespace std;
bool isTidy(string &s)
{
	int len(s.length());
	char val(s[0]);
//	int dnum(0),maxdnum(0);
	for (int n(0); n<len; ++n) {
		if (s[n] > val) {
//			if ((maxdnum)&&(maxdnum != dnum))
//				return false;
//			if (dnum) {
//				if (!maxdnum){
//					maxdnum = dnum;
//				}
//				dnum = 0;
//			}
//			++dnum;
			val = s[n];
		}
		else if (s[n] == val) {
//			++dnum;
//			if ((maxdnum) && (dnum>maxdnum))
//				return false;
		}
		else {
			return false;
		}
	}
//	if ((maxdnum) && (maxdnum != dnum))
//		return false;
	return true;
}
string solve(string &s) {
	int len(s.length());
	if (isTidy(s))
		return s;
	for (__int64 val(stoull(s));;){
		--val;
		string ss(to_string(val));
		if (isTidy(ss))
			return ss;
	}
	return "SAMUP!";
}
int main() {
	int T;
	cin >> T;
	for (int cas(1); cas <= T; ++cas) {
		string s;
		cin >> s;
		cout << "Case #" << cas << ": " << solve(s) << endl;
	}
	return 0;
}

#include <iostream>
#include <string>
#include <queue>
#include <fstream>
#include <algorithm>
#include <map>
using namespace std;


map<string, int> vis;

string solve(string a) {
	vector<int> fine;
	fine.assign(30, 1);
	for (int i = 1; i < a.size(); ++i) {
		fine[i] = fine[i - 1] && (a[i - 1] <= a[i]);
	}
	int s = -1;
	for (int i = a.size()-1; i >=0; --i) {
		if (fine[i] && ((i == 0 && a[0] != '1') ||(i!=0&& a[i] > a[i - 1]))) {
			s = i;
			break;
		}
	}
	if (s == -1) {
		return string("").assign(a.size() - 1, '9');
	}

	a[s]--;
	
	for (int i = s+1; i < a.size(); ++i) {
		a[i] = '9';
	}

	return a;
}

bool isTidy(string a) {

	for (int i = 1; i < a.size(); ++i) {
		if (a[i] < a[i - 1])
			return false;
	}

	return true;
}

int main() {
	ifstream in("test.in");
	ofstream out("test.out");
	int n;
	in >> n;

	for (int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ": ";

		out << "Case #" << i << ": ";
		
		string a;
		in >> a;
		if (isTidy(a))
		{

			cout << a;
			out << a;
		}
		else {
			cout << solve(a);
			out << solve(a);

		}

		
		out << endl;
		cout << endl;
	}
	
	return 0;
}
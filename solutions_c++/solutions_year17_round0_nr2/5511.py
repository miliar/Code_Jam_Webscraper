#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int t;
void findLastTidyNumber(string n, ofstream& out);

int main() {
	ios_base::sync_with_stdio(false);
	
	ifstream in("input.in");
	ofstream out("output.out");

	in >> t;
	for (int cnt = 1; cnt <= t; ++cnt) {
		string n;
		in >> n;
		out << "Case #" << cnt << ": ";
		findLastTidyNumber(n, out);
	}
	out << "\n";
	
	in.close(); out.close();
	return 0;
}

void findLastTidyNumber(string n, ofstream& out) {
	if (n.size() == 1) {
		out << n << "\n";
		return;
	}
	else {
		bool changes = true;
		while (changes) {
			changes = false;
			for (int i = 0; i != n.size() - 1; ++i) {
				if (n[i] > n[i + 1]) {
					changes = true;
					if (n[i] == 1) n[i] = '9';
					else --n[i];
					for (int j = i + 1; j != n.size(); ++j)
						n[j] = '9';
					break;
				}
			}
		}
		if (n[0] == '0') n.erase(n.begin());
		out << n << "\n";
	}
}
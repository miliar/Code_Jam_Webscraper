#include <fstream>
#include <vector>
#include <string>
using namespace std;
int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	string n;
	in >> t;
	for(int i=1;i<=t;i++) {
		in >> n;
		string m = n;
		string ans;
		int l = (int)n.size();
		for (int j=0;j<l;j++) m[j]='1';
		if (m > n) {
			ans = m;
			ans.erase(l-1,1);
			for (int j=0;j<l-1;j++) ans[j] = '9';
		} else {
			ans = n;
			for (int k=0;k<l;k++) {
				for (int j=1;j<l;j++) {
					if (ans[j] < ans[j-1]) {
						ans[j-1]--;
						for (int k=j;k<l;k++) ans[k] = '9';
					}
				}
			}
		}
		out << "Case #" << i << ": " << ans << "\n";
	}
	return 0;
}


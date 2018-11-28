#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve(int n, int p, vector<int>& g, int T, ofstream& out) {
	out << "Case #" << T << ": ";
	int ans = 0;
	map<int, int> m;
	for (int i=0; i<p; ++i)
		m[i]=0;
	for (int i=0; i<n; ++i) {
		g[i]=g[i]%p;
		if (g[i]==0) {
			++ans;
		} else if (m[p-g[i]]>0) {
			++ans;
			--m[p-g[i]];
		} else {
			++m[g[i]];
		}
	}
	if (p==2)
		ans+=(m[1]+1)/2;
	else if (p==3)
		ans+=(m[1]+m[2]+2)/3;
	else if (p==4) {
		if (m[1]==0 && m[2]==0 && m[3]!=0)
			ans+=(m[3]+3)/4;
		else if (m[1]!=0 && m[2]==0 && m[3]==0)
			ans+=(m[1]+3)/4;
		else if (m[1]==0 && m[2]!=0 && m[3]==0)
			++ans;
		else if (m[1]!=0 && m[2]!=0)
		{
			if (m[1]>=2) {
				ans+=(m[1]-2+3)/4;
			}
			++ans;
		}
		else if (m[3]!=0 && m[2]!=0)
		{
			if (m[3]>=2) {
				ans+=(m[3]-2+3)/4;
			}
			++ans;
		}
	}
	out << ans << "\n";
}

int main() {
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int T, i = 1;
	in >> T;
	while (T--) {
		int n, p;
		in >> n >> p;
		vector<int> g(n);
		for (int j = 0; j < n; ++j) {
			in >> g[j];
		}
		solve(n, p, g, i, out);
		++i;
	}
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

int main(int argc, char** argv) {

	ifstream in("../data/a_large.in");
	ofstream out("../data/a_large.out");

	int T;  // cases
	in >> T;

	for (int z = 1; z <= T; z++) {

		string s;
		int k;
		in >> s >> k;

		int l = s.length();
		bool happy[l];
		for (int i = 0; i < l; i++)
			happy[i] = (s[i] == '+');

		bool possible = true;
		int res = 0;

		for (int i = 0; i <= l - k; i++) {
			if (happy[i])
				continue;
			else {
				res++;
				for (int j = 0; j < k; j++)
					happy[i + j] = !happy[i + j];
			}
		}
		for (int i = l - k + 1; i < l && possible; i++)
			if (!happy[i])
				possible = false;

		out << "Case #" << z << ": ";
		// print the result
		if (!possible)
			out << "IMPOSSIBLE";
		else
			out << res;

		out << endl;

	}

	in.close();
	out.close();
	
	return 0;
}
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char** argv) {

	ifstream in("../data/b_large.in");
	ofstream out("../data/b_large.out");

	int T;  // cases
	in >> T;
	for (int z = 1; z <= T; z++) {

		long long n;
		in >> n;

		stack<int> res;
		while (n > 0) {
			int lastDigit = n % 10;
			n /= 10;
			int prevLastDigit = n % 10;
			if (lastDigit < prevLastDigit) {
				int t = res.size() + 1;
				while (!res.empty()) 
					res.pop();
				for (int j = 0; j < t; j++)
					res.push(9);
				n--;
			}
			else
				res.push(lastDigit);
		}

		out << "Case #" << z << ": ";
		// print the result
		while (!res.empty()) {
			out << res.top();
			res.pop();
		}

		out << endl;

	}

	in.close();
	out.close();
	
	return 0;
}
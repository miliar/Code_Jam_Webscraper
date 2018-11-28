#include <fstream>
#include <string>
#include <cstring>
using namespace std;
ifstream in;
ofstream out;

int main()
{
	in.open("input.txt");
	out.open("output.txt");
	int T, K;
	string s;
	in >> T;
	for (int i = 0; i < T; ++i){
		bool b[1100]{};
		in >> s;
		int j;
		for (j = 0; j < s.length(); ++j){
			switch(s[j]){
			case '+':b[j] = true; break;
			}
		}

		in >> K;
		int t = 0, sum=0;
		for (t; t < (j - K+1); ++t){
			if (!b[t]){
				for (int n = t; n - t < K; ++n){
					b[n] = !b[n];
				}
				++sum;
			}
		}
		bool check=true;
		for (int m = 0; m < j; ++m){
			if (!b[m]){
				check = false;
				out << "Case #" << i+1 << ": " << "IMPOSSIBLE\n";
				break;
			}
		}
		if (check){
			out << "Case #" << i+1 << ": " << sum<<"\n";
		}
	}
	in.close();
	out.close();
	return 0;
}
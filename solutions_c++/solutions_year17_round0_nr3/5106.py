#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("C-small-2-attempt0.in");
	fout.open("coutsmall22222.txt");
	int t;
	fin >> t;
	for (int ti = 1; ti <= t; ti++)
	{
		long long k, n, ans;
		fin >> n >> k;
		int logmin = log2(k);
		long long a = pow(2, logmin);
		long long dijige = k - a + 1;
		long long b = n - (a - 1);
		long long c = b / a;
		long long d = b%a;
		ans = c;
		if (dijige <= d)
			ans++;
		fout << "Case #" << ti << ": " << ans / 2 << " " << (ans - 1) / 2 << endl;
	}
}
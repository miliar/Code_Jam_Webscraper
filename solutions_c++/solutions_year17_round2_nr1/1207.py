#include<bits/stdc++.h>
using namespace std;
# define ll long long
# define mod 1000000007
# define MAX 1011
# define anotherMax 11
# define INF 1e16
ll ar[MAX];
int main()
{
	ifstream in("file/a.txt");
	ofstream out("file/b.txt");
	in.sync_with_stdio(false);
	int t, var = 0;
	in >> t;
	while(t--)
	{
		var++;
		out << "Case #" << var << ": ";
		double d, k, s;
		int n, i;
		in >> d >> n;
		auto timeTaken = 0.0;
		while(n--)
		{
			in >> k >> s;
			timeTaken = max(timeTaken, static_cast<double>((d - k) / s));
		}
		out <<fixed<< setprecision(6) << (d / timeTaken) << '\n';
	}
	return 0;
}
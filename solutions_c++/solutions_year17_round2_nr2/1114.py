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
		int n, r, b, y, o, g, v;
		in >> n >> r >> o >> y >> g >> b >> v;
		if (r + y + b == n)
		{
			char ch[3];
			pair <int, char> pp[3];
			pp[0] = make_pair(r, 'R');
			pp[1] = make_pair(y, 'Y');
			pp[2] = make_pair(b, 'B');
			sort(pp, pp + 3);
			for (auto i = 0; i < 3; i++)
				ch[i] = pp[i].second;
			if (pp[2].first > pp[0].first + pp[1].first)
				out << "IMPOSSIBLE\n";
			else
			{
				vector <int> ans;
				int br[3];
				for (auto i = 0; i < 3; i++)
					br[i] = pp[i].first;
				auto temp = br[1] - (br[2] - br[0]);
				while (temp--)
					ans.push_back(2), ans.push_back(1), ans.push_back(0);
				temp = br[0] - (br[1] - (br[2] - br[0]));
				while (temp--)
					ans.push_back(2), ans.push_back(0);
				temp = br[2] - br[0];
				while (temp--)
					ans.push_back(2), ans.push_back(1);
				for (auto i = 0; i < n; i++)
					out << ch[ans[i]];
				out << '\n';
			}
		}
		else
			out << "IMPOSSIBLE\n";
	}
	return 0;
}
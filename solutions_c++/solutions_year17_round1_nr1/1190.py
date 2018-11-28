#include <bits/stdc++.h>

using namespace std;

const int maxx = 30;

string s[maxx], soal;
char c[maxx][maxx];
int n, t, m;
vector<int> v;

int main()
{
	ifstream in;	in.open("tt.txt");	ofstream out;	out.open("ans.out");
	in >> t;
	for(int u = 1; u <= t; u++)
	{
		out << "Case #" << u << ": " << endl ;
		v.clear();
		in >> n >> m;
		soal = ""; for(int i = 0; i < m; i++) soal += "?";
		for(int i = 0; i < n; i++) s[i] = "";
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				in >> c[i][j];
				s[i] += c[i][j];
			}
		}
		for(int i = 0; i < n; i++)
		{
			if (s[i] == soal) continue;
			v.push_back(i);
			int p = 0;
			while (s[i][p] == '?') p++;
			for(int j = 0; j < p; j++) s[i][j] = s[i][p];
			char gh = s[i][p];
			for(int j = p + 1; j < m; j++)
				if (s[i][j] == '?')
					s[i][j] = gh;
				else
					gh = s[i][j];
		}
		v.push_back(n);
		for(int i = 0; i < v[0]; i++)
			s[i] = s[v[0]];
		for(int i = 0; i + 1 < v.size(); i++)
			for(int j = v[i] + 1; j < v[i + 1]; j++)
				s[j] = s[v[i]];
		//
		for(int i = 0; i < n; i++)
			out << s[i] << endl;
	}
	return 0;
}

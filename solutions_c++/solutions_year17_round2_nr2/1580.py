#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <map>

#include <iostream>
#include <sstream>

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)


bool submit = true;

// ---------------------------------------------------
// ---------------------------------------------------


vector<char> colors{'R', 'O', 'Y', 'G', 'B', 'V'};
vector<int> ryb = {0, 2, 4};
void printv(vector<int> v)
{
	for(auto n : v)
		printf("%d ", n);
	cout << endl;
}
void printvc(vector<char> v)
{
	for(auto c : v)
		printf("%c ", c);
	cout << endl;
}

bool comp(string a, string b)
{
	return a.size() > b.size();
}

string util(vector<int> v, int N)
{
	int mx = 0;
	map<char, int> m;
	for (int i = 0; i < v.size(); ++i) 
	{	
		mx = max(mx, v[i]);
		m[colors[i]] += v[i];
	}
	if (mx*2 > N) return "IMPOSSIBLE";
	
	vector<string> vstring;
	for (auto i : m)
		vstring.push_back(string(i.second, i.first));
		sort(vstring.begin(), vstring.end(), comp);

	vector<char> vc;
	for (auto s : vstring)
		for (int i = 0; i < s.size(); ++i)
			vc.push_back(s[i]);

	// printvc(vc);

	string out(N, '_');

	for (int i = 0; i < N; i++)
	{
		if (2*i < N)
			out[i*2] = vc[i];
		else
			if (N%2==0)
				out[i*2 - N + 1] = vc[i];
			else
				out[i*2 - N] = vc[i];
	}

	return out;
}

int main()
 {
	if (submit)
	{
		freopen("B-small-attempt1.in", "r", stdin);
		freopen("B-small-attempt1.out", "w", stdout);
		
		// freopen("B-large.in", "r", stdin);
		// freopen("B-large.out", "w", stdout);

		int tt, tn; // loop var and total test cases
		cin >> tn;

		F1(tt,tn) 
		{
			int N; cin >> N;
			vector<int> v(6, 0);
			F0(i, 6) 
			{
				cin >> v[i];
			}

			string s = util(v, N);
			printf("Case #%d: %s\n", tt, s.c_str());
		}
	}
	else // go dev
	{

	}

	return 0;
}

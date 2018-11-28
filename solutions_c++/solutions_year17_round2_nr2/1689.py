#include <bits/stdc++.h>
#define x first
#define y second
using namespace std;
typedef long long ll;
const int MAXN = 100500;

string sol(int R, int Y, int B)
{
	int n = R + Y + B;
	string s;
	vector <pair <int, int> > kek;
	kek.push_back({R, 'R'});
	kek.push_back({Y, 'Y'});
	kek.push_back({B, 'B'});
	sort(kek.begin(), kek.end());

	for (int i = 0; i < n; i++)
	{
		s += '-';
	}

	int ptr = 0;
	int ind = 0;

	while (ind < 3)
	{
		if (kek[ind].first == 0)
			ind++;
		else
		{
			kek[ind].first--;
			s[ptr] = kek[ind].second;
			ptr += 2;
			if (ptr >= n)
				ptr = 1;
		}
	}

	bool ok = s[0] != s.back();
	for (int i = 0; i < n - 1; i++)
		ok &= s[i] != s[i + 1];

	if (!ok)
		s = "IMPOSSIBLE";

	return s;
}

void sol()
{
	int n, R, O, Y, G, B, V;
	cin >> n >> R >> O >> Y >> G >> B >> V;
	
	string s = sol(R, Y, B);
	
	if (s == "IMPOSSIBLE")
	{
		cout << s << '\n';
		return;
	}

	cout << s << '\n';

}

int main()
{                                                     
	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		sol();
	}
	
	
	return 0;
}


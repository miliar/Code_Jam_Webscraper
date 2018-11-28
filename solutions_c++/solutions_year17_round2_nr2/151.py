#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <string>
#include <cstdio>
#include <vector>
#include <deque>
#include <cmath>
#include <list>
#include <set>
#include <map>
#define rep(i,m,n) for(int i=(m),_end=(n);i < _end;++i)
#define repe(i,m,n) for(int i=(m), _end =(n);i <= _end;++i)
typedef long long ll;
using namespace std;



string alternate(int n, char Mc, char Oc)
{
	string s(n, Oc);
	for (int i = 1; i < n; i += 2)
	{
		s[i] = Mc;
	}
	return s;
}


void fill(string &s, char f, int c)
{
	for (int i = 0; i < s.size() && c>0; i++)
	{
		if (s[i] == 'x')
		{
			s[i] = f;
			i++;
			c--;
		}
	}
}

void sol(ifstream& sr, ofstream& sw) {
	int N, R, O, Y, G, B, V;

	sr >> N >> R >> O >> Y >> G >> B >> V;

	R -= G;
	B -= O;
	Y -= V;
	if (R == 0 && G * 2 == N)
	{
		sw << alternate(N, 'G', 'R');
		return;
	}
	if (B == 0 && O * 2 == N)
	{
		sw << alternate(N, 'O', 'B');
		return;
	}
	if (Y == 0 && V * 2 == N)
	{
		sw << alternate(N, 'V', 'Y');
		return;
	}
	
	if (R < 0 || B < 0 || Y < 0 || (G>0 && R == 0) || (O>0 && B == 0) || (V>0 && Y == 0))
	{
		sw << "IMPOSSIBLE";
		return;
	}

	int n = R + Y + B;

	if (R * 2 > n || Y * 2 > n || B * 2 > n)
	{
		sw << "IMPOSSIBLE";
		return;
	}

	string s(n, 'x');

	vector<pair<int, char>> v;
	v.push_back(make_pair(R, 'R'));
	v.push_back(make_pair(B, 'B'));
	v.push_back(make_pair(Y, 'Y'));
	std::sort(v.begin(), v.end());

	for (int i = 0; i < v[2].first; i++)
	{
		s[i * 2] = v[2].second;
	}
	int c = v[2].first * 2 - 1;
	while (c < n)
	{
		s[c] = v[c % 2].second;
		v[c % 2].first--;
		c++;
	}
	c = 1;
	while (v[1].first > 0)
	{
		s[c] = v[1].second;
		v[1].first--;
		c += 2;
	}
	while (v[0].first > 0)
	{
		s[c] = v[0].second;
		v[0].first--;
		c += 2;
	}

	if (G > 0)
	{
		s.insert(s.find("R"), alternate(G * 2, 'G', 'R'));
	}
	if (O > 0)
	{
		s.insert(s.find("B"), alternate(O * 2, 'O', 'B'));
	}
	if (V > 0)
	{
		s.insert(s.find("Y"), alternate(V * 2, 'V', 'Y'));
	}
	sw << s;
}

int main() {

	ifstream sr = ifstream("D:\\in.in");
	ofstream sw = ofstream("D:\\out.out");

	int T;
	sr >> T;
	for (int i = 0; i < T; i++)
	{
		sw << "Case #" << i + 1 << ": ";
		sol(sr, sw);
		sw << endl;
		cout << i << endl;
	}
	sr.close();
	sw.close();
	cout << "FINISHED type a number and enter to exit";
	cin >> T;

	return 0;
}

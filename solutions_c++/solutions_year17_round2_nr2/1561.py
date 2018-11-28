#pragma warning(disable : 4996) //_CRT_SECURE_NO_WARNINGS
#include <queue>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <set>
#include <deque>
#include <sstream>
#include <iomanip>
#define sync ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ss second
#define ff first
#define ll long long
#define mp make_pair
#define endl "\n"
#define pb push_back
#define ld long double
#define M_PI 3.14159265358979323846
#define puss vector
const ld EPS = 0.9;
const ll INF = 1000000007;
using namespace std;

int main() 
{
	freopen("in.in", "r", stdin);
	freopen("sol.out", "w", stdout);
	int t;
	cin >> t;
	for (int h = 0; h < t; h++)
	{
		int n;
		cin >> n;
		pair<int,char> R, O, Y, G, B, V;
		cin >> R.ff >> O.ff >> Y.ff >> G.ff >> B.ff >> V.ff;
		R.ss = 'R';
		Y.ss = 'Y';
		B.ss = 'B';
		pair<int, char> maxx = mp(-1, 'r');
		if (R.ff > maxx.ff) maxx = R;
		if (Y.ff > maxx.ff) maxx = Y;
		if (B.ff > maxx.ff) maxx = B;
		pair<int, char> minx = mp(100000000, 'r');
		if (R.ff <  minx.ff&& R.ss != maxx.ss) minx = R;
		if (Y.ff <  minx.ff&& Y.ss != maxx.ss) minx = Y;
		if (B.ff <  minx.ff&& B.ss != maxx.ss) minx = B;
		pair<int, char> midx = mp(100000000, 'r');
		if (R.ss !=  minx.ss && R.ss != maxx.ss ) midx = R;
		if (Y.ss != minx.ss && Y.ss != maxx.ss) midx = Y;
		if (B.ss != minx.ss && B.ss != maxx.ss) midx = B;
		//cout << minx.ss << ' ' << midx.ss << ' ' << maxx.ss << endl;
		vector<char> res(maxx.ff, maxx.ss);
		cout << "Case #" << h + 1 << ": ";
		if (maxx.ff > minx.ff + midx.ff)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		int j = 0;
		for (int i = 0; (i < res.size()&&midx.ff>0); i+=2)
		{
			res.insert(res.begin() + i, midx.ss);
			midx.ff--;
			j += 2;
		}
		for (int i = j; (i < res.size() && minx.ff>0); i+=2)
		{
			res.insert(res.begin() + i, minx.ss);
			minx.ff--;
		}
		if (minx.ff > 0)
		{
			for (int i = 0; (i < res.size() && minx.ff>0); i += 2)
			{
				res.insert(res.begin() + i, minx.ss);
				minx.ff--;
			}
		}
		for (int i = 0; i < res.size(); i++)
		{
			cout << res[i];
		}
		cout << endl;
	}
	return 0;
}
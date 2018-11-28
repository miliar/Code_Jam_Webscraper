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
const int INF = 1000000007;
using namespace std;
 
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	set<int> a;
	vector<int> cnt;
	for (int h = 0; h < t; h++)
	{
		a.clear();
		int k;
		int x;
		cin >> x >> k;
		if (x == k)
		{
			cout << "Case #" << h + 1 << ": " << 0 << ' ' << 0 << endl;
			continue;
		}
		a.insert(x);
		cnt.assign(x+2, 0);
		cnt[x]++;
		for (int i = 0; i < k-1; i++)
		{
			set<int>::iterator it = a.end();
			--it;
			int p = *it;
			cnt[p]--;
			if (cnt[p] <= 0)
				a.erase(it);
			//cout << p << endl;
			p--;
			a.insert(p / 2);
			a.insert((p / 2) + (p % 2));
			cnt[p / 2]++;
			cnt[(p / 2) + (p % 2)]++;
		}
		set<int>::iterator it = a.end();
		--it;
		int maxi = *(it);
		maxi--;
		cout << "Case #" << h + 1 << ": " << (maxi / 2) + (maxi % 2) << ' ' << maxi / 2 << endl;
	}
}
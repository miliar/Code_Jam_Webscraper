#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<vector>
#include<string>
#include<iostream>
#include<algorithm>
#include<map>
#include<iterator>
#include<set>
#include<stack>
#include<queue>
#include<fstream>
#include<iomanip>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include<cmath>
#include<list>
#include <sstream>
#define rep(i,m,n) for(int i = (m); i < (n); i++)
#define rep0(i, n) for(int i = (0); i < (n); i++)
#define repd(i,m,n) for(int i=(m); i > (n); i--)
#define ll long long
#define ull unsigned ll
#define pii pair<int,int>
#define pll pair<ll,ll>
#define plli pair<pll,int>
#define mp make_pair
#define endl '\n'
#define pb push_back
#define x first
#define y second
#define pt pair<ll,ll>
#define vi vector<int>
#define vll vector<ll>
#define vvi vector<vi>
#define vvll vector<vll>
#define vpll vector<pll>
#define vpt vector<pt>
#define pdd pair<double, double>
#define vpdd vector<pair<double, double> >
#define pq priority_queue
//#define _USE_MATH_DEFINES
using namespace std;
vvi g;
vvll dp, ams;
int n, k;

void convert(string& text, int start, int r) {
	for (int i = start; i < start + r; ++i) {
		text[i] = text[i] == '+' ? '-' : '+';
	}
}

bool check(string& line) {
	for (auto& l : line) {
		if (l == '-')
			return false;
	}

	return true;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("outclarge2.txt", "w", stdout);
	int t;
	cin >> t;
	
	for (int qt = 0; qt < t; ++qt) {
		ll n, k;
		cin >> n >> k;
		set<ll> length;
		map<ll, ll> counts;
		ll r = 0;
		length.insert(-n);
		counts[n] = 1;
		ll last = 0, next1, next2;
		do {
		
			last = -*length.begin();
			r += counts[last];
			length.erase(length.begin());
			next1 = (last - 1) / 2;
			next2 = last - 1 - next1;
			length.insert(-next1);
			length.insert(-next2);
			counts[next1] += counts[last];
			counts[next2] += counts[last];

		} while (r < k);

		cout << "Case #" << qt + 1 << ": "<<max(next1, next2) << " " << min(next1, next2)<<endl;
	}
}

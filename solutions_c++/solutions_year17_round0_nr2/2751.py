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
	freopen("B-large.in", "r", stdin);
	freopen("outBLarge.txt", "w", stdout);
	int t;
	cin >> t;
	
	for (int qt = 0; qt < t; ++qt) {
		string numb;
		cin >> numb;

		for (int i = numb.size() - 2; i >= 0; --i) {
			if (numb[i] > numb[i + 1]) {
				numb[i] = numb[i] - 1;
				for (int j = i + 1; j < numb.size(); ++j) {
					numb[j] = '9';
				}
			}
		}

		if (numb[0] == '0') {
			numb.erase(0, 1);
		}

		cout << "Case #" << qt + 1 << ": "<<numb<<endl;
	}
}

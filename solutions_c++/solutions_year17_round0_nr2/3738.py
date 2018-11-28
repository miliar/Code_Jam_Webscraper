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
#define vpii vector<pii>
#define vpll vector<pll>
#define vpt vector<pt>
#define vb vector<bool>
#define vvb vector<vb>
#define pdd pair<double, double>
#define vpll vector<pll>
#define vpdd vector<pair<double, double> >
#define pq priority_queue

using namespace std;

bool isOk(ll n) {
	string s = to_string(n);
	rep(i, 1, s.length()) {
		if (s[i] < s[i - 1]) {
			return false;
		}
	}
	return true;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	rep(qw, 1, t + 1) {
		string s;
		cin >> s;
		repd(i, s.length() - 1, 0) {
			if (s[i] < s[i - 1]) {
				s[i] = '9';
				int k = i-1;

				while (s[k] == '0') {
					k--;
				}
				s[k]--;
				rep(j, k+1, s.length()){
					s[j] = '9';
				}
				i = s.length();
			}
		}
		int begin = s.length()-1;
		rep(i, 0, s.length()) {
			if (s[i] != '0') {
				begin = i;
				break;
			}
		}
		cout << "Case #" << qw << ": ";
		rep(i, begin, s.length()) {
			cout << s[i];
		}
		cout << endl;
	}

	return 0;
}
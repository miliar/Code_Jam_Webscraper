#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <stdio.h>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <queue>
#include <unordered_map>
using namespace std;

#define all(v) (v).begin(),(v).end()
#define SRT(v) sort(all(v))
#define rall(v) (v).rbegin(),(v).rend()
#define rSRT(v) sort(rall(v))
#define sz(a) int((a).size())
#define PB push_back
#define trav(c,i) for(typeof((c).begin()i=(c).begin();i!=(c).end();i++)
#define mem(a, b) memset(a, b, sizeof(a))
#define MP make_pair
#define EPS      1e-9
#define Mod      (ll)1e9+7
#define oo       1e9
#define OO       1e14*1LL
#define PI       3.141592653589793
#define F        first
#define S        second
#define pw(x)	 (x)*(x)

typedef stringstream ss;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<long long> vll;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef pair<int, ll> il;
typedef vector<vector<ii>> vvii;
typedef vector<vector<il>> vvil;

//ll gcd(ll a, ll b) { return !b ? a : gcd(b, a % b); }
//ll lcm(ll a, ll b) { return (a / gcd(a, b)) * b; }

//char letters[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m'
//                    ,'n','o','p','q','r','s','t','u','v','w','x','y','z'};
//const int dx[] = { 0, -1, 0, 1, -1, -1, 1, 1 };
//const int dy[] = { 1, 0, -1, 0, 1, -1, 1, -1 };

int T, k;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w", stdout);
	cin >> T; string str; vi vec; int cnt = 0;
	for(int j=1;j<=T;j++){
		cin >> str >> k; vec.resize(sz(str));
		for (int i = 0; i < sz(str); i++) {
			if (str[i] == '+')
				vec[i] = 1;
			else
				vec[i] = 0;
		}
		for (int i = sz(vec) - 1; i >= 0; i--) {
			if (!vec[i]) {
				int end = i - k + 1;
				if (end >= 0) {
					for (int x = i; x >= end; x--)
						vec[x] = !vec[x];
					cnt++;
				}
			}
		}
		int s = 0;
		for (int i = 0; i < sz(vec); i++) {
			if (!vec[i]) {
				s = 1;
				break;
			}
		}
		if (!s)
			cout << "Case #" << j << ": " << cnt << endl;
		else
			cout << "Case #" << j << ": IMPOSSIBLE" << endl;
		cnt = 0; str.clear(); vec.clear();
	} 
	//int shit; cin>> shit;
	return 0;
}
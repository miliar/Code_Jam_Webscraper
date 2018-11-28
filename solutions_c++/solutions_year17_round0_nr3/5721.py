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

ll T, N, K;

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt", "w", stdout);
	cin >> T;
	for (int j = 1; j <= T; j++) {
		cin >> N >> K;
		vi vis(N + 2, 0); vis[0] = vis[N + 1] = 1;
		vi blocks; blocks.PB(0); blocks.PB(N + 1);
		vi pos, left, right, mins, maxs; int x, y;
		for (int p = 0; p < K; p++) {
			for (int i = 0; i < sz(blocks) - 1; i++) {
				int tmp = blocks[i + 1] - blocks[i] - 1; int mid;
				if (tmp % 2 != 0)
					mid = ((tmp + 1) / 2) + blocks[i];
				else
					mid = (tmp / 2) + blocks[i];
				int L = mid - blocks[i] - 1;
				int R = blocks[i + 1] - mid - 1;
				pos.PB(mid); left.PB(L); right.PB(R); mins.PB(min(L, R)); maxs.PB(max(L, R));
			}
			int idx = 0;
			for (int i = 0; i < sz(mins); i++) {
				if (mins[idx] < mins[i])
					idx = i;
				else if (mins[idx] == mins[i]) {
					if (maxs[idx] < maxs[i])
						idx = i;
				}
			}
			vis[pos[idx]] = 1; blocks.PB(pos[idx]); SRT(blocks);
			x = left[idx]; y = right[idx];
			left.clear(); right.clear(); pos.clear(); mins.clear(); maxs.clear();
		}
		cout << "Case #" << j << ": " << max(x, y) << " " << min(x, y) << endl;
		blocks.clear(); vis.clear();
	}
	//int shit; cin>> shit;
	return 0;
}
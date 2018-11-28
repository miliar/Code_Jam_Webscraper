#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <iomanip>
#include <set>
#include <map>
#include <queue>
#include <deque>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair <int, int> pii;
#define x first
#define y second
#define mp make_pair
#define pb push_back
const int N = (int)1e5 + 5, INF = (int)1e9;
const ld EPS = 1e-9;

int main()
{
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("bb.txt", "w", stdout);
	int T;
	cin >> T;
	for(int z = 1; z <= T; z++){
		multiset <int> s;
		int n, k;
		cin >> n >> k;
		s.insert(n);
		int a, b;
		while(k--){
			multiset<int>::iterator it = s.end();
			it--;
			int m = *(it);
			s.erase(it);
			a = m / 2; b = (m - 1) / 2;
			s.insert(a); s.insert(b);
		}
		cout << "Case #" << z << ": " << a << ' ' << b << "\n";
	}
	return 0;
}
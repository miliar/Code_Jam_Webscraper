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
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair <int, int> pii;
typedef pair <long long, long long> pll;
#define x first
#define y second
#define mp make_pair
#define pb push_back
const int N = (int)1e3 + 5, INF = (int)1e9;
const ld EPS = 1e-9;

pii a[N], b[N];

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	cin >> T;
	for(int z = 1; z <= T; z++){
		cout << "Case #" << z << ": ";
		int n, m;
		cin >> n >> m;
		for(int i = 0; i < n; i++)
			cin >> a[i].x >> a[i].y;
		for(int i = 0; i < m; i++)
			cin >> b[i].x >> b[i].y;
		if(max(n, m) < 2)
			cout << 2 << "\n";
		else if(n == 2){
			if(a[0].x > a[1].x)
				swap(a[0], a[1]);
			if(a[1].x - a[0].y < 720 && a[0].x + 1440-a[1].y < 720)
				cout << 4 << "\n";
			else
				cout << 2 << "\n";
		}
		else {
			if(b[0].x > b[1].x)
				swap(b[0], b[1]);
			if(b[1].x - b[0].y < 720 && b[0].x + 1440-b[1].y < 720)
				cout << 4 << "\n";
			else
				cout << 2 << "\n";
		}
	}
	return 0;
}
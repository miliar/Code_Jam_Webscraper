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
#define x first
#define y second
#define mp make_pair
#define pb push_back
const int N = (int)1e5 + 5, INF = (int)1e9;
const ld EPS = 1e-9;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	cin >> T;
	for(int z = 1; z <= T; z++){
		string s;
		cin >> s;
		int n = (int)s.size();
		int k = n;
		for(int i = n - 1; i > 0; i--){
			if(s[i] < s[i - 1]){
				s[i - 1]--;
				k = i;
			}
		}
		for(int i = k; i < n; i++)
			s[i] = '9';
		while(s[0] == '0')
			s.erase(0, 1);
		cout << "Case #" << z << ": " << s << "\n";
	}
	return 0;
}
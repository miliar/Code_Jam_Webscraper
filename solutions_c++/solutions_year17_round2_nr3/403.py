#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
#define mp make_pair
#define pb push_back
#define sz(x) ((int) (x).size())
#define db(x) cout << #x" = " << x << endl
#define db2(x,y) cout << #x" = " << x << "; " << #y" = " << y << endl
#define db3(x,y,z) cout << #x" = " << x << "; " << #y" = " << y << "; " << #z" = " << z << endl

#define X first
#define Y second

ld d[105][105];

ld e[105], s[105];
void solve(int test) {
	int n,q;
	cin >> n >> q;
	for (int i = 0; i < n; i++) cin >> e[i] >> s[i];
	
	
	for (int i = 0; i < n; i++) 
	   for (int j = 0; j < n; j++) {
		   cin >> d[i][j];
		   if (d[i][j] < 0) d[i][j] = 1e16;
	   }
	for (int k = 0; k < n; k++)
	   for (int i = 0; i < n; i++)
	      for (int j = 0; j < n; j++)
	         d[i][j] = min(d[i][k] + d[k][j], d[i][j]);
	for (int i = 0; i < n; i++)
	   for (int j = 0; j < n; j++)
	      if (d[i][j] > e[i]) 
	         d[i][j] = 1e16;
	      else d[i][j] = d[i][j] / s[i];
	for (int k = 0; k < n; k++)
	   for (int i = 0; i < n; i++)
	      for (int j = 0; j < n; j++)
	         d[i][j] = min(d[i][k] + d[k][j], d[i][j]);
	//cerr << "---" << endl;
	//for (int i = 0; i < n; i++, cerr << endl)
	//  for (int j = 0; j < n; j++) cerr << d[i][j] << ' ';
	cout << "Case #" << test << ": ";
	for (int i = 0; i < q; i++) {
		int a,b;
		cin >> a >> b;
		cout << d[a-1][b-1] << " \n"[i==q-1];
	}
}

int main()
{
	cout.precision(20);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		solve(i);
	}
	return 0;
}

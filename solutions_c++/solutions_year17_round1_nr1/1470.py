//By Ralif Rakhmatullin
#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
#include<math.h>
#include<cassert>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<map>
#include<ctime>
#include<queue>
#include<stack>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<bitset>
#include<valarray>
#include<iterator>
#include<list>
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define S second
#define ld long double
#define F first
#define y1 LOL
#define ld long double
#define pb push_back
#define len length
#define sz size
#define beg begin
const ll INF = (ll)1e18 + 123;
const int inf=(int)2e9 + 123; 
const int mod=1e9+7;
using namespace std;
char a[31][31];
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	//cout.tie(0);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin >> t;
	int cas = 1;
	while(t --){
		int n, m;
		cin >> n >> m;
		for(int i = 1; i <= n; i ++){	
			for(int j = 1; j <= m; j ++)
				cin >> a[i][j];
		}
		for(int i = 1; i <= n; i ++){
			for(int j = 2; j <= m; j ++){
				if(a[i][j] == '?' && j > 1)
					a[i][j] = a[i][j - 1];
			}
			for(int j = m - 1; j >= 1; j --){
				if(a[i][j] == '?' && j < m)
					a[i][j] = a[i][j + 1];
			}
		}
		for(int j = 1; j <= m; j ++){
			for(int i = 2; i <= n; i ++){
				if(a[i][j] == '?')
					a[i][j] = a[i - 1][j];
			}
			for(int i = n - 1; i >= 1; i --){
				if(a[i][j] == '?')
					a[i][j] = a[i + 1][j];
			}
		}
		cout << "Case #" << cas << ":\n";
		for(int i = 1; i <= n; i ++){
			for(int j = 1; j <= m; j ++)
				cout << a[i][j];
			cout << endl;
		}
		cas ++;
	}
	return 0;
}

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

char a[25+1][25+1];

int main() {
    //freopen("x.in", "r", stdin);
	int ans;
	//freopen("C-small-practice.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);

	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);

	int tt, tn;
	cin >> tn;
	F1(tt,tn) {
		int R, C;
		cin >> R;
		cin >> C;
		F0(i, R) {

			cin >> a[i];
		}
		/* Left to right. Top to Bottom */
		F0(i, R) {
			char previous = '#';
			F0(j, C) {
				if (a[i][j] != '?')
				{
					previous = a[i][j];
				}
				else
				{
					a[i][j] = previous!='#'?previous:a[i][j];
				}
			}
		}

		/* Right to left. Top to Bottom */
		F0(i, R) {
			char previous = '#';
			for (int j = C-1; j >=0; j--)
			{
				
				if (a[i][j] != '?')
				{
					previous = a[i][j];
				}
				else
				{
					a[i][j] = previous!='#'?previous:a[i][j];
				}
			}
		}

		F0(j, C) {
			char previous = '#';
			F0(i, R) {
				if (a[i][j] != '?')
				{
					previous = a[i][j];
				}
				else
				{
					a[i][j] = previous!='#'?previous:a[i][j];
				}
			}
		}


		for (int j = C-1; j >=0; j--)
		{
			char previous = '#';
			F0(i, R) 
			{
				
				if (a[i][j] != '?')
				{
					previous = a[i][j];
				}
				else
				{
					a[i][j] = previous!='#'?previous:a[i][j];
				}
			}
		}
		/* Top to Bottom. Right to Left */
		F0(j, C) {
			char previous = '#';
			for (int i = R-1; i >=0; i--)
			{
				if (a[i][j] != '?')
				{
					previous = a[i][j];
				}
				else
				{
					a[i][j] = previous;
				}
			}
		}

		for (int j = C-1; j >=0; j--)
		{
			char previous = '#';
			for (int i = R-1; i >=0; i--)
			{
				if (a[i][j] != '?')
				{
					previous = a[i][j];
				}
				else
				{
					a[i][j] = previous;
				}
			}
		}

		for (int i = R-1; i >=0; i--)
		{
			char previous = '#';
			F0(j, C) 
			{
				if (a[i][j] != '?')
				{
					previous = a[i][j];
				}
				else
				{
					a[i][j] = previous;
				}
			}
		}

		for (int i = R-1; i >=0; i--)
		{
			char previous = '#';
			for (int j = C-1; j >=0; j--)
			{
				if (a[i][j] != '?')
				{
					previous = a[i][j];
				}
				else
				{
					a[i][j] = previous;
				}
			}
		}
		cout << "Case #" << tt << ": " << endl;
		
		F0(i, R) {
			cout << a[i] << endl;
		}
	}
}

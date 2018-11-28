// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdio.h"
#include "conio.h"
#include "string.h"
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
typedef pair<int, int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define RF0(i,n) for(int i=n-1;i>=0;i--)
#define F1(i,n) for(int i=1;i<=n;i++)
#define RF1(i,n) for(int i=n;i>=1;i--)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll ucln(ll x, ll y) { return y ? ucln(y, x%y) : x; }
ll bcnn(ll x, ll y) { return (x*y) / ucln(x, y); }
bool prime(ll n) { for (ll i = 2, size = sqrt(n); i <= size; i++) if (n%i == 0) return false;	return true; }
int bc(int n) { return n ? bc((n - 1)&n) + 1 : 0; }
/*
int get_line_intersection(float p0_x, float p0_y, float p1_x, float p1_y,
	float p2_x, float p2_y, float p3_x, float p3_y, float *i_x = NULL, float *i_y = NULL)
{
	float s1_x, s1_y, s2_x, s2_y;
	s1_x = p1_x - p0_x;     s1_y = p1_y - p0_y;
	s2_x = p3_x - p2_x;     s2_y = p3_y - p2_y;

	float s, t;
	s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / (-s2_x * s1_y + s1_x * s2_y);
	t = (s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / (-s2_x * s1_y + s1_x * s2_y);

	if (s >= 0 && s <= 1 && t >= 0 && t <= 1)
	{
		// Collision detected
		if (i_x != NULL)
			*i_x = p0_x + (t * s1_x);
		if (i_y != NULL)
			*i_y = p0_y + (t * s1_y);
		return 1;
	}

	return 0; // No collision
}
*/
typedef __int64    INT;
bool f;
int t;
INT     k, n, L, R, index;
vector<INT>     S;

bool myfunction (INT i, INT j) { return (i>j); }

int main() {

	//freopen("test.in", "r", stdin);
	//freopen("test.out", "w", stdout);

    freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);

	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);

	cin >> t;
    //cout << t;
	//t = 1; // test

	F0(i, t) {
		cin >> n;
		cin >> k;

        S.clear();
        S.push_back(n);
        F0(j, k) {
            L = ceil(1.0f*S[0]/2-1);
            R = S[0]/2;
            S.erase(S.begin(), S.begin()+1);
            S.push_back(L);
            S.push_back(R);
            sort(S.begin(), S.end(), myfunction);
            //cout << "Attemp j = " << j << ": L = " << L << " --- R: " << R << endl;
        }

        cout << "Case #" << i+1 << ": " << max(L, R) << " " << min(L, R) << endl;
	}

	//getch();
	return 0;
}

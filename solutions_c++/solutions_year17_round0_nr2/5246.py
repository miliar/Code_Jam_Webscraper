// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdio.h"
#include "conio.h"
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
typedef unsigned __int64    INT;
bool f;
int t;
INT    n, x, y;
vector<int> arr;

bool check(INT n) {
	INT i, j;

	if (n < 10) return true;

    j = n % 10;
    n = n / 10;
	while (n > 0) {
        i = n % 10;
        cout << "n = " << n << "  i = " << i << "  j = " << j << endl;
        if (i > j)  return false;
        j = i;
        n = n / 10;
	}

	return true;
}

int main() {

	//freopen("test.in", "r", stdin);
	//freopen("test.out", "w", stdout);

    freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	//freopen("C-small-attempt2.in", "r", stdin);
	//freopen("C-small-attempt2.out", "w", stdout);

	cin >> t;
    //cout << t;
	//t = 1; // test

	F0(i, t) {
		cin >> n;
		//cout << n << endl;
        /*while (n >= 0) {
            if (check(n)) {
                cout << "Case #" << i+1 << ": " << n << endl;
                break;
            }
            else n--;
        }*/
        arr.clear();
        while (n > 0) {
            arr.push_back(n%10);
            n /= 10;
            //cout << "arr[" << arr.size()-1 << "] = " << arr[arr.size()-1] << endl;
        }


        for (int j = 0; j < (int)(arr.size()-1); j++) {
            /*cout << "*** BEFORE ";
            for (int k = 0, size = arr.size(); k < size; k++)   cout << arr[k] << " ";
            cout << "-- truoc = " << j << " -- sau = " << j+1 << endl;
            */
            if (arr[j] < arr[j+1]) {
                for (int k = 0; k <= j; k++)    arr[k] = 9;
                arr[j+1]--;
                if (arr[arr.size()-1] == 0) arr.pop_back();
                j = -1;
            }
            /*
            cout << "*** AFTER  ";
            for (int k = 0, size = arr.size(); k < size; k++)   cout << arr[k] << " ";
            //cout << "-- truoc = " << arr[j] << " -- sau = " << arr[j+1] << endl;
            cout << endl;
            */
        }
        n = 0;
        for (int j = arr.size()-1; j >= 0; j--)  n = n*10 + arr[j];
        cout << "Case #" << i+1 << ": " << n << endl;
	}

	//getch();
	return 0;
}

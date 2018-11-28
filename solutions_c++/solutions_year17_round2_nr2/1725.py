#pragma warning(disable : 4996) //_CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <set>
#include <fstream>
#include <iomanip>
#include <iso646.h>
#include <stdio.h>
#include <map>
#include <queue>
#include <string.h>

typedef long long LL;
typedef long double LD;

#define sync ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ss second
#define ff first
#define mp make_pair
#define endl "\n"
#define pb push_back
#define FilkinMaksim int main()
#define exit return 0
#define f_in freopen("input.txt", "r", stdin)
#define f_out freopen("output.txt", "w", stdout)
#define file_on f_in; f_out

//const LD M_PI = 3.14159265358979323846;
const LD EPS = 0.0000000001;
const LL INF = 1000000007;

using namespace std;

const int nmax = 10001;

//vector < double > a;

vector <char> a;

int main() {
	file_on;
	int q;
	cin >> q;
	for (int gi=1; gi<=q; gi++)
	{
		int n,r,o,y,g,b,v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		if (r>b+y || b>y+r || y>r+b) printf("Case #%d: IMPOSSIBLE\n", gi);
		else
		{
			pair <int, char> mas[3];
			mas[0] = make_pair(r, 'R');
			mas[1] = make_pair(b, 'B');
			mas[2] = make_pair(y, 'Y');
			sort(mas, mas + 3);
			for (int i = 0; i < mas[2].first; i++)
				a.push_back(mas[2].second);
			int j = 0;
			for (int i = 0; i < a.size() && mas[1].first>0; i += 2)
			{
				a.insert(a.begin() + i, mas[1].second);
				mas[1].first--;
				j += 2;
			}
			for (int i = j; i < a.size() && mas[0].first>0; i += 2)
			{
				a.insert(a.begin() + i, mas[0].second);
				mas[0].first--;
			}
			if (mas[2].first > 0)
			{
				for (int i = 0; i < a.size() && mas[0].first>0; i += 2)
				{
					a.insert(a.begin() + i, mas[0].second);
					mas[0].first--;
				}
			}
			printf("Case #%d: ", gi);
			for (int i = 0; i < a.size(); i++)
				cout << a[i];
			cout << endl;
			a.clear();
		}
	}
}
//printf("Case #%d: %.6f\n", gi, d);
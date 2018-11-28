#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
#include <sstream>
#include <cstring>
#include <cmath>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <bitset>
#include <functional>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>
#include <cstdio>
#include <chrono>
#include <thread>
using namespace std;
typedef long long int ll;
typedef pair<string, ll> si;
typedef pair<ll, string> is;
typedef pair<double, double> dd;
typedef pair<ll, ll> ii;
typedef pair<string, string> ss;
typedef map<ll, ll>::iterator it;
#define inf 100000000000000
#define lop2(i,a,b) for(int i=a;i<b;i++)
#define lop(i,b) for(int i=0;i<b;i++)
template <class T>
T power(T a, T b) { T x; if (b == 0) x = 1; else x = a; for (size_t i = 1; i < b; i++)  x *= a; return x; }
ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }

ll n, m, a, b, c, ab, ba, x, y, z, avg, sum;
ll arr2[30], arr3[200000], arr4[200001], arr5[100001];
char c2;
bool f, f1, f2;
string str, s1, s2, s3, s4;
set<int> seto;
double d, d1;
ll x1, x2, y11, y2;
ll mini = inf, maxi = 0;

map<ll, ll> mp;
vector<ll> v;

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	cin >> n;
	while (n--) {
		cin >> str;
		f = 0;
		memset(arr2, 0, sizeof(arr2));
		lop(i, str.size() - 1) {
			if (str[i] <= str[i + 1]) {
				arr2[i + 1] = str[i + 1] - str[i];
			}
			else {
				if (!i) {
					if (str[i] == '1') {
						str.resize(str.size() - 1);
						lop(j, str.size()) {
							str[j] = '9';
						}
					}
					else {
						str[i]--;
						lop2(j, 1, str.size()) {
							str[j] = '9';
						}
					}
				}
				else if (arr2[i] != 0) {
					str[i]--;
					lop2(j, i + 1, str.size()) {
						str[j] = '9';
					}
				}
				else {
					while (i > 0) {
						if (arr2[i] != 0) {
							f = 1;
							str[i]--;
							lop2(j, i + 1, str.size()) {
								str[j] = '9';
							}
							break;
						}
						i--;
					}
					if (!f) {
						if (str[i] == '1') {
							str.resize(str.size() - 1);
							lop(j, str.size()) {
								str[j] = '9';
							}
						}
						else {
							str[i]--;
							lop2(j, 1, str.size()) {
								str[j] = '9';
							}
						}
					}
				}
				break;
			}
		}
		printf("Case #%lld: %s\n", ++y, str.c_str());
	}
}
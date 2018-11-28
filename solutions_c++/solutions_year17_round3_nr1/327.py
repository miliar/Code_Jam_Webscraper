// #include <bits/stdc++.h>
#include <iostream>
#include <limits>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <sstream>

using namespace std;

#define MAXINT numeric_limits<int>::max()
#define MININT numeric_limits<int>::min()
#define PI 3.141592653589793238
#define rep(i, a, n) for(int i = (a); i < (n); i++)
#define per(i, a, n) for(int i = (n)-1; i >= (a); i--)
#define pb push_back
#define mp make_pair
#define fi first
#define sn second
#define vi vector<int>
#define si set<int>
#define li list<int>
#define lit list<int>::iterator
#define sit set<int>::iterator
#define mit map<int, int>::iterator

	

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<double, double> pdd;

template <typename T>
void print_array(T arr[], int size_arr){
	rep(i, 0, size_arr){
		cout << arr[i];
		if(i == size_arr - 1) cout << endl;
		else cout << " ";
	}
}

template<typename T>
void print_vector(vector<T> v){
	rep(i, 0, v.size()){
		cout << v[i];
		if(i == v.size() - 1) cout << endl;
		else cout << " ";
	}
}

template <typename T>
void memset_array(T arr[], T value, int size_arr){
	rep(i, 0, size_arr){
		arr[i] = value;
	}
}

bool compare_lexical_string(string a, string b){
	rep(i, 0, min(a.length(), b.length())){
		if(a[i] != b[i]) return a[i] < b[i];
	}
	return a.length() < b.length();
}
struct lex_string
{
	bool operator()(string a, string b){
		return compare_lexical_string(a, b);
	} 
};



/////////////////////////////////////////////////////////////////////////////
// NEVER USE NAME : DISTANCE FOR FUNCTION
// NEVER USE NAME : FIND FOR FUNCTION
// AVOID DOUBLE IF POSSIBLE
////////////////////////////////////////////////////////////////////////////
// compare_lexical_string("huy", "huy") will return false

bool compare_pll(pll a, pll b){
	if(a.fi != b.fi) return a.fi < b.fi;
	else return a.sn < b.sn;
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	int t; cin >> t;
	rep(test, 1, t+1){
		int n, k; cin >> n >> k;
		pll cake[n];
		rep(i, 0, n) cin >> cake[i].fi >> cake[i].sn;
		sort(cake, cake + n, compare_pll);
		double dp[k+1][n];
		rep(i, 0, n) dp[1][i] = cake[i].fi*cake[i].fi * PI + 2*cake[i].fi * cake[i].sn * PI;
		rep(i, 2, k+1){
			rep(j, 0, n){
				if(j < i-1) dp[i][j] = -1;
				else{
					dp[i][j] = 0;
					rep(k, i-2, j){
						dp[i][j] = max(dp[i][j], dp[i-1][k] + cake[j].fi*cake[j].fi*PI + 2*cake[j].fi*cake[j].sn*PI-cake[k].fi *cake[k].fi*PI);
					}
				}
			}
		}
		double res = 0;
		rep(i, 0, n) res = max(res, dp[k][i]);
		cout << setprecision(20) << "Case #" << test << ": " << res << endl;
	}

	return 0;
}
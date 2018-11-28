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
#define PI 3.1415926
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
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	int t; cin >> t;
	rep(test, 1, t+1){
		int n, c, m; cin >> n >> c >> m;
		int seat[m], person[m];
		int total[c+1]; memset_array(total, 0, c+1);
		rep(i, 0, m){
			cin >> seat[i] >> person[i];
			total[person[i]] += 1;
		}
		int max_total = 0;
		rep(i, 1, c+1) max_total = max(max_total, total[i]);
		int accu_[n+1]; memset_array(accu_, 0, n+1);
		rep(i, 0, m) accu_[seat[i]]++;
		int accu[n+1];
		accu[0] = 0;
		rep(i, 1, n+1){
			accu[i] = accu[i-1] + accu_[i];
		}
		int min_ride = accu_[1];
		rep(i, 2, n+1) min_ride = max(min_ride, (accu[i]+1)/i);
		min_ride = max(min_ride, max_total);

		int prom = 0;
		rep(i, 1, n+1) prom += max(0, accu_[i] - min_ride);

		cout << "Case #" << test << ": " << min_ride << " " << prom << endl;
	}
	return 0;
}
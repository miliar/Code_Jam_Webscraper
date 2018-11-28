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
#include <functional>

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
template<typename T> void print_queue(T& q) {
    while(!q.empty()) {
        std::cout << q.top().fi << " " << q.top().sn << endl;
        q.pop();
    }
    std::cout << '\n';
}

int n, k;

struct comp_interval
{
	bool operator()(pii a, pii b){
		if(a.sn - a.fi != b.sn - b.fi)
			return a.sn - a.fi < b.sn - b.fi;
		else return a.fi > b.fi;
	}
};

pii solve(){
	priority_queue<pii, vector<pii>, comp_interval> interval;
	interval.push(pii(0, n+1));
	rep(i, 0, k-1){
		pii head = interval.top(); interval.pop();
		pii left = pii(head.fi, (head.fi + head.sn)/2);
		pii right = pii((head.fi + head.sn)/2, head.sn);
		if(left.sn - left.fi > 1) interval.push(left);
		if(right.sn - right.fi > 1) interval.push(right);
	}
	pii head = interval.top(); interval.pop();
	pii left = pii(head.fi, (head.fi + head.sn)/2);
	pii right = pii((head.fi + head.sn)/2, head.sn);
	if(left.sn - left.fi > 1) interval.push(left);
	if(right.sn - right.fi > 1) interval.push(right);
	return pii(left.sn - left.fi - 1, right.sn - right.fi - 1);
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	int t; cin >> t;
	rep(test, 1, t+1){
		cin >> n >> k;
		pii res = solve();
		cout << "Case #" << test << ": " << res.sn << " " << res.fi << endl;
	}
	return 0;
}
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
		int n, p; cin >> n >> p;
		int count = 0;
		vi g;
		rep(i, 0, n){
			int x;
			cin >> x;
			if(x%p == 0) count++;
			else{
				g.pb(x);
			}
		}
		if(p==2){
			count += (g.size()+1)/2;
		}
		else if(p == 3){
			int one, two;
			one = two = 0;
			rep(i, 0, g.size()){
				if(g[i]%3==1) one++;
				else two++;
			}
			count += min(one, two);
			count += (max(one, two) - min(one, two) + 2)/3; 
		}
		else if(p == 4){
			int one, two, three;
			rep(i, 0, g.size()){
				if(g[i]%4==1) one++;
				else if(g[i]%4==2) two++;
				else three++;
			}
			int plus_1 = min(one, three);
			count += plus_1;
			one -= plus_1;
			three -= plus_1;
			int plus_2 = two/2;
			count += plus_2;
			two -= plus_2*2;

			if(two == 0) count += (three + one + 3)/4;
			else{
				int sum = three + one;
				count += sum/4;
				sum -= sum/4 * 4;
				if(sum < 3) count += 1;
				else count += 2;
			}
		}
		cout << "Case #" << test << ": " << count << endl;
	}
	return 0;
}
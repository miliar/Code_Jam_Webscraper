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
bool compare_pii_a(pii a, pii b){
	return a.fi < b.fi;
}


bool compare_pii_b(pii a, pii b){
	return a.sn - a.fi < b.sn - b.fi;
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	int t; cin >> t;
	rep(test, 1, t+1){
		int ac, aj; cin >> ac >> aj;
		pii C[ac], J[aj];
		int current_sum_C = 0;
		int current_sum_J = 0;
		rep(i, 0, ac){
			cin >> C[i].fi >> C[i].sn;
			current_sum_C += C[i].sn - C[i].fi;
		}
		rep(i, 0, aj){
			cin >> J[i].fi >> J[i].sn;
			current_sum_J += J[i].sn - J[i].fi;
		}
		sort(C, C+ac, compare_pii_a);
		sort(J, J+aj, compare_pii_a);

		// find free C intervals
		vector<pii> free_C, free_J;
		rep(i, 0, ac-1){
			bool ok = true;
			rep(j, 0, aj){
				if(J[j].fi >= C[i].sn && J[j].fi < C[i+1].fi){
					ok = false;
					break;
				}
			}
			if(ok) free_C.pb(pii(C[i].sn, C[i+1].fi));
		}
		if(aj == 0 || (ac > 0 && C[ac-1].fi > J[aj-1].fi && C[0].fi < J[0].fi)) free_C.pb(pii(C[ac-1].sn, C[0].fi + 24*60));

		// find free J intervals
		rep(i, 0, aj-1){
			bool ok = true;
			rep(j, 0, ac){
				if(C[j].fi >= J[i].sn && C[j].fi < J[i+1].fi){
					ok = false;
					break;
				}
			}
			if(ok) free_J.pb(pii(J[i].sn, J[i+1].fi));
		}
		if(ac == 0 || (aj > 0 && J[aj-1].fi > C[ac-1].fi && J[0].fi < C[0].fi))  free_J.pb(pii(J[aj-1].sn, J[0].fi + 24*60));

		// combine C intervals
		sort(free_C.begin(), free_C.end(), compare_pii_b);
		sort(free_J.begin(), free_J.end(), compare_pii_b);
		int count_C = free_C.size(), count_J = free_J.size();
		int sum_C = 0, sum_J = 0;
		rep(i, 0, free_C.size()){
			sum_C += free_C[i].sn - free_C[i].fi;
			if(sum_C > 720 - current_sum_C){
				count_C = i;
				break;
			}
		}
		rep(i, 0, free_J.size()){
			sum_J += free_J[i].sn - free_J[i].fi;
			if(sum_J > 720 - current_sum_J){
				count_J = i;
				break;
			}
		}

		cout << "Case #" << test << ": " << 2*max(ac - count_C, aj - count_J) << endl;

	}
	
	return 0;
}
/*
	Pratik Gajjar
*/
#include <bits/stdc++.h>
using namespace std;
/*
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
//ordered_set < int > rbtree;
//int i = *rbtree.find_by_order(2) 
//int j = rbtree.order_of_key(2)
*/
 
typedef long long ll;
typedef long double ld;
typedef vector<ll> vl;
typedef pair<ll, ll> pll;
typedef vector<pll> vpll;
typedef set<ll> setl;
typedef map<string, ll> msl;
typedef map<ll,ll> mll;

#define sortv(x) sort(x.begin(),x.end())
#define all(v) v.begin() , v.end()
#define UNIQUE(c) (c).resize(unique(all(c)) - (c).begin())
#define binarysearch(v, n) binary_search(all(v),n)
#define rev(v) reverse(all(v))
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define fa(i, a, b) for (ll i = a ; i < b ; i++) 
#define f(i,b) for (ll i = 0 ; i < b ; i++)
#define fv(x , it , c ) for (x ::iterator it = (c).begin(); it != (c).end(); it++)

const ll INF = LONG_MAX-SHRT_MAX ; 
const ll MINF = LLONG_MIN;
const ll mod = 1000000007;
const ll N = 1000010;
const ld PI = 2 * acos(0.0) ;
string str ;
int main()
{
	cout << fixed <<std::setprecision(12) ;   
	ll t ;
	cin >> t ;
	f(i , t){
		std::cout << "Case #" << (i+1) << ": " ;
		cin >> str ;
		ll sz = str.size();
		string old = str ;
		sortv(str) ;
		ll index = sz-1;
		while(str != old){
			int val = stoi(old);
			val--;
			old = to_string(val);
			str = old ;
			sortv(str);
		}
		cout << str << "\n" ;
	}
 	return 0;
}
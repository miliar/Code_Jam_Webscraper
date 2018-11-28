#define _CRT_SECURE_NO_WARNINGS
#include <cctype>
#include <climits>
#include <cmath>
#include <cstring>
#include <deque>
#include <fstream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <bitset>
#include <numeric>
#include <ratio>
#include <regex>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <valarray>

using namespace std;

#define sz(v) (int)v.size()
#define eps 1e-10
#define all(v) v.begin(), v.end() 
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define chk(a,k) ((bool)(a&(1<<(k))))
#define set0(a,k) (a&(~(1<<(k))))
#define set1(a,k) (a|(1<<(k)))
#define in(v, x) (find(all(v),x) != v.end()) 
#define re return
#define sum(v) accumulate(v.begin(),v.end(),(ld)0)
#define tr(v,it) for(auto it=v.begin();it != v.end();it++)
#define asrt(v) sort(v.begin(),v.end())
#define dsrt(v) sort(v.rbegin(),v.rend())
#define rev(v) reverse(v.begin(),v.end())
#define pi 3.1415926535897932384626433832795
#define MOD 1000000007
#define print(v) for (auto& i:v) cout<<i<<endl 
#define endl '\n'

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<string> vs;
typedef vector<vi> vvi;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<string> vs;
typedef vector<vi> vvi;

#define print "Case #"+to_string(t1)+": " 

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<string> vs;
typedef vector<vector<int>> vvi;



int main() {
	freopen("Data/in.txt", "r", stdin);
	freopen("Data/out.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t1=1; t1<=T; t1++) {
		string s;
		int k;
		cin >>s>>k;
		int c=0;
		for(int i=0; i<sz(s); i++) {
			if(s[i]=='-') {
				c++;
				if(i+k-1>=sz(s)) {
					c=sz(s) + 1;
					break;
				}
				for(int j=0; j<k; j++) {
					if(s[i+j]=='-') s[i+j]='+';
					else s[i+j]='-';
				}
			}
		}
		cout<<print;
		if(c>sz(s)) {
			cout<<"IMPOSSIBLE";
		} else{
			cout<<c;
		}
		cout<<endl;
	}
	getchar();
	return 0;
}

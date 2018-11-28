#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

#define IT(a,it) for(auto it=a.begin(); it != a.end(); it++)
#define REV_IT(a,it) for(auto it=a.rbegin(); it != a.rend(); it++)
#define LL long long
#define LD long double
#define MP make_pair
#define FF first
#define SS second
#define PB push_back
#define INF (int)(1e9)
#define EPS (double)(1e-9)

#ifndef ONLINE_JUDGE
#  define LOG(x) cerr << #x << " = " << (x) << endl
#else
#  define LOG(x) 0
#endif

#define MAXX 500005

using namespace std;

typedef pair <int, int> pi_i;
typedef pair<int, pi_i> pi_ii;

bool cmp(int a, int b){ return a>b; }
template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template<class T> T lcm(T a, T b) { return a * (b / gcd(a, b)); }

int n, vv;
string s;

bool chk(int val){
	string ss = to_string(val);
	//cout << val << " " << ss << endl;
	for(int i = 0;i < ss.size() - 1;i++){
		if(ss[i] > ss[i+1]) return false;
	}return true;
}

void bf(){
	for(int i = vv;i >= 0;i--){
		if(chk(i) == true){
			cout << i << endl;break;
		}
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	
	freopen("in.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	
	int T, casee = 1;
	cin >> T;
	for(casee=1;casee<=T;casee++){
		cout << "Case #" << casee << ": " ;
		//cin >> vv;
		cin >> s;
		//s = to_string(vv);
		n = s.size();
		//bf();
		int idx1 = -1, idx2 = -1;
		for(int i = 0;i < n-1;i++){
			int j = i+1;
			for(;j < n;j++){
				if(s[i] != s[j]) break;
			}
			if(j == n) break;
			if(s[i] > s[j]){
				idx1 = i, idx2 = j;
				//cout << idx1 << " " << idx2 << endl;
				break;
			}
			i = j-1;
		}
		if(idx1 == -1){
			cout << s << endl;
		}else if(s[idx1] == '1' && s[idx2] == '0'){
			for(int i = 0;i < n-1;i++){
				cout << '9';
			}cout << endl;
		}else{
			s[idx1] = s[idx1] - 1;
			for(int i = idx1+1;i < n;i++) s[i] = '9';
			cout << s << endl;
		}
	}
	
	//fclose(stdin);
	//fclose(stdout);
return 0;	
}


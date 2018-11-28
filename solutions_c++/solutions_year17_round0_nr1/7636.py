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

int n, k;
string s;

int main(){
	ios_base::sync_with_stdio(false);
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T, casee = 1;
	cin >> T;
	for(casee=1;casee<=T;casee++){
		cin >> s >> k;
		n = s.size();
		int ans = 0;bool can = true;
		for(int i = 0;i < n;i++){
			if(s[i] == '-'){
				ans++;
				if(i + k - 1 < n){
					for(int j = i;j <= i + k - 1;j++){
						if(s[j] == '-') s[j] = '+';
						else s[j] = '-';
					}
				}else{
					can = false;break;
				}
			}
		}
		cout << "Case #" << casee << ": " ;
		if(can == true) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	
	//fclose(stdin);
	//fclose(stdout);
return 0;	
}


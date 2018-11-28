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

LL D, N, K[MAXX], S[MAXX];

bool chk(LD val){
	LD timee = (LD)D/(LD)val;
	for(int i = 0;i < N;i++){
		LD dist = D - K[i];
		LD tt = (LD)dist/(LD)S[i];
		if(timee <= tt) return false;
	}return true;
}

int main(){
	ios_base::sync_with_stdio(false);
	
	freopen("in.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	
	int T, casee = 1;
	cin >> T;
	for(casee=1;casee<=T;casee++){
		cin >> D >> N;
		for(int i = 0;i < N;i++){
			cin >> K[i] >> S[i];
		}
		LD st = 0.0, en = 1e15, ans = 0;
		for(int i = 0;i < 100;i++){
			LD mid = (st + en)/(LD)2.00;
			bool b = chk(mid);
			if(b) st = mid, ans = max(ans, mid);else en = mid;
		}
		cout << "Case #" << casee << ": " ;
		cout << fixed << setprecision(8) << ans << endl;
	}
	
	//fclose(stdin);
	//fclose(stdout);
return 0;	
}


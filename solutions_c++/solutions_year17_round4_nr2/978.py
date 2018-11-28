#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#define X first 
#define Y second 
#define MP make_pair
#define PB push_back
#define ll long long
#define CLR(x) memset(x,0,sizeof(x))
#define vrep(i, v)    for(int i = 0; i < v.size(); i++)
#define rep(i, a, b)  for(int i = a; i <= b; i++)
#define drep(i, a, b) for(int i = a; i >= b; i--)
using namespace std;
const double pi = acos(-1.), eps = 1e-6;
const int                   Maxn=1010,Maxk=5010,Mo=1e9 + 7,oo = INT_MAX;
// const ll oo=LLONG_MAX >> 2;
const int sp[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};
int T;
using namespace std;
int n,m,k,cs;
struct Rec{
	int a, b,l;
};
int N,M,C;
int cnt[1010],num[1010], sum[Maxn];
int p[1010], c[1010];
int main(){
	cin >> T;
	while(T--){
		printf("Case #%d: ",++cs);
		cin >> N >> C >> M;
		memset(cnt,0,sizeof(cnt));
		memset(num,0,sizeof(num));
		memset(sum,0,sizeof(sum));
		for (int i=1;i<=M;i++){
			cin >> p[i] >> c[i];
			num[c[i]] ++;
			cnt[p[i]] ++;
		}
		for (int i=1;i<=N;i++) sum[i] = sum[i-1] + cnt[i];
		// for (int i=1;i<=N;i++) cout << sum[i] << " "; cout << endl;
		int l = 1, r = 1000;
		while(l < r){
			int mid = l + r >> 1;
			int ck = 1;
			for (int i =1; i<=1000;i++){
				if (sum[i] > i * mid) ck = 0;
			}
			if (ck) r = mid; else l = mid + 1;
		}
		ll xans = 0;
		rep(i,1,C) l = max(l, num[i]);
		rep(i,1,1000){
			xans += max(cnt[i] - l, 0);
		}
		cout << l <<" "<< xans << endl;
	}
	return 0;
}
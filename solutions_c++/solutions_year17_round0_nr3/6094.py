#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <cassert>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
typedef pair<int,P> P1;
typedef pair<P,P> P2;
#define pu push
#define pb push_back
#define mp make_pair
#define eps 1e-7
#define INF 1000000000
#define fi first
#define sc second
#define rep(i,x) for(int i=0;i<x;i++)
#define SORT(x) sort(x.begin(),x.end())
#define ERASE(x) x.erase(unique(x.begin(),x.end()),x.end())
#define POSL(x,v) (lower_bound(x.begin(),x.end(),v)-x.begin())
#define POSU(x,v) (upper_bound(x.begin(),x.end(),v)-x.begin())
int t;
int main()
{
	cin >> t;
	for(int ii=1;ii<=t;ii++){
		int n,k; cin >> n >> k;
		priority_queue<P2>que;
		int x = (n+1)/2-1;
		int y = n+1-(n+1)/2-1;
		if(x>y) swap(x,y);
		que.push(mp(mp(x,y),mp(0,n+1)));
		int ans,ans2;
		for(int i=0;i<k;i++){
			P2 p = que.top(); que.pop();
			int x = -1*p.sc.fi,y = p.sc.sc;
			{
				ans = (y+x)/2-x-1;
				ans2 = y-(y+x)/2-1;
				int k = x+(x+y)/2; k/=2;
				int G = min(k-x,(x+y)/2-k)-1;
				int H = max(k-x,(x+y)/2-k)-1;
				que.push(mp(mp(G,H),mp(-1*x,(x+y)/2)));
				//cout << G << " " << x << " " << (x+y)/2 << endl;
				k = (x+y)/2+y; k/=2;
				G = min(y-k,k-(x+y)/2)-1;
				H = max(y-k,k-(x+y)/2)-1;
				que.push(mp(mp(G,H),mp(-1*(x+y)/2,y)));
				//cout << G << " " << (x+y)/2 << " " << y << endl;

			}
		}
		printf("Case #%d: %d %d\n",ii,max(0,max(ans,ans2)),max(0,min(ans,ans2)));
	}
}
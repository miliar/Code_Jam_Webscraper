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
int t,n;
int main()
{
	cin >> t;
	for(int i=1;i<=t;i++){
		int a; cin >> a;
		for(int j=a;j>=1;j--){
			vector<int>vi; int k = j;
			while(k){
				vi.pb(k%10);
				k/=10;
			}
			for(int l=1;l<vi.size();l++){
				if(vi[l-1] < vi[l]) goto fail;
			}
			printf("Case #%d: %d\n",i,j); break;
			fail:;
		}
	}
}
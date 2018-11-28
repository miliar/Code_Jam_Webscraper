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
	int n,p;
	int a[55],b[55][55],used[55][55];
	cin >> t;
	for(int r=1;r<=t;r++){
		cin >> n >> p;
		for(int i=1;i<=n;i++) cin >> a[i];
		for(int i=1;i<=n;i++){
			for(int j=1;j<=p;j++){
				cin >> b[i][j];
			}
			sort(b[i]+1,b[i]+p+1);
		}
		memset(used,0,sizeof(used));
		int c = 0;
		for(int k=1;k<=2000000;k++){
			while(1){
				//0.9*k*a[i] ~ 1.1*k*a[i]
				for(int i=1;i<=n;i++){
					for(int j=1;j<=p;j++){
						if(9LL*k*a[i] <= 10LL*b[i][j] && 10LL*b[i][j] <=11LL*k*a[i] && !used[i][j]){
							goto ok;
						}
					}
					goto bad; ok:;
				}
				c++;
				for(int i=1;i<=n;i++){
					for(int j=1;j<=p;j++){
						if(9LL*k*a[i] <= 10LL*b[i][j] && 10LL*b[i][j] <=11LL*k*a[i] && !used[i][j]){
							used[i][j] = 1; break;
						}
					}
				}
				continue;
				bad:; break;
			}
			//if(k<=2) cout << c << endl;
		}
		printf("Case #%d: ",r);
		cout << c << endl;
	}
}
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
	for(int r=1;r<=t;r++){
		int hd,ad,hk,ak,b,d;
		cin >> hd >> ad >> hk >> ak >> b >> d;
		int ans = INF;
		for(int a=0;a<=100;a++){
			for(int c=0;c<=100;c++){
				int D1 = hd,A1 = ad,D2 = hk,A2 = ak;
				int q=0,r=0,cnt=0;
				for(int i=0;i<=1000;i++){
					if(i==1000) goto fail;
					if(q == a && r == c){
						cnt = i; break;
					}
					else if(q == a){
						if(D1 <= A2){
							D1 = hd;
							D1 -= A2;
						}
						else{
							A1 += b;
							D1 -= A2;
							r++;
						}
					}
					else{
						if(D1 <= max(0,A2-d)){
							D1 = hd;
							D1 -= A2;
						}
						else{
							A2 -= d; if(A2<0) A2 = 0;
							D1 -= A2;
							q++;
						}
					}
				}
				for(;;cnt++){
					if(cnt == 1000) goto fail;
					if(D2 == 0){
						ans = min(ans,cnt); break;
					}
					else{
						if(D2 > A1 && D1 <= A2){
							D1 = hd;
							D1 -= A2;
						}
						else{
							D2 -= A1; if(D2<0) D2 = 0;
							D1 -= A2;
						}
					}
				}
				fail:;
			}
		}
		printf("Case #%d: ",r);
		if(ans > 10000) puts("IMPOSSIBLE");
		else cout << ans << endl;
	}
}
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

#define pb push_back
#define ri(x) scanf("%d",&x)
#define rii(x,y) ri(x),ri(y)
#define ms(obj,val) memset(obj,val,sizeof(obj))
#define ms2(obj,val,sz) memset(obj,val,sizeof(obj[0])*sz)
#define FOR(i,f,t) for(int i=f;i<(int)t;i++)
#define FORR(i,f,t) for(int i=f;i>(int)t;i--)
#define EPS 1e-28
#define PI 2*acos(0.0)
#define y1 fdsadfa
typedef long long ll;
typedef vector<int> vi;

int T, n, k;
string N, ans;

int main(){
	cin >> T;
	FOR(t, 1, T+1){
		cin >> N;
		n = N.size();
		for(k = 1; k<n; k++) if(N[k] < N[k-1]) break;
		
		if (k == n) ans = N;
		else{
			for(k = k-1; k>0; k--) if(N[k]!=N[k-1]) break;
			if(N[k] != '1'){
				N[k]--;
				FOR(i, k+1, n) N[i] = '9';
				ans = N;
			} else{
				ans.resize(n-1);
				FOR(i, 0, n-1) ans[i] = '9';
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}

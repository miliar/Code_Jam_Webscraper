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


int T;
ll N, K, m, t, cM, cm, x, y;

int main(){
	cin >> T;
	
	FOR(tt, 1, T+1){
		
		cin >> N >> K;
		K--;
		t  = N;
		cM = 1;
		cm = 0;
		m  = 1;
		
		while(K>=m){
			K -= m;
			m *= 2;
			if(t&1) cM = 2*cM + cm;
			else    cm = 2*cm + cM;
			t = t/2;
		}
		
		if (K >= cM) t--;
		x = t/2, y = (t-1)/2;
		cout << "Case #" << tt << ": " << x << ' ' << y << endl;
	}
}

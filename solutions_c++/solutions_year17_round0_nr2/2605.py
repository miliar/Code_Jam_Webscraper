#include <iostream>
#include <cstdio>
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
#define rl(x) scanf("%lld",&x)
#define rll(x,y) rl(x),rl(y)
#define ms(obj,val) memset(obj,val,sizeof(obj))
#define ms2(obj,val,sz) memset(obj,val,sizeof(obj[0])*sz)
#define FOR(i,f,t) for(int i=f;i<(int)t;i++)
#define FORR(i,f,t) for(int i=f;i>(int)t;i--)

typedef long long ll;
typedef vector<int> vi;

const int MAXN=0;

string N;
bool good;
int T,L,pos;

int main() {
	cin>>T; FOR(t,1,T+1) {
		cin>>N;
		good=true;
		L=N.length();
		FOR(i,0,L-1) if(N[i]>N[i+1]) {
			pos=i;
			while(pos>=0 && N[pos]==N[i]) pos--;
			pos++;
			good=false;
			break;
		}
		if(!good) {
			N[pos]--;
			FOR(i,pos+1,L) N[i]='9';
		}
		printf("Case #%d: ",t);
		if(N[0]=='0') cout << N.substr(1,L-1) << endl;
		else cout << N << endl;
	}
}
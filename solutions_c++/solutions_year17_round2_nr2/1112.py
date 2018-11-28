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
#define ms(obj,val) memset(obj,val,sizeof(obj))
#define ms2(obj,val,sz) memset(obj,val,sizeof(obj[0])*sz)
#define FOR(i,f,t) for(int i=f;i<(int)t;i++)
#define FORR(i,f,t) for(int i=f;i>(int)t;i--)

typedef long long ll;
typedef vector<int> vi;

const int MAXN=1010;

map<int,char> mp;
int T,N;
pair<int,char> C[10];
char ans[MAXN];

int main() {
	cin>>T;
	FOR(t,1,T+1) {
		int c;
		cin >> N;
		FOR(i,0,N) ans[i]=0;
		cin >> c; C[0]={c,'R'};
		cin >> c; C[1]={c,'O'};
		cin >> c; C[2]={c,'Y'};
		cin >> c; C[3]={c,'G'};
		cin >> c; C[4]={c,'B'};
		cin >> c; C[5]={c,'V'};
		sort(C,C+6,greater<pair<int,char> >());
		if(C[0].first>N/2) {
			printf("Case #%d: IMPOSSIBLE\n",t);
			continue;
		}
		int i=0;
		while(C[0].first > 0) {
			ans[i]=C[0].second;
			C[0].first--;
			i+=2;
		}
		i--;
		while(C[1].first > 0 && i<N) {
			ans[i]=C[1].second;
			C[1].first--;
			i+=2;
		}
		i=1;
		while(C[1].first > 0) {
			ans[i]=C[1].second;
			C[1].first--;
			i+=2;
		}
		FOR(i,0,N) if(ans[i]==0) ans[i]=C[2].second;
		printf("Case #%d: ",t);
		FOR(i,0,N) printf("%c",ans[i]);
		printf("\n");
	}
}
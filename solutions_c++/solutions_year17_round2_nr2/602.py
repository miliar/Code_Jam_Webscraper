#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define PB push_back
#define GI ({int _x; scanf("%d",&_x); _x;})

typedef vector<string> VS;
template<class T> inline int size(const T&c) { return c.size(); }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

inline string calc(string first,int R,int Y,int B) {
	if(R<0 || Y<0 || B<0) return "";
	char last = first[size(first)-1];
	int N = R + Y + B;
	while(N > 0) {
		if(last=='R') {
			if(Y+B <= 0) return "";
			if(Y>B) { last = 'Y'; Y--; }
			else { last = 'B'; B--; }
		}else if(last=='Y') {
			if(R + B <= 0) return "";
			if(R>B) { last = 'R'; R--; }
			else { last = 'B'; B--; }
		}else {
			if(Y + R <= 0) return "";
			if(Y>R) { last = 'Y'; Y--; }
			else { last = 'R'; R--; }
		}
		first += last;
		N--;
	}
	if(first[0] == last) return "";
	return first;
}

int main() {
	OPEN("B");
	REP(nc,GI) {
		int N=GI;
		int R=GI;
		int O=GI;
		int Y=GI;
		int G=GI;
		int B=GI;
		int V=GI;

		// focus R Y B
		VS ans;
		ans.PB(calc("R",R-1,Y,B));
		ans.PB(calc("Y",R,Y-1,B));
		ans.PB(calc("B",R,Y,B-1));


		ans.PB(calc("RY",R-1,Y-1,B));
		ans.PB(calc("RB",R-1,Y,B-1));

		ans.PB(calc("YB",R,Y-1,B-1));
		ans.PB(calc("YR",R-1,Y-1,B));

		ans.PB(calc("BY",R,Y-1,B-1));
		ans.PB(calc("BR",R-1,Y,B-1));

		printf("Case #%d: ",nc+1);
		bool ok = false;
		REP(i,size(ans)) {
			if(size(ans[i])>0) {
				puts(ans[i].c_str());
				ok = true;
				break;
			}
		}
		if(!ok) puts("IMPOSSIBLE");
	}
	return 0;
}

#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iterator>
#include <map>
#include <string>
#include <cstdio>
#include <sstream>
#include <utility>
 
using namespace std;
 
#define lld long long int
#define REP(i,n) for (lld i = 0; i < (lld)n; i++)
#define REPD(i,n) for (lld i = (lld)n; i >= 0; i--)
#define FOR(i,a,b) for (lld i = (lld)a; i <= (lld)b; i++)
#define FORD(i,a,b) for (lld i = (lld)b; i >= (lld)a; i--)
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define RESET(a,x) memset(a,x,sizeof(a))
#define EXIST(a,s) ((s).find(a) != (s).end())
#define MX(a,b) a = max((a),(b));
#define MN(a,b) a = min((a),(b));
#define VC(a) vector< a >
#define PR(a,b) pair<a, b>
#define sc second
#define ft first
lld N;
vector< pair<string, lld> > all;
 
lld toNum(string str) {
    lld rs;
    stringstream ss(str);
    ss >> rs;
    return rs;
}
 
string toStr(lld n) {
    stringstream ss;
    ss << n;
    return ss.str();
}
 
string bstr(string m, lld n) {
    string rs="";
    REP(i, n) {
        rs+=m;
    }
    return rs;
}
 
bool isTidy(lld n) {
    string c=to_string(n);
    REP(i,c.length()-1)
        if ((lld)c[i] > (lld)c[i+1]) return false;
    return true;
}
 
void solve(lld idx, lld n) {
    lld ans=n;
 
    if (n>=10||!isTidy(n)) {
        while(!isTidy(ans)) {
            string c=to_string(ans);
            REP(i,c.length()-1) {
                if ((lld)c[i] > (lld)c[i+1]) {
                    string gb = c.substr(0,i);
                    lld t=toNum(string(1,c[i]))-1;
                    if (t==0&&i!=0)
                        gb.replace(gb.end()-1,gb.end(),string(1,gb[gb.length()-1]));
                    gb+=toStr(t)+bstr("9", (lld)c.length()-i-1); //last number always 9, build it
                    ans=toNum(gb);
                    break;
                }
            }
        }
    }
 	if(idx+1 == N)
    printf("Case #%lld: %lld", idx+1, ans);
	else
		    printf("Case #%lld: %lld\n", idx+1, ans);

}
 
int main(int argc, char *argv[]) {
    lld inp;
 
    scanf("%lld", &N);
 
    REP(i,N) {
        scanf("%lld", &inp);
        solve(i, inp);
    }
}
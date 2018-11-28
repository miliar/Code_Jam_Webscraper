#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<string>
using namespace std;
#define LL long long

void impossible(int t) {
    printf("Case #%d: IMPOSSIBLE\n",t);
}

string getO(int k) {
    string ret = "";
    for (int i=0; i<k; i++) ret += "OB";
    return ret;
}

string getG(int k) {
    string ret = "";
    for (int i=0; i<k; i++) ret += "GR";
    return ret;
}

string getV(int k) {
    string ret = "";
    for (int i=0; i<k; i++) ret += "VY";
    return ret;
}

int main() {
    int tc;
    scanf("%d",&tc);
    for (int t=1; t<=tc; t++) {
        int n,r,o,y,g,b,v;
        scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
        if (o >= b && o > 0) {
            if (b == o && n == b*2) { printf("Case #%d: %s\n",t,getO(o).c_str()); }
            else impossible(t);
            continue;
        }
        else b -= o;
        if (g >= r && g > 0) {
            if (g == r && n == r*2) { printf("Case #%d: %s\n",t,getG(g).c_str()); }
            else impossible(t);
            continue;
        }
        else r -= g;
        if (v >= y && v > 0) {
            if (v == y && n == y*2) { printf("Case #%d: %s\n",t,getV(v).c_str()); }
            else impossible(t);
            continue;
        }
        else y -= v;

        int pn = b+r+y;
        if ((b > pn/2) || (r > pn/2) || (y > pn/2)) { impossible(t); continue; }
        string str = "";
        char last = '.';
        while (pn--) {
            if (last == 'B') {
                if (r >= y) { last = 'R'; r--; }
                else { last = 'Y'; y--; }
            }
            else if (last == 'R') {
                if (b >= y) { last = 'B'; b--; }
                else { last = 'Y'; y--; }
            }
            else {
                if (b >= r) { last = 'B'; b--; }
                else { last = 'R'; r--; }
            }
            str += last;
        }
        if (o > 0) {
            str.replace(str.find("B"),1,"B"+getO(o));
        }
        if (g > 0) {
            str.replace(str.find("R"),1,"R"+getG(g));
        }
        if (v > 0) {
            str.replace(str.find("Y"),1,"Y"+getV(v));
        }
        printf("Case #%d: %s\n",t,str.c_str());

    }
	return 0;
}

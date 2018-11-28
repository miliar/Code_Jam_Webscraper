#include <bits/stdc++.h>

using namespace std;

#define fs first
#define sc second

pair <int,int> a[3];
int R, G, B, O, Y, V;

char change(int x) {
    if (x==0) return 'R';
    if (x==1) return 'Y';
    return 'B';
}

void go(string & s, int idx, char u) {
    string k = "";
    k += u;
    s.insert(idx,k);
}

void solve() {
    a[0].fs = R; a[0].sc = 0;
    a[1].fs = Y; a[1].sc = 1;
    a[2].fs = B; a[2].sc = 2;
    sort(a,a+3);
    string s = "";
    for (int i = 0; i < a[2].fs; ++i)
        s.push_back(change(a[2].sc));
    for (int i = 0; a[1].fs; i+=2) {
        char k = change(a[1].sc);
        go(s,i,k);
        a[1].fs--;
    }
    for (int i = s.size()-1; a[0].fs; i--) {
        char k = change(a[0].sc);
        a[0].fs--;
        go(s,i,k);
    }
    for (int i = 0; i < (int)s.size(); ++i)
    if (s[i]==s[(i+1)%s.size()]) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    cout << s << endl;
}

int main() {
	freopen("B-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);
    int t; scanf("%d",&t); int te = t;
    while (t--) {
        int cxcx;
        scanf("%d%d%d%d%d%d%d",&cxcx,&R,&O,&Y,&G,&B,&V);
        printf("Case #%d: ",te-t);
        solve();
    }
	return 0;
}

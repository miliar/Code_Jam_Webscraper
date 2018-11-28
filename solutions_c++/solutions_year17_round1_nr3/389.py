#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>

#define REP(i,n) for(int i=0;i<(n);i++)
#define TR(i,x) for(__typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))
#define SIZE(x) (int)(x).size()

#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

const int MAXN = 105;

struct Node {
    int Hd, Ad, Hk, Ak, d;
    Node() {}
    Node(int Hd, int Ad, int Hk, int Ak, int d):Hd(Hd),Ad(Ad),Hk(Hk),Ak(Ak), d(d){}
};

int mk[MAXN][MAXN][MAXN][MAXN];

void Solve() {
    int Hd, Ad, Hk, Ak, B, D;
    cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
    queue<Node> Q;
    Q.push(Node(Hd, Ad, Hk, Ak, 0));
    CLEAR(mk);
    int ans = -1;
    while (!Q.empty()) {
        Node a = Q.front();
        Q.pop();
        if (a.Hk - a.Ad <= 0) {
            ans = a.d + 1;
            break;
        }
        //attack
        Node b = Node(a.Hd - a.Ak, a.Ad, a.Hk - a.Ad, a.Ak, a.d + 1);
        if (b.Hd > 0 && !mk[b.Hd][b.Ad][b.Hk][b.Ak]) {
            mk[b.Hd][b.Ad][b.Hk][b.Ak] = true;
            Q.push(b);
        }
        //buff
        if (a.Ad < a.Hk && B) {
            int Ad = a.Ad + B;
            b = Node(a.Hd - a.Ak, Ad, a.Hk, a.Ak, a.d + 1);
            if (b.Hd > 0 && !mk[b.Hd][b.Ad][b.Hk][b.Ak]) {
                mk[b.Hd][b.Ad][b.Hk][b.Ak] = true;
                Q.push(b);
            }
        }
        //debuff
        if (a.Ak > 0 && D) {
            int Ak = max(a.Ak - D, 0);
            b = Node(a.Hd - Ak, a.Ad, a.Hk, Ak, a.d + 1);
            if (b.Hd > 0 && !mk[b.Hd][b.Ad][b.Hk][b.Ak]) {
                mk[b.Hd][b.Ad][b.Hk][b.Ak] = true;
                Q.push(b);
            }
        }
        //cure
        if (a.Hd < Hd) {
            b = Node(Hd - a.Ak, a.Ad, a.Hk, a.Ak, a.d + 1);
            if (b.Hd > 0 && !mk[b.Hd][b.Ad][b.Hk][b.Ak]) {
                mk[b.Hd][b.Ad][b.Hk][b.Ak] = true;
                Q.push(b);
            }
        }
    }
    if (ans == -1) {
        puts("IMPOSSIBLE");
    } else {
        cout << ans << endl;
    }
}

int main() {
   // freopen("C.in","r",stdin);
  //  	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
    	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
    //	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
    //	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
    int cas;
    cin >> cas;
    for (int T = 1; T <= cas; ++T) {
        printf("Case #%d: ", T);
        Solve();
        cerr << "Case #" << T << ": done!" << endl;
    }
    return 0;
}


#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair <int, int> pii;
typedef vector<int> vi;

#define mp make_pair
#define pb push_back

#define FOR(i, a, b) for (int i=a; i<b; i++)
#define F0R(i, a) for (int i=0; i<a; i++)
 
#define f first
#define s second
#define lb lower_bound
#define ub upper_bound
#define endl "\n"
 
const int MOD = 1000000007;
double PI = 4*atan(1);

pair<ll,ll> debuff[101], buff[101][101]; // correct

ll Hd, Ad, Hk, Ak, B, D, ans = MOD; 

void sim(int i, int j) {
    pair<ll,ll> stor = buff[i][j];
    ll Hk1 = Hk;
    while (Hk1 > 0) {
        int co = 0;
        if (Hk1 - (Ad+j*B) <= 0) {
            buff[i][j].f ++;
            break;
        }
        while (buff[i][j].s-(Ak-i*D) <= 0) {
            buff[i][j] = {buff[i][j].f+1,Hd-(Ak-i*D)}; co++;
            if (buff[i][j].s <= 0 || co>1) {
                buff[i][j] = stor;
                return;
            }
        }
        buff[i][j] = {buff[i][j].f+1,buff[i][j].s-max(Ak-i*D,(ll)0)};
        Hk1 -= (Ad+j*B);
    }
    ans = min(ans,buff[i][j].f);
    buff[i][j] = stor;
}

void solve() {
    debuff[0] = {0,Hd};
    int i = 1;
    for (; i <= 100; ++i) {
        debuff[i] = debuff[i-1];
        int co = 0, flag = 0;
        while (debuff[i].s-(Ak-i*D) <= 0) {
            debuff[i] = {debuff[i].f+1,Hd-(Ak-(i-1)*D)}; co++;
            if (debuff[i].s <= 0 || co>1) {flag = 1; break;}
        }
        if (flag == 1) { i--; break;}
        debuff[i] = {debuff[i].f+1,debuff[i].s-max(Ak-i*D,(ll)0)};
    }
    int i1 = min(i,100);
    for (i = 0; i <= i1; ++i) {
        buff[i][0] = debuff[i];
        sim(i,0);
        FOR(j,1,101) {
            buff[i][j] = buff[i][j-1];
            int co = 0, flag = 0;
            while (buff[i][j].s-(Ak-i*D) <= 0) {
                buff[i][j] = {buff[i][j].f+1,Hd-(Ak-i*D)};
                co++;
                if (buff[i][j].s <= 0 || co>1) {flag = 1; break;}
            }
            if (flag) break;
            buff[i][j] = {buff[i][j].f+1,buff[i][j].s-max(Ak-i*D,(ll)0)};
            sim(i,j);
        }
    }
}

int main() { 
	int T; cin >> T;
	F0R(i,T) {
		cout << "Case #" << (i+1) << ": ";
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		ans = MOD; solve();
		if (ans == MOD) cout << "IMPOSSIBLE\n";
		else cout << ans << "\n";
	}
} // correct
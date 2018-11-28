#include <bits/stdc++.h>
using namespace std;

#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define REPD(i,a,b) for (int i = (a); i >= (b); --i)
#define FORI(i,n) REP(i,1,n
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (auto i = t.begin(); i != t.end(); ++i)
#define fi first
#define se second

int plan[1445];
pair<int,bool> dp[1441][721][3][3];

void init() {
    FOR(i,1441)
        FOR(j,721)
            FOR(k,3)
                FOR(h,3)
                    dp[i][j][k][h]=mp(-1,true);
}

pair<int,bool> f(int i, int jt, int last, int starting) {
    if (jt > 720) {
        return mp(0,false);
    }
    if (i == 1440) {
        if (jt == 720) {
            if (starting == last)
                return mp(0,true);
            else
                return mp(1,true);
        }
        else
            return mp(0,false);
    }
    if (dp[i][jt][last][starting].fi != -1)
        return dp[i][jt][last][starting];

    if (plan[i] != 0) {
        if (plan[i] == 1) {
            if (last == 1)
                return dp[i][jt][last][starting] = f(i+1,jt+1,1,starting);
            else if (last == 2) {
                auto o = f(i+1,jt+1,1,starting);
                return dp[i][jt][last][starting] = mp(1+o.fi,o.se);
            }
            else if (last == 0)
                return dp[i][jt][last][starting] = f(i+1,jt+1,1,1);
        } else if(plan[i] == 2) {
            if (last == 1) {
                auto o = f(i+1,jt,2,starting);
                return dp[i][jt][last][starting] = mp(1+o.fi,o.se);
            } else if (last == 2)
                return dp[i][jt][last][starting] = f(i+1,jt,2,starting);
            else if (last == 0)
                return dp[i][jt][last][starting] = f(i+1,jt,2,2);
        }
    } else {
        pair<int,bool> o1,o2;
        if (last == 1) {
            // put 1
            o1 = f(i+1,jt+1,1,starting);
            // put 2
            auto o = f(i+1,jt,2,starting);
            o2 = mp(1+o.fi,o.se);
        } else if (last == 2) {
            // put 1
            auto o = f(i+1,jt+1,1,starting);
            o1 = mp(1+o.fi,o.se);
            // put 2
            o2 = f(i+1,jt,2,starting);
        } else {
            o1 = f(i+1,jt+1,1,1);
            o2 = f(i+1,jt,2,2);
        }
        if (!o1.se && !o2.se)
            return dp[i][jt][last][starting] = mp(0,false);
        else if (!o1.se)
            return dp[i][jt][last][starting] = o2;
        else if (!o2.se)
            return dp[i][jt][last][starting] = o1;
        else if (o1.fi < o2.fi)
            return dp[i][jt][last][starting] = o1;
        else
            return dp[i][jt][last][starting] = o2;
    }
}

int main() {
    freopen("./2017/Round 1C/B-large.in", "r", stdin);
    freopen("./2017/Round 1C/B-large.out", "w", stdout);
	int T;
	cin >> T;
    int AC, AJ;
    int x,y;
	FOR(t,T) {
	    FOR(i,1445) {
	        plan[i] = 0;
	    }
        cin >> AC >> AJ;
        FOR(i,AC) {
            cin >> x >> y;
            while(x < y) {
                plan[x] = 1;
                x++;
            }
        }
        FOR(i,AJ) {
            cin >> x >> y;
            while(x < y) {
                plan[x] = 2;
                x++;
            }
        }
		cout << "Case #" << t+1 << ": ";
		init();
		cout << f(0,0,0,0).fi;
		cout << endl;
	}
	return 0;
}

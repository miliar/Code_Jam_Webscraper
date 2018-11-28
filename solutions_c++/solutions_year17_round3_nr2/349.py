#include <bits/stdc++.h>
using namespace std;
struct pe {
    int st, ed, ty;
    pe(){}
    pe(int _st, int _ed, int _ty): st(_st), ed(_ed), ty(_ty) {}
    bool operator < (const pe &o)const {
        return st < o.st;
    }
}in[1005];
struct inter {
    int v;
    inter(){}
    inter(int _v): v(_v) {}
    bool operator < (const inter &o)const {
        return v > o.v;
    }
};
int n, k;
int start[1005], end[1005];

void solve(int Case) {
    int ac, aj;
    priority_queue<inter> Q1, Q2;
    cin >> ac >> aj;
    int last = 0;
    int t1 = 0, t2 = 0;
    for (int i = 0; i < ac; i++) {
        cin >> in[last].st >> in[last].ed;
        t1 += in[last].ed - in[last].st;
        in[last++].ty = 1;
    }

    for (int i = 0; i < aj; i++) {
        cin >> in[last].st >> in[last].ed;
        t2 += in[last].ed - in[last].st;
        in[last++].ty = 2;
    }

    sort(in,in+last);

    /*for (int i=0; i<last; i++) {
        cout << in[i].st << " " << in[i].ed << " " << in[i].ty << "\n";
    }*/
    int ans = 0;
    for (int i=0; i<last; i++) {
        if(i < last-1) {
            if(in[i].ty == in[i+1].ty) {
                ans += 2;
                if(in[i].ty == 1) {
                    Q1.push(inter(in[i+1].st-in[i].ed));
                } else {
                    Q2.push(inter(in[i+1].st-in[i].ed));
                }
            } else {
                ans += 1;
            }
        } else {
            if(in[i].ty == in[0].ty) {
                ans += 2;
                if(in[i].ty == 1) {
                    Q1.push(inter(in[0].st + 1440 - in[i].ed));
                } else {
                    Q2.push(inter(in[0].st + 1440 - in[i].ed));
                }
            } else {
                ans += 1;
            }
        }
    }

    while(!Q1.empty()) {
        if (t1 + Q1.top().v > 720) break;
        t1 += Q1.top().v;
        ans -= 2;
        Q1.pop();
    }

    while(!Q2.empty()) {
        if (t2 + Q2.top().v > 720) break;
        t2 += Q2.top().v;
        ans -= 2;
        Q2.pop();
    }

    cout << "Case #" << (Case+1) <<": " << ans << "\n";
    //printf("%lf\n", ans);
}

int main () {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int i=0;i<T;i++) solve(i);
}

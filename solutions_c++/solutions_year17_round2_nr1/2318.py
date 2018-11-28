#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <deque>
using namespace std;

deque<long long> label, num;
/*
void debug() {
    if(label.size() != num.size()) {
        cout << "size not same" << endl;
        return;
    }
    cout << "hehe" << endl;
    for(int i = 0;i < label.size();i ++) {
        cout << label.at(i) << " " << num.at(i) << endl;
    }
}
*/


int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    int casenum;  scanf("%d", &casenum);
    for(int cs = 1; cs <= casenum; cs ++) {
        int D, N; scanf("%d%d", &D, &N);
        double t = 0.0;
        for(int i = 0;i < N;i ++) {
            int s, v; scanf("%d%d", &s, &v);
            double tt = ((double)(D - s)) / v;
            if(t < tt) t = tt;
        }
        printf("Case #%d: %f\n", cs, D / t);
    }
    return 0;
}




#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

#include <queue>
#include<cmath>;

double pi = acos(-1);
int n, k;
struct Node {
    double r, h;
};

bool cmp1(Node a, Node b) {
    return a.r > b.r;
}

bool cmp2(Node a, Node b) {
    return a.h * a.r > b.h * b.r;
}

vector<Node> vec;

double getans(int id, int n, int k) {
    vector<Node> tmp;
    tmp.clear();
    double sum = pi * vec[id].r * vec[id].r + vec[id].r * vec[id].h * 2 * pi;
    for (int i = id + 1; i < n; i++) {
        tmp.push_back(vec[i]);
    }
    if (tmp.size() < k - 1) return 0;
    sort(tmp.begin(), tmp.end(), cmp2);
    for (int i = 0; i < k - 1; i++) {
        sum += tmp[i].r * tmp[i].h * 2 * pi;
    }
    return sum;
}

int main() {
    freopen("../A-large.in","r",stdin);
    freopen("../A-large.out","w",stdout);
    int cas = 1;
    int T;
    cin >> T;
    while (T--) {
        vec.clear();
        printf("Case #%d: ", cas++);
        cin >> n >> k;
        for (int i = 1; i <= n; i++) {
            double r, h;
            cin >> r >> h;
            Node a;
            a.r = r;
            a.h = h;
            vec.push_back(a);
        }
        sort(vec.begin(), vec.end(), cmp1);
        double ans = 0;
        for (int i = 0; i < n; i++) {
            ans = max(ans, getans(i, n, k));
        }
        printf("%.10f\n", ans);
    }


}
//3 1 4 1
/*
 *
 11
10
1 2 7 10 3 4 5 6 8 9
1 6 9 8 2 7 10 3 5 4
 */
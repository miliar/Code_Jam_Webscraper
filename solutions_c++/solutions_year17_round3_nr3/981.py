#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const double eps = 1e-10;
const double pi = acos(-1);
const int N = 1e6+10;
int cas = 1, n, k;

double u, p[N];

bool gt(double a, double b){
    return a > b + eps;
}

bool le(double a, double b){
    return gt(b, a) || fabs(a - b) < eps;
}

int check(double x){
    double sum = 0;
    for(int i=0;i<k;i++){
        sum += (x - p[i]);
    }
    if(gt(sum, u)) return 1;
    if(fabs(sum - u) < eps) return 0;
    return -1;
}

double calc(int x){
    double ret = 0;
    for(int i=0;i<x;i++){
        ret += p[x] - p[i];
    }
    return ret;
}

double solve(){
    sort(p, p+n);
    double s = 0;
    for(int i=0;i<n;i++){
        double t = calc(i);
        if(le(t, u)) k = i+1;
        else break;
    }

    for(int i=0;i<n;i++){
        s += (1 - p[i]);
    }
    if(le(s, u)) return 1.0;
    double l = 0, r = 1.0, y;
    while( true ){
        double m = ( l + r) / 2;
        int f = check(m);
        if(f > 0) r = m;
        else if( f < 0) l = m;
        else {
            y = m;
            break;
        }
    }
   //  cout << y << endl;
    double ans = 1;
    for(int i=0;i<n;i++){
        if(i < k) ans *= y;
        else ans *= p[i];
    }
    return ans;
}

int main(){
    freopen("C-small-1-attempt2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    while(T--){
        cin >> n >> k;
        cin >> u;
        for(int i=0;i<n;i++){
            cin >> p[i];
        }
        printf("Case #%d: %.6f\n", cas++, solve());
    }
    return 0;
}


#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pii pair<int, int>
#define X first
#define Y second
#define pb push_back
#define mp make_pair

int T;

const int maxN = 1e3+5;
const double EPS = 1e-9;

const double PI = 2*acos(0);


struct node{
    int x, y;
    double z;
};

int n, k;
double ret = 0.0;
node val[maxN];

bool compare(node a, node b){
    if(abs(a.z - b.z) <= EPS){
        return a.x > b.x;
    }
    return a.z > b.z;
}

void solve_test(){
    cin>>n>>k;
    ret = 0;
    for(int i = 0; i < n; i++){
        cin>>val[i].x>>val[i].y;
        val[i].z = 2*PI*val[i].x*val[i].y;
    }
    sort(val, val + n, compare);

    for(int i = 0; i < n; i++){
        int vlarg = val[i].x;

        double tmp = PI*vlarg*vlarg + val[i].z;
        int j = 0, tmpk = 1;
        for(j; tmpk < k && j < n;j++){
            if(val[j].x <= vlarg && j != i){
                tmp += val[j].z;
                tmpk++;
            }
        }
        if(tmpk >= k){
            ret = max(ret, tmp);
        }
    }

    printf("%.9f\n", ret);
}


int main(){
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    //ios::sync_with_stdio(false);
    cin>>T;
    for(int t = 1; t <= T; t++){
        cout<<"Case #"<<t<<": ";
        solve_test();
    }
    return 0;
}

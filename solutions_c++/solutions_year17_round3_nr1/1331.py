#include <bits/stdc++.h>
using namespace std;
struct data{
    double ra, he;
    bool operator < (const data &r){
        if(ra == r.ra) return he < r.he;
        return ra > r.ra;
    }
}a[1010];
double D[1010][1010], max1[1010][1010];
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    double pi = 3.14159265358979;
    int i, j, N, M, T;
    cin>>T;
    for(int t=1; t<=T; t++){
        cin>>N>>M;
        for(i=0; i<=N; i++) {
            a[i].ra = a[i].he = 0;
            for(j=0; j<=N; j++){
                D[i][j] = max1[i][j] = 0;
            }
        }
        for(i=1; i<=N; i++){
            cin>>a[i].ra>>a[i].he;
        }
        sort(a+1, a+N+1);
        double ans = 0;
        for(i=1; i<=M; i++){
            for(j=i; j<=N; j++){
                if(i == 1) D[i][j] = a[j].ra * a[j].ra * pi;
                D[i][j] += max1[i-1][j-1] + a[j].ra * a[j].he * pi * 2;
                max1[i][j] = max(max1[i][j-1], D[i][j]);
            }
        }
        ans = max1[M][N];
        printf("Case #%d: %.12lf\n", t, ans);
    }
}

# include <bits/stdc++.h>
using namespace std;

struct cylinder{
    double r, h;
    bool operator < (const cylinder &n) const{
        return r > n.r;
    }
};

double ks[1000][1000];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large-out.txt", "w", stdout);
    int cases, caseno=0, n, k;
    cin >> cases;
    double pi = acos(-1.0), r, h, circleArea, curvedSurfaceArea, area;
    cylinder panCake;
    while(cases--){
        cin >> n >> k;
        vector <cylinder> panCakes;
        for (int i=0; i<n; i++){
            cin >> panCake.r >> panCake.h;
            panCakes.push_back(panCake);
        }
        sort(panCakes.begin(), panCakes.end());
        r = panCakes[0].r;
        h = panCakes[0].h;
        circleArea = pi*r*r;
        curvedSurfaceArea = 2*pi*r*h;
        area = circleArea + curvedSurfaceArea;
        for (int i=0; i<k; i++) ks[0][i] = area;
        for (int i=1; i<n; i++){
            r = panCakes[i].r;
            h = panCakes[i].h;
            circleArea = pi*r*r;
            curvedSurfaceArea = 2*pi*r*h;
            area = circleArea + curvedSurfaceArea;
            ks[i][0] = max(ks[i-1][0], area);
        }
        for (int i=1; i<n; i++){
            r = panCakes[i].r;
            h = panCakes[i].h;
            curvedSurfaceArea = 2*pi*r*h;
            for (int j=1; j<k; j++){
                ks[i][j] = max(ks[i-1][j], ks[i-1][j-1]+curvedSurfaceArea);
            }
        }
        printf("Case #%d: %0.9lf\n", ++caseno, ks[n-1][k-1]);
    }
}

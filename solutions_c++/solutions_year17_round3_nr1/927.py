#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const double PI = acos(-1.0);

struct Pancake{
    Pancake(){}
    Pancake(double _radius, double _height): radius(_radius), height(_height){
        sideArea = 2.0 * PI * radius * height;
        faceArea = radius * radius * PI;
    }

    bool operator < (const Pancake &p) const{
        if(radius != p.radius){
            return radius > p.radius;
        }
        return height > p.height;
    }

    double radius;
    double height;
    double sideArea;
    double faceArea;
};

double dp[1010][1010];

int main(void){
    int tt;
    int n, k;
    scanf("%d", &tt);
    for(int tc = 1; tc <= tt; tc++){
        vector<Pancake> pancakes;
        int r, h;
        scanf("%d %d", &n, &k);
        for(int i = 0; i < n; i++){
            scanf("%d %d", &r, &h);
            pancakes.push_back(Pancake((double)r, (double)h));
        }
        sort(pancakes.begin(), pancakes.end());

        memset(dp, 0, sizeof(dp));
        for(int j = 0; j < n; j++){
            dp[1][j] = pancakes[j].sideArea + pancakes[j].faceArea;
        }
        for(int i = 1; i <= k; i++){
            for(int j = 0; j < n; j++){
                for(int k = j+1; k < n; k++){
                    dp[i+1][k] = max(dp[i+1][k], dp[i][j] + pancakes[k].sideArea);
                }
            }
        }

        double ans = 0.0;
        for(int j = 0; j < n; j++){
            ans = max(ans, dp[k][j]);
        }
        printf("Case #%d: %.9f\n", tc, ans);
    }
    return 0;
}

#include<cstdio>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

const double pi = acos(-1);

struct cake{
    double top, side;
    bool operator<(const cake& c) const { return side > c.side;}
};

int main (){
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++){
        vector<cake> v;
        int N, K;
        scanf("%d%d", &N, &K);
        for (int i=0;i<N;i++){
            int R, H;
            scanf("%d%d", &R, &H);
            v.push_back({pi*(double)R*(double)R, 2.0*pi*(double)R*(double)H});
        }
        sort(v.begin(), v.end());

        double max_top = 0, sum = 0;
        for (int i=0;i<K;i++){
            sum += v[i].side;
            if (v[i].top > max_top)
                max_top = v[i].top;
        }

        int min_side = K-1;
        for (int i=K;i<N;i++){
            if (v[i].top > max_top){
                if ((v[i].top - max_top) > (v[min_side].side - v[i].side)){
                    sum -= v[min_side].side - v[i].side;
                    max_top = v[i].top;
                    min_side = i;
                }
            }
        }
        printf("Case #%d: %.9f\n", t, sum + max_top);
    }
}

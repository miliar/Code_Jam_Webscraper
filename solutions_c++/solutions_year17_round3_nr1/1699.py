#include <bits/stdc++.h>
#include <math.h>
#define PI 3.14159265358979323846
using namespace std;
struct Data{
    double r;
    double h;
    double a;
    double v;
    bool operator<(const Data& rhs) const {
        return r < rhs.r;
    }
};
int main(){
    int tc;
    scanf("%d",&tc);
    for(int t = 1; t <= tc; t++){
        int N, K;
        scanf("%d%d",&N,&K);
        Data data[2000];
        double ans[2001][2];
        for(int i = 0; i < N; i++){
            double r,h,a,v;
            scanf("%lf%lf",&r,&h);
            a = PI*r*r;
            v = 2.0*PI*h*r;
            data[i] = Data{r, h, a, v};

        }
        sort(data, data + N);
        int index = 0;
        int next;
        next = (index+1)%2;
        for(int i = 0; i < N; i++){
            ans[i][next] = data[i].v;
            //printf("%f\n",data[i].r);
        }
        index = next;

        for(int k = 2; k <= K; k++){
            next = (index+1)%2;
            double add = ans[k-2][index];
            for(int i = k-1; i < N; i++){
                ans[i][next] = data[i].v + add;

                if(ans[i][index] > add){
                    add = ans[i][index];
                }
            }
            index = next;
        }
        double answer = -INFINITY;
        for(int i = K-1; i < N;i++){
            answer = max(answer, ans[i][next] + data[i].a);
        }

        printf("Case #%d: ",t);
        printf("%f\n", answer);

    }
    return 0;
}

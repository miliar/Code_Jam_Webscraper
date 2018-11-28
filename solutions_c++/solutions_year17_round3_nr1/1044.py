#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

struct cake{
    int h, r;
    double surface, top;
    bool operator<(const cake& right) const{
        return surface > right.surface;
    }
    void getSurface(){
        surface = M_PI*2*r*h;
    }
    void getTop(){
        top = M_PI*r*r;
    }
};

int main(){
    int T, N, K;
    std::vector<cake> v;
  scanf("%d\n", &T);
  int t = 1;
  while(t < T+1){
    scanf("%d %d", &N, &K);
    v.resize(N);
    for(int i = 0; i < N; i++){
        scanf("%d %d", &v[i].r, &v[i].h);
        v[i].getSurface();
        v[i].getTop();
    }
    std::sort(v.begin(), v.end());
    double ans = 0;
    double maxtop = 0;
    double minsurface = v[K-1].surface;
    for(int i = 0; i < K; i++){
        ans += v[i].surface;
        if(v[i].top > maxtop)
            maxtop = v[i].top;
    }
    ans += maxtop;
    for(int i = K; i < N; i++){
        if((v[i].top - maxtop) + (v[i].surface - minsurface) > 0){
            ans += (v[i].top - maxtop) + (v[i].surface - minsurface);
            maxtop = v[i].top;
            minsurface = v[i].surface;
        }
    }
    printf("Case #%d: %lf\n", t, ans);
    t++;
  }
}

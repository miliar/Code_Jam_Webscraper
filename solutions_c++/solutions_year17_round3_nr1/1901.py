#include <iostream>
#include <vector>
#include <algorithm>
double pi = 3.14159265359;
using namespace std;

struct pan{
    int R;
    int H;
    double Hv;
    double Vv;
};

int main() {
    int T; cin>>T;
    for (int tt=1;tt<=T;tt++) {
        int N,K;cin>>N>>K;
        vector<pan> v(N);
        for (int i = 0; i < N; i++) {
            cin>>v[i].R>>v[i].H;
            v[i].Hv = (double)v[i].H * (double)v[i].R * 2.0;
            v[i].Vv = (double)v[i].R * (double)v[i].R + v[i].Hv;
        }
        double rs = 0;
        for (int i = 0; i < N; i++) {
            vector<int> st;
            for (int j=0; j<N;j++){
                if (i!=j && v[j].R <= v[i].R) {
                    st.push_back(j);
                }
            }
            if (st.size() < K-1) {
                continue;
            }
            sort(st.begin(), st.end(), [v](const int& a, const int& b){
                    return v[a].Hv > v[b].Hv;
                    });
            double max_t = v[i].Vv;
            for (int j=0; j<K-1;j++) {
                max_t += v[st[j]].Hv;
            }
            rs = max(rs, max_t);
        }
        rs *= pi;
        printf ("Case #%d: %f\n",tt,rs);
    }
}

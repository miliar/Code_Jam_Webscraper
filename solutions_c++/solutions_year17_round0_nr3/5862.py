#include<iostream>
#include<vector>
using namespace std;
struct bath {
    int l,r;
    bool occupied;
    int Min, Max;
};
bath B[1003];
int K, N;
int choose() {
    int Max = -1;
    for (int i = 1; i <= N; ++i) {
        if (!B[i].occupied && B[i].Min > Max) Max = B[i].Min;
    }
    vector<int> V;
    for (int i = 1; i <= N; ++i) {
        if (!B[i].occupied && B[i].Min == Max) V.push_back(i);
    }
    if (V.size() == 1) return V[0];
    Max = -1;
    for (int i = 0; i < V.size(); ++i) {
        if (B[V[i]].Max > Max) Max = B[V[i]].Max;
    }
    for (int i = 0; i < V.size(); ++i) {
        if (B[V[i]].Max == Max) return V[i];
    }
}
void update() {
    for (int i = 1; i <= N; ++i) {
        if (B[i].occupied) continue;
        int k = 1;
        while (!B[i - k].occupied) k++;
        B[i].l = k - 1;
        k = 1;
        while (!B[i + k].occupied) k++;
        B[i].r = k - 1;
        B[i].Min = B[i].l < B[i].r ? B[i].l : B[i].r;
        B[i].Max = B[i].l < B[i].r ? B[i].r : B[i].l;
    }
}
int main() {
    int n;
    cin >> n;
    for (int ca = 1; ca <= n; ++ca) {
        cin >> N >> K;
        B[0].occupied = true;
        B[N + 1].occupied = true;
        for (int i = 1; i <= N; ++i) B[i].occupied = false;
        update();
        for (int i = 1; i <= K - 1; ++i) {
            int k = choose();
            B[k].occupied = true;
            update();
        }
        int k = choose();
        cout << "Case #" << ca << ": " << B[k].Max << ' ' << B[k].Min << endl;
    }
}
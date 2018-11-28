#include<bits/stdc++.h>
using namespace std;

int N, P;

vector<int> R;
vector<vector<int> > H;

void main2(int tc) {
    scanf("%d %d", &N, &P);

    R.clear();
    R.resize(N);

    for(int i = 0; i < N; i++) {
        scanf("%d", &R[i]);
    }

    H.clear();
    H = vector<vector<int> >(N, vector<int>(P));

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < P; j++) {
            scanf("%d", &H[i][j]);
        }
    }

    for(int i = 0; i < N; i++) {
        sort(H[i].begin(), H[i].end());
    }

    int s = 1, ans = 0;
    vector<int> pos(N, 0);

    while(1) {

        //cout << s << endl;

        bool term = false;

        for(int i = 0; i < N; i++) {
            if(pos[i] == P) {
                term = true;
                break;
            }
        }
        if(term) break;

        bool con = false;
        for(int i = 0; i < N; i++) {
            if((long long)11*R[i]*s/10 < H[i][ pos[i] ]) {
                s++;
                con = true;
                break;
            }
        }
        if(con) continue;

        for(int i = 0; i < N; i++) {
            if(H[i][ pos[i] ] < (long long)9*R[i]*s/10) {
                pos[i]++;
                con = true;
                break;
            }
        }
        if(con) continue;

        ans++;

        for(int i = 0; i < N; i++) {
            pos[i]++;
        }
    }
    printf("Case #%d: %d\n", tc, ans);
}

int TC;
int main() {

    freopen("inB.txt", "r", stdin);
    freopen("outB.txt", "w", stdout);

    scanf("%d", &TC);
    for(int i = 1; i <= TC; i++) main2(i);
}

#include<cstdio>

void init (int *L, int *R, int N, bool *occupied) {
    for(int i = 0; i < N; i++) {
        L[i] = i;
        R[i] = N - i - 1;
        occupied[i] = false;
    }
}

int choose(int *L, int *R, int N, bool *occupied) {
    int maxMinLR = -1;
    int maxLR = -1;
    int ch = -1;
    for(int i = 0; i < N; i++) {
        if(occupied[i]) continue;
        int minLR = L[i] < R[i] ? L[i] : R[i];
        if(minLR > maxMinLR) {
            maxMinLR = minLR;
            ch = i;
            maxLR = L[i] < R[i] ? R[i] : L[i];
        }
        else if(minLR == maxMinLR) {
            int currMaxLR = L[i] < R[i] ? R[i] : L[i];
            if(maxLR < currMaxLR) {
                maxLR = currMaxLR;
                ch = i;
            }
        }
    }
    if(ch == -1) while(1);
    occupied[ch] = true;
    return ch;
}

void relax(int *L, int *R, int N, int s, bool *occupied) {
    for(int i = 0; i < s; i++) {
        if(occupied[i]) continue;
        int newDisR = s - i - 1;
        if(R[i] > newDisR)
            R[i] = newDisR;
    }
    for(int i = s+1; i < N; i++) {
        if(occupied[i]) continue;
        int newDisL = i - s - 1;
        if(L[i] > newDisL)
            L[i] = newDisL;
    }
}

int main() {
    int T, t = 0, N, K;
    int L[1010], R[1010];
    bool occupied[1010];
    scanf("%d", &T);
    while(T--) {
        scanf("%d%d", &N, &K);
        init(L, R, N, occupied);
        int s;
        for(int i = 0; i < K; i++) {
            s = choose(L, R, N, occupied);
            relax(L, R, N, s, occupied);
        }
        int y = L[s] < R[s] ? R[s] : L[s];
        int z = L[s] < R[s] ? L[s] : R[s];
        printf("Case #%d: %d %d\n", ++t, y, z);
    }
    return 0;
}

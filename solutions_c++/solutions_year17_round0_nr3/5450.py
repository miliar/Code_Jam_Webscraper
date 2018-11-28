#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>


using namespace std;

bool used[1001] = { false };

int L[1001];
int R[1001];

int minLR[1001];
int maxLR[1001];


int select_stall(int n) {
    int min_lr = 0, max_lr = 0;
    int res = 0;

    int i = 0;
    while (used[i]) 
        ++i;
    
    res = i;
    min_lr = minLR[i];
    max_lr = maxLR[i];
    ++i;

    for (; i < n; ++i) {
        if (used[i])
            continue;
        if (min_lr < minLR[i]) {
            min_lr = minLR[i];
            max_lr = maxLR[i];
            res = i;
        } else if (min_lr == minLR[i]) {
            if (max_lr < maxLR[i]) {
                max_lr = maxLR[i];
                res = i;
            }
        }
    }

    return res;
}

void update(int i, int n) {
    used[i] = true;
    // update on the left
    int j = i - 1;
    for (; j >= 0 && !used[j]; --j) {
        R[j] = i - j - 1;
        minLR[j] = min(R[j], L[j]);
        maxLR[j] = max(R[j], L[j]);
    }
    minLR[i] = min(R[i], i - j - 1);
    maxLR[i] = max(R[i], i - j - 1);

    // update on the right
    j = i + 1;
    for (; j < n && !used[j]; ++j) {
        L[j] = j - i - 1;
        minLR[j] = min(R[j], L[j]);
        maxLR[j] = max(R[j], L[j]);
    }
    minLR[i] = min(L[i], j - i - 1);
    maxLR[i] = max(L[i], j - i - 1);
}   

int solve(int n, int k) {
    memset(used, 0, 1001 * sizeof(bool));
    memset(L, 0, 1001 * sizeof(int));
    memset(R, 0, 1001 * sizeof(int));
    memset(minLR, 0, 1001 * sizeof(int));
    memset(maxLR, 0, 1001 * sizeof(int));

    for (int i = 0; i < n; ++i) {
        L[i] = i;
        R[i] = n - 1 - i;
        minLR[i] = min(L[i], R[i]);
        maxLR[i] = max(L[i], R[i]);
    }

    int res = 0;

    for (int i = 0; i < k; ++i) {
        res = select_stall(n);
       // printf("%d\n", res);
        update(res, n);
    }

    return res;
}

int main(int argc, char const *argv[]) {
    FILE *fin = fopen("problemC.in", "r");
    FILE *fout = fopen("problemC.txt", "w");

    int t = 0, n = 0, k = 0;
    fscanf(fin, "%d", &t);

    for (int i = 0; i < t; ++i) {
        fscanf(fin, "%d %d", &n, &k);
        int idx = solve(n, k);
        fprintf(fout, "Case #%d: %d %d\n", i + 1, maxLR[idx], minLR[idx]);
    }

    return 0;
}
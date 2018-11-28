#include <iostream>
using namespace std;


int T;
int N, P;
int G[4];
int opt[1100000];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> T;
    for (int tid = 0; tid < T; ++tid) {
        cin >> N >> P;
        memset(G, 0, sizeof G);
        for (int i = 0; i < N; ++i) {
            int x;
            cin >> x;
            ++G[x % P];
        }

        memset(opt, 0, sizeof opt);
        for (int i = 0; i <= G[1]; ++i) {
            if (P == 2) {
                if (i > 0) {
                    if (((i - 1) * 1) % P == 0)
                        opt[i] = opt[i - 1] + 1;
                    else
                        opt[i] = opt[i - 1];
                }
            } else {
                for (int j = 0; j <= G[2]; ++j) {
                    if (P == 3) {
                        if (i > 0) {
                            if (((i - 1) * 1 + j * 2) % P == 0) {
                                opt[i * 101 + j] = max(opt[i * 101 + j], opt[(i - 1) * 101 + j] + 1);
                            } else {
                                opt[i * 101 + j] = max(opt[i * 101 + j], opt[(i - 1) * 101 + j]);
                            }
                        }
                        if (j > 0) {
                            if ((i * 1 + (j - 1) * 2) % P == 0) {
                                opt[i * 101 + j] = max(opt[i * 101 + j], opt[i * 101 + j - 1] + 1);
                            } else {
                                opt[i * 101 + j] = max(opt[i * 101 + j], opt[i * 101 + j - 1]);
                            }
                        }
                    } else {
                        for (int k = 0; k <= G[3]; ++k) {
                            if (i > 0) {
                                if (((i - 1) * 1 + j * 2 + k * 3) % P == 0) {
                                    opt[i * 101 * 101 + j * 101 + k] = max(opt[i * 101 * 101 + j * 101 + k], opt[(i - 1) * 101 * 101 + j * 101 + k] + 1);
                                } else {
                                    opt[i * 101 * 101 + j * 101 + k] = max(opt[i * 101 * 101 + j * 101 + k], opt[(i - 1) * 101 * 101 + j * 101 + k]);
                                }
                            }
                            if (j > 0) {
                                if ((i * 1 + (j - 1) * 2 + k * 3) % P == 0) {
                                    opt[i * 101 * 101 + j * 101 + k] = max(opt[i * 101 * 101 + j * 101 + k], opt[i * 101 * 101 + (j - 1) * 101 + k] + 1);
                                } else {
                                    opt[i * 101 * 101 + j * 101 + k] = max(opt[i * 101 * 101 + j * 101 + k], opt[i * 101 * 101 + (j - 1) * 101 + k]);
                                }
                            }
                            if (k > 0) {
                                if ((i * 1 + j * 2 + (k - 1) * 3) % P == 0) {
                                    opt[i * 101 * 101 + j * 101 + k] = max(opt[i * 101 * 101 + j * 101 + k], opt[i * 101 * 101 + j * 101 + k - 1] + 1);
                                } else {
                                    opt[i * 101 * 101 + j * 101 + k] = max(opt[i * 101 * 101 + j * 101 + k], opt[i * 101 * 101 + j * 101 + k - 1]);
                                }
                            }
                        }
                    }
                }
            }
        }

        // cout << G[0] << " " << G[1] << " " << G[2] << " " << G[3] << endl;

        int result = G[0];
        if (P == 2) {
            result += opt[G[1]];
        } else if (P == 3) {
            result += opt[G[1] * 101 + G[2]];
        } else {
            result += opt[G[1] * 101 * 101 + G[2] * 101 + G[3]];
        }

        cout << "Case #" << tid + 1 << ": " << result << endl;
    }

    return 0;
}
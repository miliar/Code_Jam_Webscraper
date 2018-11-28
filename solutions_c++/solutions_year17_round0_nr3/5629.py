#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int mmin(const int &a, const int &b) {
    return (a<b)?a:b;
}
int mmax(const int &a, const int &b) {
    return (a>b)?a:b;
}

int main(int argc, char* argv[])
{
    int T; cin >> T;
    for (int t = 0; t < T; t++) {
        int N, K; cin >> N >> K;
        int s[1003]; s[0] = 1; s[N+1] = 1;
        for (int i = 1; i <= N; ++i) s[i] = 0;
        for (int k = 0; k < K; ++k) {
            int l[1003], r[1003], mi[1003], ma[1003];
            for (int i = 0; i < 1003; ++i) {
                l[i] = 0; r[i] = 0; mi[i] = 0; ma[i] = 0;
            }
            int lastLeft = 0;
            for (int i = 0; i <= N+1; i++) {
                if (s[i] == 1) {
                    lastLeft = i;
                    continue;
                }
                l[i] = i-lastLeft;
                int right = i+1;
                while (s[right] == 0) right++;
                r[i] = right-i;
                mi[i] = mmin(l[i], r[i]);
                ma[i] = mmax(l[i], r[i]);
                //printf("%d: %d %d %d", k, i, mi[i], ma[i]);
            }
            for (int i = 0; i < 1003; ++i) l[i] = 0, r[i] = 0;
            int maximalM = 0;
            for (int i = 0; i < 1003; ++i) if (mi[i] > maximalM) maximalM = mi[i];
            vector<int> possibles;
            for (int i = 0; i < 1003; ++i) if (mi[i] == maximalM) possibles.push_back(i);
            maximalM = 0;
            int chosen = possibles.back();
            for (vector<int>::reverse_iterator r = possibles.rbegin(); r != possibles.rend(); ++r) {
                int index = *r;
                if (ma[index] >= maximalM) {
                    maximalM = ma[index];
                    chosen = index;
                }
            }
            s[chosen] = 1;
            if (k == K-1) cout << "Case #" << (t+1) << ": " << (maximalM-1) << " " 
                               << (mi[possibles.front()]-1) << endl;
        }
    }
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

ifstream fin("test.in");
ofstream fout("test.out");

inline void Solve(int A[]) {
    for(int i = A[0] - 1; i > 0; i--) {
        if(A[i] < A[i + 1]) {
            A[i + 1]--;

            for(int j = 1; j <= i; j++) {
                A[j] = 9;
            }

            return;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);

    int t;
    fin >> t;

    int level = 0;
    while(t--) {
        level++;

        long long int x;
        fin >> x;

        int A[30];
        memset(A, 0, sizeof(A));

        long long int c = x;
        while(c) {
            A[++A[0]] = c % 10;
            c /= 10;
        }

        for(int i = A[0] - 1; i > 0; i--) {
            if(A[i] < A[i + 1]) {
                Solve(A);
                i = A[0];
            }
        }

        if(A[A[0]] == 0) A[0]--;
        fout << "Case #" << level << ": ";
        for(int i = A[0]; i > 0; i--) fout << A[i];
        fout << "\n";
    }
    return 0;
}

#include <bits/stdc++.h>

#define cin fin
#define cout fout
#define MAXN 52

using namespace std;

typedef long long ll;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

int T;
int N, P;
ll R[MAXN];
ll Q[MAXN][MAXN];
int idx[MAXN];
int answer;

int main()
{
    cin >> T;

    for (int caseno=1; caseno<=T; caseno++) {
        cin >> N >> P;
        answer = 0;
        for (int i=0; i<N; i++)
            cin >> R[i];

        for (int i=0; i<N; i++) {
            for (int j=0; j<P; j++)
                cin >> Q[i][j];
            sort(Q[i], Q[i]+P);
            idx[i] = 0;
        }

        for (ll serv=1LL; serv<1000010LL; serv++) {
            while (true) {
                for (int i=0; i<N; i++) {
                    while ((idx[i] < P) && (9LL*R[i]*serv > 10LL*Q[i][idx[i]]))
                        idx[i] ++;
                    if (idx[i] == P) goto finish;
                    if ((10LL*Q[i][idx[i]] > 11LL*R[i]*serv)) goto tempfinish;
                }
                answer ++;
                for (int i=0; i<N; i++)
                    idx[i] ++;
            }
            tempfinish:;
        }
        finish:;
        cout << "Case #" << caseno << ": " << answer << endl;
    }


    return 0;
}

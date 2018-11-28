#include <iostream>
#include <string>
#include <map>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

vector<unsigned long long> R;
int N, P;
int max2(int a, int b) {
    return (a<b)?b:a;
}
int solve(vector<vector<unsigned long long> > &Q) {
    int ans = 0;
    int curr = 1;
    vector<int> k(N,0);
    while (true) {
        for (int i = 0; i < N; i++) {
            while (Q[i][k[i]]*10 < 9 * R[i]*curr) {
                k[i]++;
                if (k[i] == P) return ans;
            }
        }
        bool flag = true;
        int nxtcurr = curr+1;
        for (int i = 0 ; i < N; i++) {
            if (Q[i][k[i]]*10>11*R[i]*curr) {
                flag = false;
                nxtcurr = max2(nxtcurr,Q[i][k[i]]*10/(11*R[i]*curr));
            }
        }
        if (flag) {
            ans ++;
            for (int i = 0 ; i < N; i++) {
                k[i] ++;
                if (k[i] == P) return ans;
            }
        }
        else
            curr = nxtcurr;
    }
}
int main() {
    int nn;
    cin >> nn;
    for (int i = 1 ; i <= nn; i++) {
        printf("Case #%d: ",i);
        cin >> N >> P;
        R.resize(N);
        vector<vector<unsigned long long>> Q;
        for (int i = 0 ; i < N; i++)
            cin >> R[i];
        for (int i = 0 ; i < N; i++)  {
            vector<unsigned long long> qq;
            for (int j = 0 ; j < P; j++) {
                unsigned long long pkt;
                cin >> pkt;
                qq.push_back(pkt);
            }
            sort(qq.begin(),qq.end());
            Q.push_back(qq);
        }
        printf("%d\n", solve(Q));
    }
}

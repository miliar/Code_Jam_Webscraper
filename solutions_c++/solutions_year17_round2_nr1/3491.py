#include <bits/stdc++.h>
using namespace std;

double data[1001][1001];
double inputK[1001];
double inputS[1001];
double czas[1001][1001];

vector<pair<double, double> > kolizje;

void solution() {
    kolizje.clear();
    double D;
    int N;
    cin >> D >> N;
    for(int i = 1; i <= N; i++) {
        cin >> inputK[i] >> inputS[i];
        kolizje.push_back(make_pair(inputK[i], inputS[i]));
    }
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            if(i != j) {
                data[i][j] = (inputK[i] * inputS[j] - inputS[i] * inputK[j]) / (inputS[j] - inputS[i]);
                czas[i][j] = (data[i][j] - inputK[i]) / inputS[i];
                if(data[i][j] >= inputK[i] && data[i][j] >= inputK[j]) {
                    kolizje.push_back(make_pair(data[i][j], min(inputS[i], inputS[j])));
                }
            } else {
                data[i][j] = czas[i][j] = 0;
            }
        }
    }

    double result= 1e18;

    for(auto &a : kolizje) {
        if((D * a.second) / (D - a.first) > 0) {
            result =min(result,(D * a.second) / (D - a.first))
                    ;
        }
    }cout.precision(6);
    cout << fixed << result;
}

int main() {
    ios_base::sync_with_stdio(false);
    int z;
    cin >> z;

    for(int z1 = 1; z1 <= z; z1++)  {
        cout << "Case #" << z1 << ": ";
        solution();
        cout << endl;
    }
    return 0;
}
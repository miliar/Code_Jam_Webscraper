#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

vector<pair<int, double> > horses;

bool comp(pair<int, double> a, pair<int, double> b){
    if(a.second == b.second){
        return a.first > b.first;
    }else{
        return a.second > b.second;
    }
}

int main(void){
    int T, D, N, s, v;
    double t;

    cin >> T;

    for(int i = 0; i < T; ++i){
        horses.clear();

        cin >> D >> N;

        for(int j = 0; j < N; ++j){
            cin >> s >> v;
            t = (double) ((D - s) / (double) v);
            horses.push_back(make_pair(s, t));
        }

        sort(horses.begin(), horses.end(), comp);

        cout << "Case #" << i + 1 << ": " << setprecision(6) << fixed << double (D / horses[0].second) << endl;
    }

    return 0;
}

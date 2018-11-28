#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>

using namespace std;

int Serve(int N, int P, int base[], int data[100][100]){
    int intervals[100][100][2];

    for (int i = 0; i < N; ++i){
        for (int j = 0; j < P; ++j){
            float center = float(data[i][j]) / float(base[i]);
            intervals[i][j][1] = (int)(center / float(0.9));
            intervals[i][j][0] = (int)(ceil(center / float(1.1)));
        }
    }

    int count = N * P;
    int index[100];
    for (int i = 0; i < N; ++i){
        index[i] = P - 1;
    }

    int ret = 0;
    while (count > 0){
        // find max l
        int maxl = 0;
        int maxlInd = -1;
        for (int i = 0; i < N; ++i){
            int l = intervals[i][index[i]][0];
            if (l > maxl){
                maxl = l;
                maxlInd = i;
            }
        }

        //try this
        bool fit = true;
        for (int i = 0; i < N; ++i){
            if (index[i] < 0 || intervals[i][index[i]][1] < maxl){
                fit = false;
                break;
            }
        }

        if (fit){
            ++ret;
            for (int i = 0; i < N; ++i){
                index[i]--;
            }
            count -= N;
        }else{
            index[maxlInd]--;
            count -= 1;
        }
    }
    return ret;
}

int main() {

    ifstream in_file("data/serving_large.in");
    ofstream out_file("data/serving.out");
    int T = 0;
    in_file >> T;

    int data[100][100];
    int base[100];
    for (int t = 0; t < T; ++t){

        // read data
        int N, P;
        in_file >> N >> P;

        for (int n = 0; n < N; ++n){
            in_file>>base[n];
        }

        for (int i = 0; i < N; ++i){
            for (int j = 0; j < P; ++j){
                in_file >> data[i][j];
            }
            std::sort(data[i], data[i] + P);
        }

        // run
        int rst = Serve(N, P, base, data);

        out_file<<"Case #"<<t+1<<": "<<rst<<std::endl;
    }
    return 0;
}
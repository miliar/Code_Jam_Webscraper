//
// Created by huklee on 08/04/2017.
//
// google code jam 2017 QT C
//  : DP-similar approach O((logN)^2)

#define NOMINMAX
#include <map>
#include <queue>
#include <string>
#include <bitset>
#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

void split_seg(map<long long,long long> &mpi){
    map<long long, long long>_mpi;
    for (map<long long,long long>::iterator it = mpi.begin(); it != mpi.end(); it++){
        // in case of odd numbers
        long long new_key;
        if (it->first%2 == 1) {
            new_key = (it->first - 1)/2;
            if (_mpi.find(new_key) == _mpi.end())
                _mpi[new_key] = 0;
            _mpi[new_key] += it->second*2;
        }
        else{
            new_key = (it->first - 1)/2;
            if (_mpi.find(new_key) == _mpi.end())
                _mpi[new_key] = 0;
            _mpi[new_key] += it->second;

            new_key++;
            if (_mpi.find(new_key) == _mpi.end())
                _mpi[new_key] = 0;
            _mpi[new_key] += it->second;
        }
    }
    mpi = _mpi;     // copy
};

long long solve(long long N, long long K){
    int level = 0;
    long long index = 0;

    // 01. find the right level & index
    long long low = 1, high = 2;
    while (true){
        if (low <= K && K < high){
            index = K - low;
            break;
        }
        level++;
        low *= 2;
        high *= 2;
    }

    // 02. generate segmentations
    map<long long,long long> mpi;
    mpi[N] = 1;
    for (int i=0; i < level; i++)
        split_seg(mpi);
    // 03. get the result
    long long min_val, max_val;
    for (map<long long,long long>::reverse_iterator it = mpi.rbegin(); it != mpi.rend(); it++){
        // set the values
        if (index < it->second){
            min_val = (it->first - 1)/2;
            max_val = (it->first%2 == 0) ? min_val + 1 : min_val;
            break;
        }

        index = max((long long)0, index - it->second);
    }
    cout << max_val << " " << min_val << endl;
}

int main() {
//    freopen("/Users/huklee/ClionProjects/Algorithm_Study/input.txt", "r", stdin);
    long long T, N, K;
    cin >> T;
    for (int tc=1; tc <= T; tc++){
        cin >> N >> K;
        cout << "Case #" << tc << ": ";
        solve(N, K);
    }
}

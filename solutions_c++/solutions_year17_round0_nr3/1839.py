/*
ID: bob.bra1
PROG:
LANG: C++11
*/

#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <sstream>
#include <deque>

using namespace std;
long long gap_sizes[100000];
long long gap_counts[100000];

int get_index(long long s){
    long long i;
    while(gap_sizes[i] > s) i++;
    gap_sizes[i] = s;
    return i;
}

int main()
{
    int T;
    cin >> T;
    //T=1;
    long long N, K;

    int gap_index;
    int gap_read_index;
    long long new_gap;

    for (int tc=1; tc<=T; tc++){
        cin >> N>> K;
        //N=10000;
        //K = 200;
        for (int i=0; i<100000; i++){
            gap_counts[i] = 0;
            gap_sizes[i] = 0;
        }

        gap_index =0;
        gap_sizes[gap_index] = N;
        gap_counts[gap_index] = 1;
        gap_read_index = 0;

        while (gap_sizes[gap_read_index]){
            new_gap = gap_sizes[gap_read_index]/ 2;
            gap_index = get_index(new_gap);
            gap_counts[gap_index] += gap_counts[gap_read_index];
            new_gap = (gap_sizes[gap_read_index]-1)/2;
            gap_index = get_index(new_gap);
            gap_counts[gap_index] += gap_counts[gap_read_index];
            gap_read_index++;
        }
        gap_index = -1;
        while (K > 0){

            gap_index++;
            K -= gap_counts[gap_index];
        }

        cout << "Case #" << tc << ": " << gap_sizes[gap_index] /2 << " " << (gap_sizes[gap_index]-1) /2 << endl;

    }

    return 0;
}

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <cmath>
#include <queue>
#include <map>
#include <set>
#include <sstream>

#define FOR(i, a, b) for(int i = a; i < b; i++)
#define FORD(i, a, b) for(int i = a; i > b; i--)

using namespace std;

int T;
long long N, K;

int main()
{
    ifstream fin;
    fin.open("C-small-2-attempt0.in");
    ofstream fout;
    fout.open("output-small-2.txt");

    fin >> T;

    FOR (i, 0, T) {
        fin >> N >> K;

        int target_layer;
        int index_in_layer;
        long long power_2 = 1;
        FOR(j, 0, 63) {
            power_2 = power_2 * 2;
            if (power_2 - 1 >= K) {
                target_layer = j;
                index_in_layer = K - (power_2/2 - 1);
                break;
            }
        }

        int curr_layer = 0;
        long long layer_high = N;
        long long layer_low = N - 1;
        long long layer_high_freq = 1;
        long long layer_low_freq = 0;
        while (curr_layer < target_layer) {
            if (layer_high % 2) {
                layer_high_freq = layer_high_freq*2 + layer_low_freq;
                layer_low_freq = layer_low_freq;
            }
            else {
                layer_high_freq = layer_high_freq;
                layer_low_freq = layer_high_freq + layer_low_freq*2;
            }
            layer_high = layer_high/2;
            layer_low = layer_high - 1;

            curr_layer++;
        }

        int result;
        if (index_in_layer <= layer_high_freq) {
            result = layer_high;
        }
        else {
            result = layer_low;
        }

        int minimum, maximum;
        if (result % 2) {
            minimum = result/2;
            maximum = result/2;
        }
        else {
            minimum = result/2 - 1;
            maximum = result/2;
        }

        fout << "Case #" << i + 1 << ": " << maximum << " " << minimum << endl;
    }

    return 0;
}

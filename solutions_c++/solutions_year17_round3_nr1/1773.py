#define _USE_MATH_DEFINES

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
#include <iomanip>


#define FOR(i, a, b) for(int i = a; i < b; i++)
#define FORD(i, a, b) for(int i = a; i > b; i--)

using namespace std;

int T;
int N, K;
vector<pair<long long, long long>> pancakes;

bool pancake_sort (pair<long long, long long> p1, pair<long long, long long> p2) {
    return p1.first > p2.first;
}

bool height_sort (pair<long long, long long> p1, pair<long long, long long> p2) {
    return p1.first*p1.second > p2.first*p2.second;
}

int main()
{
    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("testout.txt");

    fin >> T;

    FOR (i, 0, T) {
        fin >> N >> K;
        pair<long long, long long> pancake;
        FOR(j, 0, N) {
            fin >> pancake.first >> pancake.second;
            pancakes.push_back(pancake);
        }
        sort(pancakes.begin(), pancakes.end(), pancake_sort);

        double maxsurface = 0;
        FOR(large, 0, N - K + 1) {
            double surface = 0;
            surface += pancakes[large].first*pancakes[large].first;
            surface += 2*(pancakes[large].first*pancakes[large].second);
            if (K > 1) {
                vector<pair<long long, long long>> newpancakes(pancakes.begin() + large + 1, pancakes.begin() + N);
                sort(newpancakes.begin(), newpancakes.end(), height_sort);
                FOR(j, 0, K - 1) {
                    surface += 2*newpancakes[j].first*newpancakes[j].second;
                }
            }
            if (surface > maxsurface) {
                maxsurface = surface;
            }
        }



        maxsurface = maxsurface*3.14159265358979323846;
        fout << "Case #" << i + 1 << ": " << setprecision(17) << maxsurface << endl;
        pancakes.clear();
    }

    return 0;
}

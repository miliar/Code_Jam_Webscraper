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

int T, N;
long long int D;
vector<pair<long long int, long long int>> horses;
string N_str;

bool horse_sort (pair<long long, long long> h1, pair<long long, long long> h2) {
    return h1.first < h2.first;
}

double compute_dist(int horse_no) {
    if (horse_no == N - 1) {
        return (D - horses[horse_no].first)/((double)horses[horse_no].second);
    }
    else {
        double uncapped_time = (D - horses[horse_no].first)/((double)horses[horse_no].second);
        //double time_to_reach_next_start = (horses[horse_no + 1].first - horses[horse_no].first)/((double)horses[horse_no].second);
        double real_time = max(uncapped_time, compute_dist(horse_no + 1));
        return real_time;
    }
}

int main()
{
    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("A-large-res.txt");

    fin >> T;

    FOR (i, 0, T) {
        fin >> D >> N;
        pair<long long, long long> horse;
        FOR(j, 0, N) {
            fin >> horse.first >> horse.second;
            horses.push_back(horse);
        }

        sort(horses.begin(), horses.end(), horse_sort);

        double time_required = compute_dist(0);
        double speed_required = D/time_required;

        fout << "Case #" << i + 1 << ": " << setprecision(17) << speed_required << endl;
        horses.clear();
    }

    return 0;
}

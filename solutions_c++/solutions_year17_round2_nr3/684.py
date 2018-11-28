#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <unistd.h>
#include <unordered_set>
#include <sstream>
#include <set>
#include <map>

using namespace std;

string problem = "/Users/alanpierce/codejam17/Round1B/C-large";
FILE *infile;
FILE *outfile;

typedef long long lld;

lld next_lld() {
    lld result = 0;
    fscanf(infile, "%lld", &result);
    return result;
}

string next_string() {
    char result[100000];
    fscanf(infile, "%s", result);
    return string(result);
}

int next_int() {
    int result = 0;
    fscanf(infile, "%d", &result);
    return result;
}

vector<int> next_int_vector(int n) {
    vector<int> result(n, -1);
    for (int i = 0; i < n; i++) {
        result[i] = next_int();
    }
    return result;
}

string handle_case() {
    int numCities = next_int();
    int numPairsOfStops = next_int();

    vector<pair<lld, lld>> horses;
    for (int i = 0; i < numCities; i++) {
        horses.push_back(make_pair(next_lld(), next_lld()));
    }

    vector<vector<lld>> graph;
    for (int i = 0; i < numCities; i++) {
        vector<lld> v;
        for (int j = 0; j < numCities; j++) {
            v.push_back(next_lld());
        }
        graph.push_back(v);
    }

    vector<pair<int, int>> pairsOfStops;
    for (int i = 0; i < numPairsOfStops; i++) {
        pairsOfStops.push_back(make_pair(next_int(), next_int()));
    }

//    vector<double> minTimeByCity(numCities, -1.0);
//    minTimeByCity[numCities - 1] = 0.0;
//    for (int i = numCities - 2; i >= 0; i--) {
//        lld horseDistance = horses[i].first;
//        lld horseSpeed = horses[i].second;
//
//        double remainingDistance = double(horseDistance);
//        double minTime = -1.0;
//        for (int j = i + 1; j < numCities; j++) {
//            if (graph[j - 1][j] == -1) {
//                printf("Crap!\n");
//            }
//            remainingDistance -= graph[j - 1][j];
//            if (remainingDistance < -.0000000001) {
//                break;
//            }
//            double timeToCity = (horseDistance - remainingDistance) / double(horseSpeed);
//            if (minTimeByCity[j] == -1.0) {
//                continue;
//            }
//            double totalTime = timeToCity + minTimeByCity[j];
//            if (minTime == -1.0 || totalTime < minTime) {
//                minTime = totalTime;
//            }
//        }
//
//        minTimeByCity[i] = minTime;
//    }

    vector<vector<double>> distances(graph.size(), vector<double>(graph.size(), -1.0));
    for (int i = 0; i < graph.size(); i++) {
        for (int j = 0; j < graph.size(); j++) {
            distances[i][j] = graph[i][j];
        }
    }

    for (int k = 0; k < numCities; k++) {
        for (int i = 0; i < numCities; i++) {
            for (int j = 0; j < numCities; j++) {
                if (distances[i][k] == -1.0 || distances[k][j] == -1.0) {
                    continue;
                }
                double newDistance = distances[i][k] + distances[k][j];
                if (distances[i][j] == -1.0 || newDistance < distances[i][j]) {
                    distances[i][j] = newDistance;
                }
            }
        }
    }

    vector<vector<double>> minTimes(graph.size(), vector<double>(graph.size(), -1.0));

    for (int i = 0; i < graph.size(); i++) {
        for (int j = 0; j < graph.size(); j++) {
            if (distances[i][j] != -1 && distances[i][j] <= horses[i].first) {
                minTimes[i][j] = distances[i][j] / double(horses[i].second);
            }
        }
    }

    for (int k = 0; k < numCities; k++) {
        for (int i = 0; i < numCities; i++) {
            for (int j = 0; j < numCities; j++) {
                if (minTimes[i][k] == -1.0 || minTimes[k][j] == -1.0) {
                    continue;
                }
                double newTime = minTimes[i][k] + minTimes[k][j];
                if (minTimes[i][j] == -1.0 || newTime < minTimes[i][j]) {
                    minTimes[i][j] = newTime;
                }
            }
        }
    }

    stringstream ss;
    ss.precision(15);
    for (int i = 0; i < numPairsOfStops; i++) {
        ss << minTimes[pairsOfStops[i].first - 1][pairsOfStops[i].second - 1];
        if (i < numPairsOfStops - 1) {
            ss << " ";
        }
    }
    return ss.str();
}

int main() {
    string infilename = problem + ".in";
    string outfilename = problem + ".out";
    infile = fopen(infilename.c_str(), "r");
    if (infile == nullptr) {
        printf("File %s not found!", infilename.c_str());
        return 1;
    }
    outfile = fopen(outfilename.c_str(), "w");

    lld n_cases = next_lld();
    for (lld case_num = 1; case_num <= n_cases; ++case_num) {
        string result = handle_case();
        printf("Case #%lld: %s\n", case_num, result.c_str());
        fprintf(outfile, "Case #%lld: %s\n", case_num, result.c_str());
    }
    return 0;
}
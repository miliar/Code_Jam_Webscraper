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

string problem = "/Users/alan/codejam17/Round1A/A-large";
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
    vector<string> grid;
    int r = next_int();
    int c = next_int();
    for (int i = 0; i < r; i++) {
        grid.push_back(next_string());
    }

    vector<pair<int, int>> directions;
    directions.push_back(make_pair(0, 1));
    directions.push_back(make_pair(0, -1));
    directions.push_back(make_pair(1, 0));
    directions.push_back(make_pair(-1, 0));

    for (int i = 0; i < directions.size(); i++) {
        int dr = directions[i].first;
        int dc = directions[i].second;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == '?') {
                    int new_i = i;
                    int new_j = j;
                    while (new_i >= 0 && new_i < r && new_j >= 0 && new_j < c) {
                        if (grid[new_i][new_j] != '?') {
                            grid[i][j] = grid[new_i][new_j];
                            break;
                        }
                        new_i += dr;
                        new_j += dc;
                    }
                }
            }
        }
    }

    stringstream ss;
    for (int i = 0; i < r; i++) {
        ss << '\n' << grid[i];
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
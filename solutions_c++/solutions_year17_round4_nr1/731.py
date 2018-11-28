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

string problem = "/Users/alanpierce/codejam17/Round2/A-small-attempt0";
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
    int result = 0;
    int n = next_int();
    int p = next_int();
    map<int, int> counts;
    vector<int> values = next_int_vector(n);
    for (int i = 0; i < values.size(); i++) {
        counts[values[i] % p] += 1;
    }

    result += counts[0];
    counts[0] = 0;

    for (int i = 1; i < p; i++) {
        for (int j = 1; j < p; j++) {
            if ((i + j) % p != 0) {
                continue;
            }
            while (counts[i] > 0 && counts[j] > 0) {
                counts[i]--;
                counts[j]--;
                result++;
            }
        }
    }

    for (int i = 1; i < p; i++) {
        for (int j = 1; j < p; j++) {
            for (int k = 1; k < p; k++) {
                if ((i + j + k) % p != 0) {
                    continue;
                }
                while (counts[i] > 0 && counts[j] > 0 && counts[k] > 0) {
                    counts[i]--;
                    counts[j]--;
                    counts[k]--;
                    result++;
                }
            }
        }
    }

    for (int i = 1; i < p; i++) {
        for (int j = 1; j < p; j++) {
            for (int k = 1; k < p; k++) {
                for (int l = 0; l < p; l++) {
                    if ((i + j + k + l) % p != 0) {
                        continue;
                    }
                    while (counts[i] > 0 && counts[j] > 0 && counts[k] > 0 && counts[l] > 0) {
                        counts[i]--;
                        counts[j]--;
                        counts[k]--;
                        counts[l]--;
                        result++;
                    }
                }
            }
        }
    }

    if (counts[1] > 0 || counts[2] > 0 || counts[3] > 0) {
        result++;
    }

    stringstream ss;
    ss << result;
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
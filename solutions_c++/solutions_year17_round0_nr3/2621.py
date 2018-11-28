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

string problem = "/Users/alanpierce/codejam17/qual/C-large";
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
    lld num_stalls = next_lld();
    lld num_people = next_lld();

    map<lld, lld> gap_sizes;
    gap_sizes[num_stalls] = 1;

    while (true) {
        auto highest_element = *gap_sizes.rbegin();
        lld gap_size = highest_element.first;
        lld num_gaps = highest_element.second;

        if (num_people <= num_gaps) {
            lld min_spacing = (gap_size - 1) / 2;
            lld max_spacing = gap_size / 2;
            stringstream ss;
            ss << max_spacing << " " << min_spacing;
            return ss.str();
        }

        num_people -= num_gaps;

        gap_sizes[(gap_size - 1) / 2] += num_gaps;
        gap_sizes[gap_size / 2] += num_gaps;
        gap_sizes.erase(gap_size);
    }
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
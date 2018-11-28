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

string problem = "/Users/alanpierce/codejam17/Round1B/B-small-attempt0";
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
    int n = next_int();
    int r = next_int();
    int o = next_int();
    int y = next_int();
    int g = next_int();
    int b = next_int();
    int v = next_int();

    int numRs = r;
    int numYs = y;
    int numBs = b;

    int numOs = o;
    int numGs = g;
    int numVs = v;

    if (numOs == numBs && numRs + numYs + numGs + numVs == 0) {
        stringstream ss;
        for (int i = 0; i < numOs; i++) {
            ss << "BO";
        }
        return ss.str();
    }

    if (numGs == numRs && numYs + numBs + numOs + numVs == 0) {
        stringstream ss;
        for (int i = 0; i < numGs; i++) {
            ss << "RG";
        }
        return ss.str();
    }

    if (numVs == numYs && numRs + numBs + numOs + numGs == 0) {
        stringstream ss;
        for (int i = 0; i < numVs; i++) {
            ss << "YV";
        }
        return ss.str();
    }

    if (numOs > 0) {
        numBs -= numOs;
        if (numBs < 1) {
            return "IMPOSSIBLE";
        }
    }

    if (numGs > 0) {
        numRs -= numGs;
        if (numRs < 1) {
            return "IMPOSSIBLE";
        }
    }

    if (numVs > 0) {
        numYs -= numVs;
        if (numYs < 1) {
            return "IMPOSSIBLE";
        }
    }

    char firstChar = 0;
    char lastChar = 0;
    stringstream ss;
    map<char, int> nums;
    nums['B'] = numBs;
    nums['R'] = numRs;
    nums['Y'] = numYs;
    while (nums['B'] + nums['R'] + nums['Y'] > 0) {
        vector<char> chars;
        chars.push_back('B');
        chars.push_back('R');
        chars.push_back('Y');

        vector<char> eligibleChars;
        for (int i = 0; i < 3; i++) {
            if (chars[i] != lastChar && nums[chars[i]] > 0) {
                eligibleChars.push_back(chars[i]);
            }
        }

        if (eligibleChars.size() == 0) {
            return "IMPOSSIBLE";
        }

        int maxNum = 0;
        for (int i = 0; i < eligibleChars.size(); i++) {
            maxNum = max(maxNum, nums[eligibleChars[i]]);
        }

        vector<char> eligibleWithMaxChars;
        for (int i = 0; i < eligibleChars.size(); i++) {
            if (nums[eligibleChars[i]] == maxNum) {
                eligibleWithMaxChars.push_back(eligibleChars[i]);
            }
        }

        char charToUse = 0;
        for (int i = 0; i < eligibleWithMaxChars.size(); i++) {
            if (eligibleWithMaxChars[i] == firstChar) {
                charToUse = eligibleWithMaxChars[i];
                break;
            }
        }
        if (charToUse == 0) {
            charToUse = eligibleWithMaxChars[0];
        }

        nums[charToUse]--;
        if (nums['B'] + nums['R'] + nums['Y'] == 0 && charToUse == firstChar) {
            return "IMPOSSIBLE";
        }
        if (firstChar == 0) {
            firstChar = charToUse;
        }
        lastChar = charToUse;
        if (nums[charToUse] == 0) {
            if (charToUse == 'B') {
                for (int i = 0; i < numOs; i++) {
                    ss << "BO";
                }
                ss << "B";
            } else if (charToUse == 'R') {
                for (int i = 0; i < numGs; i++) {
                    ss << "RG";
                }
                ss << "R";
            } else if (charToUse == 'Y') {
                for (int i = 0; i < numVs; i++) {
                    ss << "YV";
                }
                ss << "Y";
            }
        } else {
            ss << charToUse;
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
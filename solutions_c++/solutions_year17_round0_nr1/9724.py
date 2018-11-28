#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<queue>
#include<string>

using namespace std;

int getMinSteps(string &str, int fsize) {
    int numSteps = 0, i = 0;
   // cout << str << " , " << fsize << endl;
    for(i=0; i <= str.size() - fsize; ++i) {
        if (str[i] == '-') {
            // try to flip fsize bytes starting from i
            for(int j = i; j < i + fsize; ++j) {
                str[j] = (str[j] == '-') ? '+' : '-';
            }
            ++numSteps;
        }
    }

    // check the rest of the string starting from where i left off
    for(int j = i; j < str.size(); ++j) {
        if (str[j] == '-')
            return -1;
    }
    return numSteps;
}

int main(int argc, char **argv) {

    int t, k;
    freopen("ip.txt", "r", stdin);
    cin >> t;
    string s;
    vector<string> strs;
    vector<int> fsizes;
    while(t-- ){
        s = "";
        cin >> s >> k;
        strs.push_back(s);
        fsizes.push_back(k);
    }

    for(int i=0; i<strs.size(); ++i ){
        int minSteps = getMinSteps(strs[i], fsizes[i]);
        if (minSteps == -1)
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl; 
        else
            cout << "Case #" << i+1 << ": " << minSteps << endl;
    }

    return 0;
}
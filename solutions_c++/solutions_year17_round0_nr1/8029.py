#include <iostream>
#include <fstream>
using namespace std;

void flip(char *buf, int K, int index) {
    int len = strlen(buf);
    int limit = index + K;
    while(index < limit && index < len) {
        buf[index] = buf[index] == '-' ? '+' : '-';
        index++;
    }
}

bool all_good(char *buf, int len) {
    for(auto i = 0 ; i < len; i++)
        if(buf[i]=='-') return false;
    return true;
}

string solve(char* buf, int K) {
    int len = strlen(buf);
    int cnt = 0;
    
    for(auto i = 0; i < len; i++){
        if(buf[i] == '-') {
            if (i + K > len) return "IMPOSSIBLE";
            flip(buf, K, i); 
            cnt++;
        }
    }
    if (!all_good(buf, len)) return "IMPOSSIBLE";
    return to_string(cnt);
}

int main () {
    int T;
    int testcase = 1;

    ifstream input;
    input.open("input.txt");
    std::ofstream outfile;
    outfile.open("out.txt", std::ios_base::app); 


    input >> T;
    while(testcase <= T) {
        char buf[1111] = {0,} ;
        int K;
        input >> buf >> K;
        string result = solve(buf, K);
        outfile << "Case #" << testcase << ": " << result << endl;
        cout << "Case #" << testcase << ": " << result << endl;
        testcase++;
    }
}

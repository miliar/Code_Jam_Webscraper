
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <sstream>
#include <random>
#include <unordered_map>
#include <algorithm> // for sort()
using namespace std;

bool isAcs(long long int n){
    int x = 9;
    while (n >= 1) {
        if(x < n%10) return false;
        x = n%10;
        n/=10;
    }
    return true;
}
long long int findNum(long long int n){
    //long long int ans = 0;
    
    
    while (!isAcs(n)) {
        string s = to_string(n);
        int x = s[0] - '0';
        for(long long int j = 0; j < s.size(); ++j){
            if (s[j]-'0' < x) {
                s[j-1] -= 1;
                for(long long int k = j; k < s.size(); ++k){
                    s[k] = '9';
                }
                //cout << "test" << s << endl;
                break;
            }
            x = s[j]-'0';
        }
        n = stoll(s);
        //cout << n << endl;
    }
    return n;
}

int main(int argc, const char * argv[]) {
    /*Input */
    
    //cout << findNum(111111111111111110);
    
    string filename = "/Users/xinpeilin/Desktop/Google_Code/B-large.in";
    ifstream fin;
    fin.open(filename);
    if (fin.fail()) {
        cout << "Failed to open input file\n";
        exit(1);
    }
    long long int num = 0;
    vector<long long int> ans;
    fin >> num;
    for (long long int i = 0; i < num; ++i) {
        long long int n = 0;
        fin >> n;
        n = findNum(n);
        ans.push_back(n);
    }
    
    
    fin.close();
    ofstream fout;
    fout.open("/Users/xinpeilin/Desktop/Google_Code/output_B-2.txt");
    for (long long int i = 0; i < ans.size(); ++i) {
        fout << "Case #" << i+1 << ": " << ans[i] << endl;
    }
    fout.close();
    return 0;
}





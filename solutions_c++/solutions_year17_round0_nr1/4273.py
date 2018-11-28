#include <string>
#include <fstream>
#include <vector>
#include <iostream>
#include <sstream>
#include <unordered_set>
#include <queue>
using namespace std;

string process(int flip, string panc){
    int len = panc.length();
    int count = 0;
    string target(len, '+');
    for(int i = 0; i <= len-flip; i++){
        if(panc[i] == '-'){
            count++;
            for(int j = 0; j < flip; j++){
                panc[i+j] = (panc[i+j]=='+'?'-':'+');
            }
        }
    }
    if(panc == target) return to_string(count); 
    return "IMPOSSIBLE";
}

int main(){
    ifstream fread("input.in");
    ofstream fwrite("output.out");
    string raw_data;
    getline(fread, raw_data);
    stringstream ss(raw_data);
    int testcase;
    ss >> testcase;
    int count = 1;
    while(testcase){
        getline(fread, raw_data);
        int flip;
        string panc;
        ss = stringstream(raw_data);
        ss >> panc;
        ss >> flip;
        fwrite << "Case #" << count << ": " << process(flip, panc) << endl;
        testcase--;
        count++;
    }
    return 0;
}

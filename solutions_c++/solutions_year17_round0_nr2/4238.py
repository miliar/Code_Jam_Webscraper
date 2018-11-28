#include <string>
#include <fstream>
#include <vector>
#include <iostream>
#include <sstream>
#include <unordered_set>
#include <queue>
using namespace std;

string process(string data){
    int len = data.length();
    int start = 0;
    int i;
    if(data.size()==1) return data;
    for(i = 1; i < len; i++){
        if(data[start] < data[i]){
            start = i;
        }
        else if(data[start] == data[i]){
            continue;
        }
        else if(data[start] > data[i]) break;
    }
    if(i == len) return data;
    else{
        data[start]--;
        for(int i = start+1; i < len; i++){
            data[i] = '9';
        }
        if(start == 0&&data[start] == '0') data.erase(data.begin());
    }
    return data;
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
        string data;
        getline(fread, data);
        fwrite << "Case #" << count << ": " << process(data) << endl;
        testcase--;
        count++;
    }
    return 0;
}

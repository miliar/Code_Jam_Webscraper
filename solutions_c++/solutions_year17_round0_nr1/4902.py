//
// Created by brian on 4/7/2017.
//
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main() {
    int K, T, firstminus, lastminus, count;
    string pancakes = "";
    ifstream fin ("A-large.in");
    ofstream fout ("outputA.txt");
    fin >> T;
    for(int i = 0; i < T; i++){
        count = 0;
        fin >> pancakes >> K;
        //count + until first -
        firstminus = pancakes.find("-");
        if(firstminus != string::npos)
        pancakes = pancakes.substr(firstminus);
        else pancakes = "";
        lastminus = pancakes.rfind("-");
        if(lastminus != string::npos)
        pancakes = pancakes.substr(0, lastminus+1);
        while(pancakes.size() >= K){
            for(int j = 0; j < K; j++){
                pancakes[j] = (pancakes[j] == '+') ? '-' : '+';
            }
            count++;
            firstminus = pancakes.find("-");
            if(firstminus == string::npos){
                pancakes = "";
                break;
            }
            pancakes = pancakes.substr(firstminus);
        }
        if(pancakes.size() != 0) fout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
        else fout << "Case #" << i+1 << ": " << count << endl;
    }
}

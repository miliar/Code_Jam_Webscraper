#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
ifstream fin ("A-large.in");
ofstream fout ("submission.txt");
long long n,size,queries;
vector<bool> pancakes;

int main() {
    fin >> queries;
    for(long long j = 1; j <= queries; j++){
        string input;
        fin >> input;
        for (long long i = 0; i < input.length(); i++) {
            char bit=input[i];
            if(bit=='-')pancakes.push_back(1);
            else pancakes.push_back(0);
        }
        n = pancakes.size();
        fin >> size;
        long long moves;
        for(long long x = 0; x <= n-size; x++){
            if(pancakes[x]==1){
                for(long long k = x; k< x+size; k++){
                    pancakes[k]=(pancakes[k]+1)%2;
                }
                moves++;
            }
        }
        bool tmp = false;
        for(long long x = n-1; x >=n-size; x--){
            if(pancakes[x]==1){
                tmp = true;
                
            }
        }
        if(tmp == true){
            fout <<"Case #"<<j << ": " << "IMPOSSIBLE" << endl;
        }
        else fout << "Case #"<<j << ": "  << moves << endl;
        pancakes.clear();
        moves = 0;
    }
}
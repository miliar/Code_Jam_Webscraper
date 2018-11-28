

#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
ifstream fin ("A-Large-1.in");
ofstream fout ("output.txt");
string input;
long long n,size,T;
vector<bool> arr;

void flip(long long a, long long b){
    for(long long x = a; x<=b; x++){
        arr[x] = !arr[x];
    }
}

int main() {
    fin >> T;
    
    for(int j = 1; j <= T; j++){
        arr.clear();
        fin >> input;
        for (int i = 0; i < input.length(); i++) {
            if(input[i]=='-'){
                arr.push_back(true);
            }
            else{
                arr.push_back(false);
            }
        }
        n = arr.size();
        fin >> size;
        long long moves;
        for(long long x = 0; x <= n-size; x++){
            if(arr[x]==1){
                flip(x, x+size-1);
                moves++;
            }
        }
        bool tmp = false;
        for(long long x = n-1; x >=n-size; x--){
            if(arr[x]==1){
                tmp = true;
                
            }
        }
        if(tmp == true){
            fout <<"Case #"<<j << ": " << "IMPOSSIBLE" << endl;
        }
        else{
            fout << "Case #"<<j << ": "  << moves << endl;
        }
        moves = 0;
    }
}
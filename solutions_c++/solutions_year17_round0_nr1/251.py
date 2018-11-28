#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(){
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T; fin >> T;
    for(int t = 1; t <= T; t++){
        fout << "Case #" << t << ": ";
        string line; fin >> line;
        int width; fin >> width;
        int state[line.length()];
        for(int i = 0; i < line.length(); i++){
            state[i] = line[i] == '+' ? 0 : 1;
        }
        int ans = 0;
        for(int i = 0; i < line.length()-width+1; i++){
            if(state[i] == 1){
                ans += 1;
                for(int j = i; j < i+width; j++){
                    state[j] = 1-state[j];
                }
            }
        }
        bool correct = true;
        for(int i = line.length()-width+1; i < line.length(); i++){
            if(state[i] == 1){
                correct = false;
                break;
            }
        }
        if(correct){
            fout << ans << "\n";
        }else{
            fout << "IMPOSSIBLE\n";
        }
    }
    return 0;
}


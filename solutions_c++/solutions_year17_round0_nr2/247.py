#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main(){
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int T; fin >> T;
    for(int t = 1; t <= T; t++){
        fout << "Case #" << t << ": ";
        string line; fin >> line;
        vector<int> num;
        for(int i = 0; i < line.length(); i++){
            num.push_back((int)line[i] - 48);
        }
        int index = 1;
        while(index < num.size()){
            if(num[index] < num[index-1]){
                num[index-1]--;
                for(int i = index; i < num.size(); i++){
                    num[i] = 9;
                }
                break;
            }
            index += 1;
        }

        for(int i = num.size()-1; i > 0; i--){
            if(num[i] < num[i-1]){
                num[i] = 9;
                num[i-1]--;
            }
        }

        for(int i = 0; i < num.size(); i++){
            if(i == 0 && num[i] != 0 || i != 0){
                fout << num[i];
            }
        }
        fout << "\n";
    }
    return 0;
}

#include<iostream>
#include<vector>
#include<map>
#include<string>

using namespace std;

int solve(string & pcks, int k, int pos = 0){

    if(pos + k == pcks.size()){
        auto first = pcks[pos];
        for(int a = 0; a < k ; a++){
            if(pcks[pos + a] != first){
                return -1;
            }
        }
        if(first == '+'){
            return 0;
        }
        if(first == '-'){
            return 1;
        } 
    }

    auto first = pcks[pos];
    if(first == '-'){
        for(int i = 0; i < k; i++){
            pcks[pos + i] = pcks[pos + i] == '+' ? '-' : '+';
        }
        int res = solve(pcks, k, pos + 1);
        if(res >= 0){
            return 1 + res;
        }
        return - 1;
    }
    else {
        int res = solve(pcks, k, pos + 1);
        if(res >= 0){
            return res;
        }
        return - 1;
    }
}

int main(){

    int ncases;

    cin >> ncases;


    for(int i = 0; i < ncases;i++){
        int k;
        string pancakes;
        cin >> pancakes;
        cin >> k;
        
        int res = solve(pancakes, k);
        if(res >= 0)
            cout << "Case #" << i + 1 << ": " << res;
        else
            cout << "Case #" << i + 1 << ": IMPOSSIBLE";
        cout << endl;
    }
}

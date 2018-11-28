
// Kasimir Tanner 2017
#include <iostream>
#include <vector>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;

char change(char c){
    if(c == '+')return '-';
    return '+';
}

int main(){
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);

    ullint T;
    cin >> T;

    for(ullint t = 0;t < T;t++){
        char c;
        cin >> noskipws >> c;

        vector<char> in;

        

        while(c != ' '){
            in.push_back(c);
            cin >> noskipws >> c;
        }

        ullint K;
        cin >> K;

        bool possible = true;
        ullint count = 0;

        for(ullint i = 0;i < in.size();i++){
            if(in[i] == '-'){
                count++;
                if(i+K-1 < in.size()){
                    for(ullint j = i;j<i+K;j++){
                        in[j] = change(in[j]);
                    }
                }else{
                    possible = false;
                }
                /*for(ullint j = 0;j<in.size();j++){
                    cout << in[j] << " ";
                }
                cout << "\n";*/
            }
        }

        cout << "Case #" << t+1 << ": ";

        if(possible){
            cout << count <<"\n";
        }else{
            cout << "IMPOSSIBLE\n";
        }


    }
    
    return 0;
}
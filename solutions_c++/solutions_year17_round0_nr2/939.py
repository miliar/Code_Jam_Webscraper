#include <algorithm>
#include <string>
#include <iostream>
#include <cassert>
#include <time.h>
#include <vector>

using namespace std;


bool untidy(string s){
    for(int i = 0 ; i < s.size() -1 ; i++){
        if((s[i] - '0') > (s[i + 1] - '0')){
            return true;
        }

    }
    return false;

}


void doWork(string& s){
    for(int i = 0 ; i  < s.size() - 1 ; i++){
        if((s[i] - '0') > (s[i + 1] - '0')){
            s[i]--;
            s[i + 1] = '9';
            for(int j = i + 1 ; j < s.size() ; j++){
                s[j] = '9';
            }
            return;
        }
    }
}

string trimZero(string s){
    int i = 0;
    while(s[i] == '0'){
        i++;
    }
    return s.substr(i);
}

int main(){
    string in;
    getline(cin, in);

    int testCases = stoi(in);

    

    for(int i = 0 ; i < testCases ; i++){
        getline(cin, in);

        while(untidy(in)){
            doWork(in);
        }

        cout << "Case #" << (i + 1) << ": " << trimZero(in) << endl;

    }


}

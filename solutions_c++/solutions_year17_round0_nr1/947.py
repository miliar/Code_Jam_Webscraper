#include <algorithm>
#include <string>
#include <iostream>
#include <cassert>
#include <time.h>
#include <vector>

using namespace std;

string getCase(string s){
    int count = 0;
    for(int i = 0 ; i < s.size() ; i++){
        if(s[i] != ' '){
            count++;
        }else{
            break;
        }
    }
    return s.substr(0, count);
}

int getSize(string s){
    int i;
    for(i = 0 ; i < s.size() ; i++){
        if(s[i] == ' '){
            i++;
            break;
        }
    }
    return stoi(s.substr(i));
}

bool notSolved(string s){
    for(int i = 0 ; i < s.size() ; i++){
        if(s[i] == '-'){
            return true;

        }

    }
    return false;

}

char flip(char c){
    if(c == '+'){
        return '-';
    }else{
        return '+';
    }
}


//return true if reached end, false otherwise
bool doWork(string& s, int k){
    for(int i = 0 ; i <= s.size() - k ; i++){
        if(s[i] == '+'){
            continue;
        }

        for(int x = 0 ; x < k ; x++){
            s[i + x] = flip(s[i + x]);
        }

        return i == (s.size() - k);

    }
    return true;
}



int main(){
    string header;
    getline(cin, header);
    int testCases = stoi(header);

    for(int i = 0 ; i < testCases ; i++){
        string line;
        getline(cin, line);

        string s = getCase(line);
        int size = getSize(line);
        int count = 0;
        bool reachedEnd = false;
        bool impossible = false;
        while(notSolved(s) && !reachedEnd){
            reachedEnd = doWork(s, size);
            count++;
        }

        if(notSolved(s)){
            impossible = true;
        }


        cout << "Case #" << (i + 1) << ": ";
        if(impossible){
            cout << "IMPOSSIBLE" << endl;
        }else{
            cout << count << endl;
        }
    }

}


/*
USER: nguyens1
PROG: nocows
LANG: C++
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <limits.h>

#include <iostream>
#include <fstream>
using namespace std;



string tidy(string td){
  
    int len = td.length();

    for (int i = len - 1; i > 0; --i){
            if (td[i] < td[i - 1] ){
                td[i] = '9';
                if (td[i - 1] > '0')
                    --td[i - 1];
            }else if (td[i] == '0' && td[i - 1] == '0'){
                td[i] = '9';
        }
    }

    int pos = td.find_first_of("0");
    if (pos != string::npos){
        td = td.substr(pos + 1,len - pos);
    }

    len = td.length();
    for (int i = 0; i < len - 1; ++i){
        if(td[i + 1] < td[i]){
            td[i + 1] += td[i] - td[i + 1];
        }
    }

    return td;
}

string arr[101];
int T;

int main(){
    freopen("B-large.in", "r", stdin);
    ofstream fout("output.txt");
    
    cin >> T;
    for (int i = 0; i < T; ++i){
        cin >> arr[i];
    }

    for (int i = 0; i < T; ++i){
       fout << "Case #" << i + 1 << ": " << tidy(arr[i]) << endl;
    }

    return 0;
}
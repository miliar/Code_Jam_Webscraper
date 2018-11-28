#include <iostream>
#include <vector>
#include <cstring>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <string>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>


using namespace std;

int pan(string str, int k){
    int counter = 0;
    for(int i = 0; i != str.size() - k + 1; ++i){
        if(str[i] == '-'){
            for(int j = i; j != i + k; ++j){
                if(str[j] == '-') str[j] = '+';
                else if(str[j] == '+') str[j] = '-';
            }
            counter++;
        }
    //    cout << str << endl;
    }
    bool works = true;
    for(int i = str.size() - 1; i != str.size() - k - 1; --i){
        if(str[i] == '-') works = false;
    }
    if(works) return counter;
    return -1;
}

int main() {

    string str;
    int t, s, answer;
    vector <int> lengths;
    vector <string> strs;
    vector <int> answers;
    cin >> t;

    for(int i = 0; i != t; ++i){
        cin >> str;
        cin >> s;
        lengths.push_back(s);
        strs.push_back(str);
    }

    for(int i = 0; i != t; ++i){
        answers.push_back(pan(strs[i], lengths[i]));
    }

    for(int i = 0; i != t; ++i){
        if(answers[i] != -1){
            cout << "Case #" << i + 1 << ": " << answers[i] << endl;
        } else{
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        }
    }

    return 0;

}

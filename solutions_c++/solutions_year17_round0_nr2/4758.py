#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

string n;
string myTry;

void color(int pos, char v){
    for(int i = pos;i < (int)myTry.size();i++) myTry[i] = v;
}

bool Try(int pos, char v){

    string cpy = myTry;
    for(int i = pos;i < (int)cpy.size();i++) cpy[i] = v;

    return cpy <= n;
}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int cases;
    cin >> cases;

    for(int tt = 1;tt <= cases;tt++){

        cin >> n;

        myTry.clear();
        for(int i = 0;i < (int)n.size();i++) myTry.push_back('1');

        cout << "Case #" << tt << ": ";
        

        if(myTry > n){ // if this is true, I'll have to pick a number with fewer digits
            for(int i = 1;i < (int)n.size();i++) cout << "9";
            cout << endl;
            
            continue;
        }

        int cur_s = 1;
        for(int i = 0;i < (int)n.size();i++){
            
            for(int j = cur_s;j <= 9;j++){
                
                if(!Try(i, j + '0')){
                    cur_s = j-1;
                    color(i, cur_s + '0');
                    break;
                }

                if(j == 9){
                    cur_s = 10;
                    color(i, '9');
                    break;
                }
            }
        }

        cout << myTry << endl;

    }

    return 0;
}

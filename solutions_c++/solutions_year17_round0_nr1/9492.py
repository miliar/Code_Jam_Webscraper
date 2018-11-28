#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;


void flip(string &s, int k, int i);

int main(){
    int t, k;
    string s;
    cin >> t;

    for (int it = 0; it < t; it++)
    {
    	cin >> s >>  k;
    	int counter = 0;
    	int possible = 1;
    	for (int i = 0; i < s.size(); i++) {

    		if(string(1, s[i]) == "-"){
                if(i+k <= s.size()){
                    flip(s, k, i);
                    counter++;
                }
                else {
                    possible = 0;
                }
    		}
    	}
        if(possible){
            cout << "Case #" << it+1 << ": " << counter << "\n";
        }
        else{
            cout << "Case #" << it+1 << ": " << "IMPOSSIBLE\n";
        }
    }

    return 0;
}

void flip(string &s, int k, int i){

    for(int j = i; j <i+k; j++){
        if(string(1, s[j]) == "-"){
            s.replace(j,1,"+");
        }
        else {
            s.replace(j,1,"-");
        }

    }
   // cout << s << "\n";
}

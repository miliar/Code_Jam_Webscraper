#include <iostream>
#include <string>
using namespace std;

int fix(string s,int i){


}

int chk(string s){




}

int main(){

    int t;
    string s;
    string k;
    cin >> t;
    int a = t;
    while(t--){
        cin >> s;
        int i = 0;
        bool chk;
        while(i != s.length()-1){

            if(s[i]>s[i+1]){
                s[i] -= 1;
                i = i+1;
                while(i!=s.length()){
                    s[i] = '9';
                    i++;
                }
                i = 0;
            }
            else i = i+1;
        }
        k = "";
        for(int i = 0;i<s.length();i++){
            if(s[i]!= '0') k = k +s[i];
        }

        cout << "Case #" << a-t << ": "<<k << endl;

    }




return 0;
}

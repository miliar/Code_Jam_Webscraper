#include <iostream>
#include <sstream>
#include <windows.h>

using namespace std;
string toString(int number){
    std::stringstream ss;
    ss << number;
    string str = ss.str();
    return str;
}
bool isTidy(int number){
    string number_string="";
   if(number <10){
        return true;
    }else{
        number_string = toString(number);
        int length = number_string.length();
        for(int i=0; i<length-1;i++){
            if(number_string[i]>number_string[i+1]){
                return false;
            }
        }
        return true;
    }
}
int tidy(int N){
    int last_tidy = 0;
    for(int i=N; i<=N;i--){
        if(isTidy(i)){
            return i;
        }
    }
    return last_tidy;
}

int main()
{
    int T=0;//Test cases
    int N=0;//single integer
    unsigned int y = 0;
    cin >>T;
    for(int x=1; x<=T; x++){
        cin >> N;
        y = tidy(N);
        cout << "Case #" << x << ": " << y <<endl;
    }
    return 0;
}

#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <sstream>
#include <stdlib.h>
using namespace std;
int convert (char newstring){
    if (newstring == '0'){
        return 0;
    }
    else if (newstring == '1'){
        return 1;
    }
    else if (newstring == '2'){
        return 2;
    }
    else if (newstring == '3'){
        return 3;
    }
    else if (newstring == '4'){
        return 4;
    }
    else if (newstring == '5'){
        return 5;
    }
    else if (newstring == '6'){
        return 6;
    }
    else if (newstring == '7'){
        return 7;
    }
    else if (newstring == '8'){
        return 8;
    }
    else{
        return 9;
    }
}
int main()
{
int n;
cin >> n;
long long int arr[n];
bool cool = false;
for (int i = 0; i < n; i++){
    cin >> arr[i];
}
//cout<< arr[3] <<endl;
for (int i = 0; i < n; i++){
    for (long long int j = arr[i]; j >= 0; j--){
        stringstream ss;
        ss << j << endl;
        string newstring = ss.str();
        //cout << newstring << endl;
        for (int k = 0; k < newstring.length()-1; k++){
            if (convert(newstring[k]) <= convert(newstring[k+1])){
                cool = true;
            }
            else{
                cool = false;
                break;
            }
        }
        if (cool == true){
            cout << "Case #" << i+1 << ": " << j << endl;
            break;
            }
        }
    }
}

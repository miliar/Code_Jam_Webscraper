#include <iostream>
#include <math.h>
#include <string.h>
using namespace std;
#define LENGTH 1001

char* stripZero(char number[LENGTH]){
    unsigned int i;
    int index = 0;
    int count = 0;
    while(number[count] == '0'){
        count++;
    }
    for(i = count; i < strlen(number); i++){
        number[index] = number[i];
        index++;
    }
    number[index] = '\0';
    return number;
}

bool isTidy(char number[LENGTH]){
    unsigned int i;
    if(strlen(number) == 1) return true;

    for(i = 0; i < strlen(number) - 1; i++){
        //cout << number[i] << " >= " << number[i + 1] << " = ";
        if(number[i] <= number[i + 1]){
            //cout << "true";
        }else{
            //cout < "false";
            return false;
        }
        //cout << endl;
    }
    return true;
}

char* findMost(char number[LENGTH]){
    bool isTidyNum = false;
    int lastIndex = strlen(number) - 1;
    int currIndex;
    while(!isTidyNum){
        //cout << "lastIndex = " << lastIndex << "\tnumber[lastIndex] = " << number[lastIndex] << "\tnumber =" << number << endl;
        if(number[lastIndex] == '0'){
            number[lastIndex] = '9';
            currIndex = lastIndex - 1;
            while(number[currIndex] == '0' && currIndex != 0){
                number[currIndex] = '9';
                currIndex--;
            }
            if(currIndex == -1){
                return stripZero(number);
            }else{
                number[currIndex] = number[currIndex] - 1;
            }
        }else{
            number[lastIndex] = number[lastIndex] - 1;
        }
        if(isTidy(number)){
            isTidyNum = true;
        }
        //isTidyNum = isTidy(number);
    }
    return stripZero(number);
}

int main(){
    int n;
    int i;
    cin >> n;
    char testcases[n][LENGTH];

    for(i = 0; i < n; i++){
        cin >> testcases[i];
    }

    for(i = 0; i < n; i++){
        if(isTidy(testcases[i])){
            cout << "Case #" << i + 1 << ": " << testcases[i] << endl;
        }else{
            cout << "Case #" << i + 1 << ": " << findMost(testcases[i]) << endl;
        }
    }
    return 0;
}
#include<iostream>
#include<string>
#include <queue>
#include <fstream>

using namespace std;

int main() {
    ofstream cop("op1.txt");
    ifstream cinp("in1.txt", ios::binary);
    int T, t=1;
    cinp >> T;
    for(;t <= T;t++){
        fflush(stdin);
        string num;
        cinp >> num;
        int length = 1, last_index = 0, index = 0, flag = 0;
        while(num[length] != 0) {
            if(num[length] < num[length-1]){
                num[last_index++]--;
                while(num[last_index] != 0)
                    num[last_index++] = '9';
                length = last_index;
                break;
            } else if(num[length] != num[length-1]) {
                last_index = length;
            }
            length++;
        }
        cop << "Case #" << t << ": ";
        for(;index < length;index++){
            if(flag == 0 && num[index] != '0')
                flag = 1;
            if(flag)
                cop << num[index];
        }
        cop << endl;
    }
}

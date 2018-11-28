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
        queue<int> locations;
        string pancake_row;
        int flipper, length=0, first_loc=-1, flips = 0, index, flip = 0;
        cinp >> pancake_row >> flipper;
        while(pancake_row[length] != 0) {
            if(first_loc == -1 && pancake_row[length] == '-')
            first_loc = length;
            length++;
        }

        if(first_loc == -1) {
            cop << "Case #" << t << ": " << 0 << endl;
            continue;
        }

        for(index = first_loc; index < length; index++) {
           if((!flip && pancake_row[index]=='-') || (flip && pancake_row[index]=='+')) {
               if(length - index < flipper)
                   break;
               locations.push(index + flipper -1);
               flip = (flip + 1) % 2;
               flips++;
           }
           if(index == locations.front()) {
               locations.pop();
               flip = (flip + 1) % 2;
           }
        }

        if(index == length)
            cop << "Case #" << t << ": " << flips << endl;
        else
            cop << "Case #" << t << ": IMPOSSIBLE" << endl;
    }
}

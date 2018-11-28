#include<iostream>
#include<string>
#include <queue>
#include <fstream>
#include<iomanip>

using namespace std;



int main() {
    ofstream cop("op1.txt");
    ifstream cinp("in1.txt", ios::binary);
    int T, t=1;
    cinp >> T;
    for(;t <= T;t++){
        fflush(stdin);
        int N, arr[6];
        cinp >> N >> arr[0] >> arr[3] >> arr[1] >> arr[4] >> arr[2] >> arr[5];
        string s;
        if((arr[5] == arr[1] && arr[5]+arr[1] == N) || (arr[4] == arr[0] && arr[4]+arr[0] == N) || (arr[3] == arr[2] && arr[2]+arr[3] == N) ) {
            if(arr[5] == arr[1]) {
                while(arr[5]!=0) {
                    s.append("VY");
                    arr[5]--;
                }
                cop << "Case #" << t << ": " << s << endl;
            }
            else if(arr[4] == arr[0]) {
                while(arr[4]!=0) {
                    s.append("GR");
                    arr[4]--;
                }
                cop << "Case #" << t << ": " << s << endl;
            }
            else {
                while(arr[3]!=0) {
                    s.append("BO");
                    arr[3]--;
                }
                cop << "Case #" << t << ": " << s << endl;
            }
            continue;
        }
        if((arr[5] >= arr[1] && arr[5] + arr[1] > 0) || (arr[4] >= arr[0] && (arr[4] + arr[0] > 0))|| (arr[3] >= arr[2] && (arr[3] + arr[2] > 0))|| ((arr[0]+arr[3]+arr[5]) >(arr[1]+arr[2])) || ((arr[1]+arr[3]+arr[4]) > (arr[0]+arr[2]))|| ((arr[2]+arr[4]+arr[5]) > (arr[0]+arr[1]))){
            // cop << (arr[5] >= arr[1]) << (arr[4] >= arr[0]) << (arr[3] >= arr[2]) << endl;
            // cop << ((arr[0]+arr[3]+arr[5]) >(arr[1]+arr[2])) << ((arr[1]+arr[3]+arr[4]) > (arr[0]+arr[2])) << ((arr[2]+arr[4]+arr[5]) > (arr[0]+arr[1])) << endl;
            // cop << arr[0] << " " << arr[1] << " " << arr[2] << " " << arr[3] << " " << arr[4] << " " << arr[5] << endl;
            cop << "Case #" << t << ": IMPOSSIBLE" << endl;
            continue;
        }
        int pref = -1, prev = -1;
        bool pos = true;
        for(int i=0;i<N;i++){
            int max = 0;
            if(arr[5] + arr[4] + arr[3] != 0) {
                if(arr[5]!=0) {
                    i = 2*arr[5]+1;
                }
                if(arr[4]!=0) {
                    i = 2*arr[4]+1;
                }
                if(arr[3]!=0) {
                    i = 2*arr[3]+1;
                }
                while(arr[5] != 0) {
                    if(pref == -1)
                        pref = 1;
                    s.append("YV");
                    arr[5]--;
                    arr[1]--;
                    if(arr[5] == 0) {
                        s.append("Y");
                        arr[1]--;
                        prev = 1;
                    }
                }
                while(arr[4] != 0) {
                    if(pref == -1)
                        pref = 0;
                    s.append("RG");
                    arr[4]--;
                    arr[0]--;
                    if(arr[4] == 0) {
                        s.append("R");
                        arr[0]--;
                        prev = 0;
                    }
                }
                while(arr[3] != 0) {
                    if(pref == -1)
                        pref = 2;
                    s.append("BO");
                    arr[3]--;
                    arr[2]--;
                    if(arr[3] == 0) {
                        s.append("B");
                        arr[2]--;
                        prev = 2;
                    }
                }
                i--;
                continue;
            }
            if(prev == -1) {
                if(arr[0] >= arr[1] && arr[0] >= arr[2]) {
                    s.append("R");
                    arr[0]--;
                    prev = 0;
                    pref = 0;
                }
                else if(arr[1] >= arr[2]) {
                    s.append("Y");
                    arr[1]--;
                    prev = 1;
                    pref = 1;
                }
                else {
                    s.append("B");
                    arr[2]--;
                    prev = 2;
                    pref = 2;
                }
            }
            else {
                if(prev == 0) {
                    if(arr[1] > arr[2] || (arr[1] == arr[2] && pref <= 1)) {
                        prev = 1;
                        arr[1]--;
                        s.append("Y");
                    }
                    else {
                        prev = 2;
                        arr[2]--;
                        s.append("B");
                    }
                }
                else if(prev == 1) {
                    if(arr[0] > arr[2] || (arr[0] == arr[2] && pref <= 1)) {
                        prev = 0;
                        arr[0]--;
                        s.append("R");
                    }
                    else {
                        prev = 2;
                        arr[2]--;
                        s.append("B");
                    }
                } else {
                    if(arr[0] > arr[1] || (arr[0] == arr[1] && pref != 1)) {
                        prev = 0;
                        arr[0]--;
                        s.append("R");
                    }
                    else {
                        prev = 1;
                        arr[1]--;
                        s.append("Y");
                    }
                }
            }
        }
        cop << "Case #" << t << ": " << s << endl;
    }
    return 0;
}

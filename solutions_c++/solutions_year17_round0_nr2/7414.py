#include <iostream>
#include "TMath.h"
#include<fstream>
#include<vector>

#include<string>

using namespace std;
using namespace TMath;

int CountTheSheep(int num);

int main() {

    ifstream inPutFile;
    ofstream outPutFile;

    inPutFile.open("/Users/zhuj/Downloads/A-large-practice.in");
    outPutFile.open("/Users/zhuj/Downloads/A-output.txt");

    if(!inPutFile){
        cout<<"can not find the doc"<<endl;
    }

    int t, n, m;
    inPutFile >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        inPutFile >> n;  // read n and then m.
        m = CountTheSheep(n);
        if (m == 0) {
            outPutFile << "Case #" << i << ": " <<"INSOMNIA" << endl;

        } else {
            outPutFile << "Case #" << i << ": " << m << endl;
            // cout knows that n + m and n * m are ints, and prints them accordingly.
            // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
            // MY_PROGRAM < small_input.txt > small_output.txt
        }
    }

    inPutFile.close();
    outPutFile.close();

//    cin >> t;
//    for (int i = 1; i <= t; ++i) {
//        cin >> n;
//        m = CountTheSheep(n);
//        if (m == 0) {
//            cout << "Case #" << i << ": " <<"INSOMNIA" << endl;
//        } else {
//            cout << "Case #" << i << ": " << m << endl;
//        }
//    }

    return 0;
}

int CountTheSheep(int num){

    bool n1=false, n2=false, n3=false, n4=false, n5=false, n6=false, n7=false, n8=false, n9=false, n0=false;
    int ans;

    //j and i are the  boundary number
    for(int j=1;j<100;j++) {
        int loopNum = j * num;
        for (int i = 1; i < 10; i++) {
            int temp = (loopNum % ((int) pow(10, i)));
            int comp = temp / (int) pow(10, i - 1);

            switch (comp) {
                case 1:
                    n1 = true;break;
                case 2:
                    n2 = true;break;
                case 3:
                    n3 = true;break;
                case 4:
                    n4 = true;break;
                case 5:
                    n5 = true;break;
                case 6:
                    n6 = true;break;
                case 7:
                    n7 = true;break;
                case 8:
                    n8 = true;break;
                case 9:
                    n9 = true;break;
                case 0:
                    n0 = true;break;
            }

            loopNum = loopNum - temp;

            if (loopNum / ((int) pow(10, i)) == 0) {
                break;
            }
            }
        if (n1 && n2 && n3 && n4 && n5 && n6 && n7 && n8 && n9 && n0) {
            ans = j * num;
            break;
        }

        if(j>100){
            ans=0;
        }
        if(num==0){
            ans=0;
        }
    }
    return ans;

}
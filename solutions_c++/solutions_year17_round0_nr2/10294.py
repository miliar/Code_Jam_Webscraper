#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h>

using namespace std;

int T;
int p = 1;
int o = 0;
int length;
int aArray[100];
string testing;
string N1, N2, N3, N4;
int n1, n2, n3, n4;
int complete = 0;

int main(){
    ofstream myfile;

    string line;
    ifstream infile;
    infile.open ("B-small-attempt0.in");//Name of File that must exist in the same folder as the project
    while (getline(infile, line)){

        istringstream iss(line);

        if(p == 1){
            if(!(iss >> T)) { break;}
            p = 0;
        }
        else{
            int a;
            if(!(iss >> a)) {break;}
            aArray[o] = a;
            o++;
        }
    }

    o = 0;

    while(o<100){

        stringstream ss;
        ss << aArray[o];
        string testing = ss.str();

        length = testing.length();

        if(length == 1){
            N1 = testing[0];
            cout << "Case #" << o + 1 << ": " << testing << endl;
                complete = 1;
        }
        if(length == 2){
            N1 = testing[0];
            N2 = testing[1];

            n1 = atoi(N1.c_str());
            n2 = atoi(N2.c_str());

            if(n1<=n2){
                cout << "Case #" << o + 1 << ": " << testing << endl;
                complete = 1;
            }
            else{
                aArray[o] = aArray[o] - 1;
            }
        }
        if(length == 3){
            N1 = testing[0];
            N2 = testing[1];
            N3 = testing[2];

            n1 = atoi(N1.c_str());
            n2 = atoi(N2.c_str());
            n3 = atoi(N3.c_str());

            if(n1<=n2 & n2<=n3){
                cout << "Case #" << o + 1 << ": " << testing << endl;
                complete = 1;
            }
            else{
                aArray[o] = aArray[o] - 1;
            }
        }
        if(length == 4){
            N1 = testing[0];
            N2 = testing[1];
            N3 = testing[2];
            N4 = testing[3];

            n1 = atoi(N1.c_str());
            n2 = atoi(N2.c_str());
            n3 = atoi(N3.c_str());
            n4 = atoi(N4.c_str());

            if(n1<=n2 & n2<=n3 & n3<=n4){
                cout << "Case #" << o + 1 << ": " << testing << endl;
                complete = 1;
            }
            else{
                aArray[o] = aArray[o] - 1;
            }
        }

        if(complete == 1){
            o++;
            complete = 0;
        }
        if(o>T-1){
            break;
        }
    }

    return 0;
}

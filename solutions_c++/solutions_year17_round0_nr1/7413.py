#include <iostream>
#include "TMath.h"
#include<fstream>
#include<vector>

#include<string>

using namespace std;
using namespace TMath;

vector<int> pancake;


long PancakeFlipper(long N);

int main() {

    ifstream inPutFile;
    ofstream outPutFile;

    inPutFile.open("/Users/zhuj/Downloads/A-large.in");
    outPutFile.open("/Users/zhuj/Downloads/A-output.txt");

    if(!inPutFile){
        cout<<"can not find the doc"<<endl;
    }

    long t, n, m;
    string s;

    inPutFile >> t;
    for (long i = 1; i <= t; ++i) {
        pancake.clear();
        inPutFile >> s >> n;
        string::iterator t;
        for(t=s.begin(); t!=s.end(); t++){
            if(*t=='+'){
                pancake.push_back(1);
            }else if(*t=='-'){
                pancake.push_back(-1);
            }
        }
        m=PancakeFlipper(n);
        if(m==-1) {
            outPutFile << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
        } else {
            outPutFile << "Case #" << i << ": " << m << endl;
        }
    }

    inPutFile.close();
    outPutFile.close();

//    cin >> t;
//    for (long i = 1; i <= t; ++i) {
//        pancake.clear();
//        cin >> s >> n;
//        string::iterator t;
//        for(t=s.begin(); t!=s.end(); t++){
//            if(*t=='+'){
//                pancake.push_back(1);
//            }else if(*t=='-'){
//                pancake.push_back(-1);
//            }
//        }
//
////        vector<int>::iterator t2;
////        for(t2=pancake.begin(); t2!=pancake.end(); t2++){
////            cout<<*t2;
////        }
//        m=PancakeFlipper(n);
//        if(m==-1) {
//            cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
//        } else {
//            cout << "Case #" << i << ": " << m << endl;
//        }
//    }


    return 0;
}

long PancakeFlipper(long N){
    long ans=0;
    long check=0;
    for(long i=0;i<=pancake.size()-N;++i){
        if(pancake[i]==-1) {
            for (int j = i; j < i + N; j++) {
                pancake[j] = pancake[j] * (-1);
            }
            ans++;

        }
    }
    for(long i=pancake.size()-N;i<pancake.size();i++){
        check=pancake[i];
        if(pancake[i]==-1) ans=-1;
    }
    return ans;
}

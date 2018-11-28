#include <iostream>
#include <TMath.h>
#include<fstream>
#include<vector>
#include <set>
#include <iterator>
#include<string>
#include <set>
#include <iomanip>

using namespace std;
using namespace TMath;

set<double> horses;

void A(int n,int m);

int main() {


    ifstream inPutFile;
    ofstream outPutFile;

    inPutFile.open("/Users/zhuj/Downloads/A-large.in");
    outPutFile.open("/Users/zhuj/Downloads/a1-output.txt");

    if (!inPutFile) {
        cout << "can not find the doc" << endl;
    }

    string s1, s2, s3;
    int t, n, m;
    int k, s;
    double vhos;


    inPutFile >> t;
    for (int i = 1; i <= t; ++i) {
        horses.clear();
        inPutFile >> n >> m;
        for (int j = 1; j <= m; j++) {
            inPutFile >> k >> s;
            vhos = (n - k) * 1.0 / s;

            horses.insert(vhos);
        }
//        A(n, m);

        set<double>::iterator t2;
        t2=horses.end();
        t2--;
        double bspeed = n/(*t2);
        outPutFile<<fixed<<setprecision(6) << "Case #" << i << ": " << bspeed<< endl;
    }

    inPutFile.close();
    outPutFile.close();

//    cin >> t;
//    for (int i = 1; i <= t; ++i) {
//        horses.clear();
//        cin >> n >> m;
//        for (int j = 1; j <= m; j++) {
//            cin >> k >> s;
//            vhos = (n - k) * 1.0 / s;
//
//            horses.insert(vhos);
//        }
////        A(n, m);
//
//        set<double>::iterator t2;
//        t2=horses.end();
//        t2--;
//        double bspeed = n/(*t2);
//        cout<<fixed<<setprecision(6) << "Case #" << i << ": " << bspeed<< endl;
//    }

    return 0;
}

void A(int d, int n) {



}

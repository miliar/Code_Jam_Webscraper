#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <time.h>       /* time */
#include <algorithm>
#include <list>
#include <utility>
#include <stack>
#include <math.h>
#include <iomanip>
#include <tuple>
#include "boost/graph/adj_list_serialize.hpp"
#include "/home/simon/ClionProjects/CodeJamBasics/Graph.h"
#include "/home/simon/ClionProjects/CodeJamBasics/Helper.h"


// int foo [5]={1,1,1,1,1};
using namespace std;

typedef long long int Lint;
typedef long double Ldouble;


int main() {
    Helper help;
    Lint a = 3;
    ofstream outfile;
    outfile.open("solution.out");
    std::ifstream infile;
    infile.open("data.in", std::ifstream::in);
    std::string line;
    getline(infile, line);
    std::stringstream lineStream(line);
    int T;
    lineStream >> T;
    for (int caseNr = 1; caseNr <= T; caseNr++) {
        cout << "Solving case number " << caseNr << endl;
        int A, B;
        getline(infile, line);
        std::stringstream Stream1(line);
        Stream1 >> A >> B;
        vector<tuple<int, int, int> > chores, choresA, choresB;
        for (int j = 0; j < A; j++) {
            int s, t;
            getline(infile, line);
            std::stringstream Stream2(line);
            Stream2 >> s >> t;
            chores.push_back(make_tuple(s, t, 0));

            choresA.push_back(make_tuple(s, t, 0));
        }
        for (int j = 0; j < B; j++) {
            int s, t;
            getline(infile, line);
            std::stringstream Stream2(line);
            Stream2 >> s >> t;
            chores.push_back(make_tuple(s, t, 1));

            choresB.push_back(make_tuple(s, t, 0));
        }
        vector<tuple<int, int, int> > sort_chores = chores;

        vector<tuple<int, int, int> > sort_choresA = choresA;

        vector<tuple<int, int, int> > sort_choresB = choresB;
        sort(sort_choresA.begin(), sort_choresA.end());
        sort(sort_choresB.begin(), sort_choresB.end());
        for (int i = 0; i < sort_choresA.size(); i++) {
            cout << get<0>(sort_choresA[i]) << "\t" << get<1>(sort_choresA[i]) << endl;
        }
        for (int i = 0; i < sort_choresB.size(); i++) {
            cout << get<0>(sort_choresB[i]) << "\t" << get<1>(sort_choresB[i]) << endl;
        }
        int index = 0;
        vector<int> gaps1;
        vector<int> gaps1ob;
        vector<int> gaps2ob;
        vector<int> gaps2;
        for (int i = 0; i < A-1; i++) {
            int begin = get<1>(sort_choresA[i]);
            int end = get<0>(sort_choresA[i + 1]);
            while (index < B && get<1>(sort_choresB[index]) < begin) {
                index++;
            }
            if (index < B && get<1>(sort_choresB[index]) < end) {
                gaps1ob.push_back(end - begin);
            } else {
                gaps1.push_back(end - begin);
            }
        }
        if (A > 0 && B > 0 && (get<0>(sort_choresB[0]) < get<0>(sort_choresA[0]) ||
                               get<0>(sort_choresB[B - 1]) > get<1>(sort_choresA[A - 1]))) {
            gaps1ob.push_back(get<0>(sort_choresA[0]) - get<1>(sort_choresA[A - 1]) + 1440);
        } else if (A > 0) {
            gaps1.push_back(get<0>(sort_choresA[0]) - get<1>(sort_choresA[A - 1]) + 1440);
            //cout<<"round gap "<<get<0>(sort_choresA[0])<< "\t" << get<1>(sort_choresA[A - 1])<<endl;
        }
        index = 0;
        for (int i = 0; i < B-1; i++) {
            if (i < (sort_choresB.size() - 1)) {
                int begin = get<1>(sort_choresB[i]);
                int end = get<0>(sort_choresB[i + 1]);
                while (index < A && get<1>(sort_choresA[index]) < begin) {
                    index++;
                }
                if (index < A && get<1>(sort_choresA[index]) < end) {
                    gaps2ob.push_back(end - begin);
                } else {
                    gaps2.push_back(end - begin);
                }
            }
        }
        if (A > 0 && B > 0 && (get<0>(sort_choresA[0]) < get<0>(sort_choresB[0]) ||
                               get<0>(sort_choresA[A - 1]) > get<1>(sort_choresB[B - 1]))) {
            gaps2ob.push_back(get<0>(sort_choresB[0]) - get<1>(sort_choresB[B - 1]) + 1440);
        } else if (B > 0) {
            gaps2.push_back(get<0>(sort_choresB[0]) - get<1>(sort_choresB[B - 1]) + 1440);
        }
        if(A==0){
            gaps1ob.push_back(1440);
        }
        if(B==0){
            gaps2ob.push_back(1440);
        }
        sort(gaps1.begin(), gaps1.end());
        sort(gaps2.begin(), gaps2.end());
       /* cout<<"gaps1"<<endl;
        for(int i=0;i<gaps1.size();i++){
            cout<<gaps1[i]<<endl;
        }
        cout<<"gaps2"<<endl;
        for(int i=0;i<gaps2.size();i++){
            cout<<gaps2[i]<<endl;
        }
        cout<<"gaps1ob"<<endl;
        for(int i=0;i<gaps1ob.size();i++){
            cout<<gaps1ob[i]<<endl;
        }
        cout<<"gaps2ob"<<endl;
        for(int i=0;i<gaps2ob.size();i++){
            cout<<gaps2ob[i]<<endl;
        }
        cout<<"end"<<endl;*/
        int sum1 = 0;
        int sum2 = 0;
        int change1 = 0;
        int change2 = 0;
        for (int i = 0; i < gaps1ob.size(); i++) {
            sum1 += gaps1ob[i];
            change1++;
        }
        int pos = gaps1.size() - 1;
        if(pos>=0) {
        }
        while (sum1 < 720) {
            sum1 += gaps1[pos];
            pos--;
            change1++;
        }
        for (int i = 0; i < gaps2ob.size(); i++) {
            sum2 += gaps2ob[i];
            change2++;
        }
        pos = gaps2.size() - 1;
        while (sum2 < 720) {
            sum2 += gaps2[pos];
            pos--;
            change2++;
        }


        outfile << "Case #" << caseNr << ": ";
        outfile << 2*max(change1, change2);
        outfile << endl;
    }

    infile.close();
    outfile.close();

    return 0;
}







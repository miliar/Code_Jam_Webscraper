//
//  codejam.cpp
//  codejam
//
//  Created by Zimu Wang on 4/8/17.
//
//

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

bool comp (pair<long long, long long> i,pair<long long, long long> j) { return (i.first<j.first); }
int main(){
    ifstream fin ("A-small-attempt6.in");
    ofstream fout ("A-small-attempt6.out");
    int cases;
    fin >> cases;
    double answer, time;
    long long distance, numHorses;
    long long position, speed;
    vector<pair<long long, long long> > horses;
    int count = 0;
    bool correct;
    fout <<fixed;
    fout <<setprecision(7);
    for (int i=0;i<cases;i++){
        fin >> distance >> numHorses;
        horses.clear();
        answer = 0;
        for (int j=0;j<numHorses;j++){
            fin >>position >> speed;
            horses.push_back(make_pair(position, speed));
        }
        sort(horses.begin(), horses.end(),comp);
        count = -1;
        for (int k = 0;k<horses.size()-1;k++){
            if (horses[k].second < horses[k+1].second){
                count = k;
                break;
            }
        }
        if (count == -1){
            count = horses.size()-1;
        }
        cout<<count <<endl;
        cout <<endl;
        for (int l = count;l>=0;l--){
            cout << distance<<endl;
            cout << horses[l].first <<endl;
            cout <<horses[l].second<<endl;
            time = ((distance - horses[l].first) / (double)horses[l].second);
            cout <<time<<endl;
            correct = true;
            answer = distance / time;
            cout <<answer<<endl<<endl;
            for (int j = 0;j<l;j++){
                if (answer > horses[j].second)
                    if ((horses[j].first / (answer - horses[j].second)) < time){
                        correct = false;
                    }
            }
            if (correct){
                break;
            }
        }
        fout << "Case #" << i+1 << ": " <<answer << endl;
        
    }
    fout.close();
}

#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <algorithm>
#include <fstream>
#include <utility>
#define MAX 9999999999
#define NUM 2
using namespace std;
typedef long long ll;

int main () {
    ifstream input("/Users/ahnzeus/Desktop/input.in");
    ofstream output("/Users/ahnzeus/Desktop/output.txt");
    
    int T;
    //cin >> T;
    input >> T;
    for(int t=1;t<=T;t++){
        int ac,aj;
        //cin >> ac >> aj;
        input >> ac >> aj;
        
        pair<int,int> c[NUM],j[NUM];
        for(int i=0;i<ac;i++)
            input >> c[i].first >> c[i].second;
            //cin >> c[i].first >> c[i].second;
        for(int i=0;i<aj;i++)
            //cin >> j[i].first >> j[i].second;
            input >> j[i].first >> j[i].second;
        
        int res =0;
        if(ac+aj==1) res = 2;
        else if(ac==1 && aj==1) res = 2;
        else {
            pair<int,int> tot[NUM];
            for(int i=0;i<ac;i++)
                tot[i] = c[i];
            for(int i=0;i<aj;i++)
                tot[i] = j[i];
            
            sort(tot,tot+NUM);
            if(tot[1].second - tot[0].first <= 720) res = 2;
            else {
                if(1440+tot[0].second-tot[1].first <= 720) res = 2;
                else res = 4;
            }
        }
        
        //cout << "Case #" << t << ": " << res << endl;
        output << "Case #" << t << ": " << res << endl;
    }
}

//#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<iterator>
#include<unordered_map>
#include<unordered_set>
#include<assert.h>
#include <iomanip>
using namespace std;



ifstream cin("/Users/naginahas/Downloads/A-Large (1).in");
ofstream cout("/Users/naginahas/Downloads/Aqqqqqq.txt");




int main(int argc, const char * argv[]) {
    
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        vector <int> K;
        vector <int> S;
        int N, D;
        cin >> D>> N;
        vector <double> ft;
        for(int i=0;i<N;i++){
            int k,s;
            cin >> k >> s;
            K.push_back(k);
            S.push_back(s);
            ft.push_back(double(D-K[i])/S[i]);
        }
        double x = *max_element(ft.begin(),ft.end());
        //cout  << endl;
        
        
        
       
        
        cout << "Case #" << t+1 << ": " << fixed << setprecision(10) << D/x <<endl;
    }
    return 0;
}

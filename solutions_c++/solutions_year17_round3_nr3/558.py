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



ifstream cin("/Users/naginahas/Downloads/C-small-1-attempt0.in");
ofstream cout("/Users/naginahas/Downloads/Czzzzzz.txt");


bool f(vector <double> vd, double lev, double u){
    double sum = 0;
    for(int i=0;i<vd.size();i++){
        if(vd[i] < lev) {
            sum+= lev-vd[i];
        }
        
    }
    if(sum<=u) return true;
    else return false;
}

int main(int argc, const char * argv[]) {
    
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        int N, K;
        cin >> N >> K;
        double U;
        cin >> U;
        vector <double> vd;
        for(int i=0;i<N;i++){
            double d;
            cin >> d;
            vd.push_back(d);
        }
        double mx=1;
        double mn=0;
        while(mx-mn>1e-12){
            double mid = (mx+mn)/2.0;
            bool b = f(vd,mid,U);
            if(b) mn = mid;
            else mx =mid;
        }
        double prod =1.0;
        for(int i=0;i<vd.size();i++){
            if(vd[i] < mn) {
                prod = prod *mn;
            }
            else prod = prod*vd[i];
            
        }
        cout << "Case #" << t+1 << ": "<< fixed << setprecision(10) << prod << endl;
    }
    return 0;
}


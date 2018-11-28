#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <iomanip>
#include <queue>
#include <iterator>
#include <fstream>
#include <cmath>
using namespace std;



int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
#define cin in
#define cout out

    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++) {
        cout<<"Case #"<<cas<<": ";
        int D,N;
        cin>>D>>N;
        vector<double> v(N);
        vector<double> pos(N);
        for(int c=0;c<N;c++){
            cin>>pos[c]>>v[c];
        }
        double maxTime = 0;
        for(int c=N-1;c>=0;c--) {
            maxTime = max(maxTime,(D-pos[c])/v[c]);
        }
        cout<<fixed<<setprecision(8)<<static_cast<double>(D)/maxTime<<endl;
    }

}

#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <algorithm>
#include <fstream>
#include <utility>
#define MAX 987654321
using namespace std;
typedef long long ll;

pair<int,int> divide(int n){
    if(n%2==0){
        return make_pair(n/2-1, n/2);
    }
    return make_pair(n/2, n/2);
}

int main () {
    ifstream input("/Users/ahnzeus/Desktop/input.in");
    ofstream output("/Users/ahnzeus/Desktop/output.txt");
    
    int T;
    //cin >> T;
    input >> T;
    
    for(int t=1;t<=T;t++){
        int n,k,a;
        pair<int,int> p;
        //cin >> n >> k;
        input >> n >> k;
        
        a = pow(2,(int)log2(k));
        
        int s = (n-(a-1))/a;
        int r = (n-(a-1))%a;
        
        int idx = k-a;
        if(idx+1 <= r){
            p = divide(s+1);
        }else{
            p = divide(s);
        }
        output <<"Case #"<<t<<": "<< p.second << " " << p.first << endl;
        //cout <<"Case #"<<t<<": "<< p.second << " " << p.first << endl;
    }
}

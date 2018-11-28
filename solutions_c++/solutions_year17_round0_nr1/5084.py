#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <algorithm>
#include <fstream>
#define MAX 987654321
using namespace std;
typedef long long ll;

int main () {
    ifstream input("/Users/ahnzeus/Desktop/input.in");
    ofstream output("/Users/ahnzeus/Desktop/output.txt");
    
    int T;
    input >> T;
    for(int t=1;t<=T;t++){
        string s;
        int k,ans=0;
        input >> s >> k;
        vector<int> v(s.size());
        
        for(int i=0;i<v.size();i++){
            s[i] == '+' ? v[i] = 1 : v[i] = -1;
        }
        
        for(int i=0;i<=v.size()-k;i++){
            if(v[i]!=1){
                for(int j=i;j<i+k;j++){
                    v[j]*=(-1);
                }
                ans+=1;
            }
        }
        
        for(int i=0;i<v.size();i++){
            if(v[i]!=1){
                output<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
                break;
            } else if(i==v.size()-1){
                output<<"Case #"<<t<<": "<<ans<<endl;
            }
        }
    }
}

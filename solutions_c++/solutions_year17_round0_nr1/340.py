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

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

ifstream cin("/Users/naginahas/Downloads/A-large.in");
ofstream cout("/Users/naginahas/Downloads/Aqqqqq.txt");


int f(string s,int K){
    if(s.size()==K) {
        if(s.find_first_not_of(s.substr(0,1))!=string::npos){
            return 100000000;
        }
        else if(s[0] == '+') return 0;
        else return 1;
    }
    int ret = 0;
    if(s[0]=='-'){
        ret+=1;
        for(int i=0;i<K;i++){
            if(s[i]=='+') s[i] = '-';
            else s[i] = '+';
        }
    }
    return ret + f(s.substr(1),K);
}

int main(int argc, const char * argv[]) {
    
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        int K;
        string s;
        cin >> s >> K;
        int n = f(s,K);
        if (n>100000) cout << "Case #" << t+1 << ": " << "IMPOSSIBLE" << endl;
        else cout << "Case #" << t+1 << ": " << n <<  endl;
    }
    return 0;
}

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

ifstream cin("/Users/naginahas/Downloads/B-large.in");
ofstream cout("/Users/naginahas/Downloads/Bqqqqq.txt");

int main(int argc, const char * argv[]) {
    
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        string s;
        cin >> s;
        string current;
        for(int i=0;i<s.size();i++) current+='0';
        
        for(int i=0;i<s.size();i++){
            string current2 = current;
            for(int j = current[i];j<='9';j++){
                for(int k=i;k<s.size();k++){
                    current2[k] = j;
                }
                if(current2<=s) current = current2;
                
            }
            //cout << current << endl;
        }
        int ind = current.find_first_not_of("0");
        if(ind ==-1) current = "0";
        else
        current = current.substr(ind);
        cout << "Case #" << t+1 << ": " << current<< endl;
    }
    return 0;
}

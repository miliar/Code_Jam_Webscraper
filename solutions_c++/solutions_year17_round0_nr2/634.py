#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
bool test(string str, long first, long val, bool bound){
    if(first==str.length()){
        return true;
    }
    if(!bound){
        return true;
    }
    char ch = (char)('0'+val);
    if(ch<str[first]){
        return true;
    }
    if(ch==str[first]){
        return test(str,first+1,val,bound);
    }
    return false;
}
int main() {
    long cases;
    ifstream in("tidynumbers.in");
    ofstream out("tidynumbers.out");
    in >> cases;
    for(long q=1; q<=cases; q++){
        out << "Case #" << q << ": ";
        string s;
        in >> s;
        if(s.length()==1){
            out << s << endl;
            continue;
        }
        string ans = "";
        for(long i = 1; i<s.length(); i++){
            ans += "9";
        }
        if(test(s,0,1,true)){
            ans = "";
            bool bound = true;
            for(long i = 0; i<s.length(); i++){
                long best = 1;
                for(long j = 2; j<=9; j++){
                    if(!test(s,i,j,bound)){
                        break;
                    }
                    best++;
                }
                char ch = (char)(best+'0');
                out << best;
                ans += (best+"");
                
                if(s[i]!=ch){
                    bound = false;
                }
            }
            out << endl;
        }
        else{
            out << ans << endl;
        }
        
    }
    
    
    return 0;
}
#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>
#include <limits.h>
#include <queue>


using namespace std;


string flip(string str, int i, int k){

    for(int j=0; j<k; j++){
        str[i+j] = str[i+j] == '+' ? '-' : '+';
    }
    
    return str;
}

int main(){
    
    int T;
    
    scanf("%d", &T);
    
    for(int t=1; t<=T; t++){
    
        string str;
        int k;
        
        cin >> str >> k;
        
        string sideup(str.size(), '+');
        
        set<string> myset;
        
        int minFlips = INT_MAX;
        
        if(str == sideup){
            minFlips = 0;
        }
        else{   
        
            queue< pair<string, int> > fifo;
            
            fifo.push( make_pair(str, 0) );
            
            while(!fifo.empty()){
            
                pair<string, int> p = fifo.front();
                fifo.pop();
                
                //cout << p.first << endl;
                
                if( myset.find(p.first) == myset.end() ){
                    
                    if(p.first == sideup){
                        minFlips = p.second;
                        break;
                    }
                    
                    myset.insert(p.first);
                    
                    for(int i=0; i<=str.size()-k; i++){
                        string s = flip(p.first, i, k);
                        
                        //cout << s << endl;
                        
                        if( myset.find(s) == myset.end() ){
                            fifo.push( make_pair(s, p.second+1) );
                        }
                    }
                       
                }
            
            }
        }
        
        if(minFlips == INT_MAX)
            printf("Case #%d: IMPOSSIBLE\n", t);
        else
            printf("Case #%d: %d\n", t, minFlips);      
        
    }
    
    return 0;
}

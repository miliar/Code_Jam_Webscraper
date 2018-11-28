//
//  main.cpp
//  CodeJam
//
//  Created by Ajit kumar chakra on 18/01/1939 Saka.
//  Copyright © 1939 Saka Ajit kumar chakra. All rights reserved.
//

#include <string>
#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    freopen("/Users/Ajit.chakra/Desktop/programs/inpyt.txt", "r",stdin );
    freopen("/Users/Ajit.chakra/Desktop/programs/output1.txt", "wb+",stdout );
    int t;cin>>t;
    for(int tt=1;tt<=t;tt++){
        int cnt = 0 ;
        string s ;cin>>s;int k;cin>>k;
        for(int i=0;i<s.length()-k+1;i++){
            if(s[i] == '-'){
                for(int j=i;j<i+k;j++){
                    s[j] = (s[j]=='+')?'-':'+' ;
                }
                cnt++ ;
            }
        }
        bool bb = false ;
        for(unsigned long i=s.length()-k;i<s.length();i++){
            if(s[i]=='-'){
                cout<<"Case #"<<tt<<": "<<"IMPOSSIBLE"<<endl;
                bb = true   ;
                break;
            }
        }
        if(bb)continue;
        cout<<"Case #"<<tt<<": "<<cnt<<endl;
    }
    return 0;
}

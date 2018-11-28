//
//  main.cpp
//  CodeJam
//
//  Created by Ajit kumar chakra on 18/01/1939 Saka.
//  Copyright © 1939 Saka Ajit kumar chakra. All rights reserved.
//

#include <string>
#include <iostream>
#include <vector>
using namespace std;

void solveA(){
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
}
void solveB()
{
    int t ;cin>>t ;

    for(int tt = 1;tt<=t;tt++){
        
        unsigned long long int n,l ;cin>>n;l=n;
        vector<int> vec ;
        while(l){
            vec.insert(vec.begin(),l%10);
            l /= 10 ;
        }
        for(unsigned long int i=vec.size()-1;i>0;i--){
            if(vec[i-1] > vec[i]){
                vec[i-1] -= 1 ;
                for(unsigned long int j=i;j<vec.size();j++)vec[j] = 9 ;
            }
        }
        
        int start=0;
        while(vec[start]==0)start++ ;
        cout<<"Case #"<<tt<<": ";
        for(auto i=vec.begin()+start;i != vec.end();i++)cout<<(*i);
        cout<<endl;
        
    }
}
int main(int argc, const char * argv[]) {
    freopen("/Users/Ajit.chakra/Desktop/programs/input.txt", "r",stdin );
    freopen("/Users/Ajit.chakra/Desktop/programs/output1.txt", "wb+",stdout );
    //solveA();
    solveB();
    return 0;
}


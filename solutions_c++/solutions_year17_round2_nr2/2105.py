//
//  main.cpp
//  dfd
//
//  Created by srikar on 28/03/17.
//  Copyright © 2017 srikar. All rights reserved.
//

#include <iostream>
#include <string>
#include <queue>
#include <unordered_map>
#include<limits.h>
#include <fstream>
using namespace std;
int main() {
    int t;
    cin >> t;
    int l=1;
    ofstream myfile;
    myfile.open ("example2.txt");
    while(t--){
        int n,r,o,y,g,b,v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        int yel=o+y+g;
        int red=o+v+r;
        int blu=o+g+b;
        int imp=0;
        if(n%2==0){
            if(yel>n/2 || red>n/2 || blu>n/2)
                imp=1;
        
        }else {
            if(yel>(n-1)/2 || red>(n-1)/2 || blu >(n-1)/2)
                imp=1;
        }
        string s="";
        
        if(max(red,max(blu,yel))==red)
        {    s="R";
            red--;
        }
        else if(max(red,max(blu,yel))==blu)
        { s="B";
            blu--;
        }
        else if(max(red,max(blu,yel))==yel)
        {   s="Y";
            yel--;
        }
        while((red!=0 || blu!=0 || yel!=0) && imp==0){
            if(s[s.length()-1]=='B'){
                if(red>yel ||(yel ==red && s[0]=='R'))
                {  s+='R';
                    red--;
                }
                 else
                 {  s+='Y';
                     yel--;
                 }
            
            }else  if(s[s.length()-1]=='Y'){
                if(red>blu ||(blu ==red && s[0]=='R'))
                { s+='R';
                    red--;
                }
                else{
                    s+='B';
                    blu--;
                }
                
            }else if(s[s.length()-1]=='R' ){
                if(blu>yel ||(blu ==yel && s[0]=='B'))
                { s+='B';
                    blu--;
                }
                else{
                        s+='Y';
                    yel--;
                }
                
            }
        
        }
        myfile << "Case #";
        myfile << l;
        myfile << ": ";
        if(imp==0)
            myfile << s<< endl;
        else
            myfile << "IMPOSSIBLE"<< endl;
        l++;
        
    }
    return 0;
}

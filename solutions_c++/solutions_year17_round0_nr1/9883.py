//

//  main.cpp

//  CodeJamQual1

//

//  Created by Jeong Yang on 4/8/17.

//  Copyright © 2017 Jonathan Yang. All rights reserved.

//



#include <iostream>

#include <fstream>

using namespace std;

int t, k, size;

bool check = false;

int mini = 0;

bool arr[11];

int count1 = 0;



ifstream fin("input.rtf");

ofstream fout("output.rtf");





void flip(int a, int b){
    
    for(int x = a; x<=b; x++){
        
        arr[x] = !arr[x];
        
    }
    
}



int main() {
    
    cin>>t;
    
    for(int x = 0; x<t; x++){
        
        string s;
        
        cin>>s;
        
        size = s.size();
        
        cin>>k;
        
        for(int y = 0; y<s.size(); y++){
            
            if(s[y] == '+'){
                
                arr[y]= true;
                
            }
            
            else{
                
                arr[y] = false;
                
            }
            
        }
        
        mini = 0;
        
        count1++;
        
        for(int y = 0; y<=size-k; y++){
            
            if(arr[y] == false){
                
                flip(y, y+k-1);
                
                mini++;
                
            }
            
        }
        
        bool check = true;
        
        for(int y = size-1; y>=size-k; y--){
            
            if(arr[y] == false){
                
                check = false;
                
                break;
                
            }
            
        }
        
        cout<<"CASE #"<<count1<<": ";
        
        
        
        if(check){
            
            cout<<mini<<endl;
            
        }
        
        else{
            
            cout<<"IMPOSSIBLE"<<endl;
            
        }
        
    }
    
}


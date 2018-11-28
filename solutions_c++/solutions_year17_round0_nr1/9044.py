//

//  main.cpp

//  coding is back

//

//  Created by VERDU SANJAY on 23/01/17.

//  Copyright © 2017 VERDU SANJAY. All rights reserved.

//



#include <iostream>
#include<string.h>
#include<map>
#include<math.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<stack>
#include<time.h>
#include<fstream>
#define mod 1000000007

using namespace std;

typedef long long ll;

using namespace std;

map<string,string> mp;

ll mark[100003] = {0};

int main(){
   
   freopen("A-large.in","r",stdin);
   
   freopen("output.txt","w",stdout);
    
    ll t,i,j;
    
    ll b = 1;
    
    string s;
    
    ll n;
    
    cin >> t;
    
    while(t--){
        
        memset(mark,0,sizeof(mark));
        
        cin >> s >> n;
        
        for(i = 0;i<s.size();i++){
            
            if(s[i]== '-')
                mark[i] = 0;
            else
                mark[i] = 1;
        }
        
        ll count  = 0;
        
        for(i = 0;i+n<=s.size(); i++){
            
            if(mark[i] == 0){
                
                for(j = i;j<i+n;j++)
                    mark[j] = mark[j] ^ 1;
                count++;
            }
        }
        
        ll count1 = 0;
        
        for(i = 0;i<s.size();i++)
            if(mark[i]==0)
                count1++;
        
        cout << "Case #" << b << ": ";
        if(count1>0)
            cout << "IMPOSSIBLE"<< endl;
        else
            cout << count<< endl;
            
        b++;
    }
    
    return 0;
    
    
    
    
}

//
//  main.cpp
//  codejam
//
//  Created by Victor on 2017/3/4.
//  Copyright © 2017年 Victor. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <unordered_map>
#include <fstream>
#include <ctime>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int main(int argc, const char * argv[]) {
    ifstream fin;
    ofstream fout;
    fin.open("B-large.txt");
    fout.open("out.txt");
    
    

    int T;
    fin>>T;
    
    for(int q=1;q<=T;q++)
    {
        long long ansnum;
        string ans="";
        long long N;
        fin>>N;
        
        string s=to_string(N);
        int n=s.size();
        string m="";
        
        for(int i=0;i<n;i++)
        {
            m+="1";
        }
        long long mnum=stoll(m);
        if(N<mnum)
        {
            for(int i=1;i<n;i++)
            {
                ans+="9";
            }
            ansnum=stoll(ans);
            //cout<<ansnum<<endl;
        }
        else
        {
            ans=s;
            for(int i=0;i<n-1;i++)
            {
                if(s[i]<=s[i+1])continue;
                else
                {
                    while(ans[i]==ans[i-1] && i>0)
                    {
                        i--;
                    }
                    ans[i]--;
                    for(int j=i+1;j<n;j++)
                    {
                        ans[j]='9';
                    }
                    break;
                }
            }
        }
        ansnum=stoll(ans);
        fout<<"Case #"<<q<<": "<<ansnum<<endl;
    }
    
    
    
  
    
    
    fout.close();
    fin.close();
    return 0;
}

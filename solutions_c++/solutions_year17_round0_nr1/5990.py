//
//  main.cpp
//  jam2
//
//  Created by Victor on 2017/3/5.
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
    fin.open("A-large.txt");
    fout.open("out.txt");
    
    
    
    int T;
    fin>>T;
    
    for(int q=1;q<=T;q++)
    {
        string s;
        fin>>s;
        int k;
        fin>>k;
        
        int n=s.size();
        int num=0;
        int ans=0;
        for(int i=0;i<n;i++)
        {
            if(s[i]=='+') num++;
        }
        if(num==n) ans=0;
        else
        {
            for(int i=0;i<=n-k;i++)
            {
                if(s[i]=='+') continue;
                else
                {
                    for(int j=i;j<i+k;j++)
                    {
                        if(s[j]=='+')
                        {
                            s[j]='-';
                            num--;
                        }
                        else
                        {
                            s[j]='+';
                            num++;
                        }
                    }
                    ans++;
                    if(num==n) break;
                }
            }
            
        }
        if(num==n) fout<<"Case #"<<q<<": "<<ans<<endl;
        else fout<<"Case #"<<q<<": "<<"IMPOSSIBLE"<<endl;

    }

    
    fout.close();
    fin.close();
    return 0;
}

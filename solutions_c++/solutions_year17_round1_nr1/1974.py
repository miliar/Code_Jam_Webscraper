//
//  main.cpp
//  1
//
//  Created by Ken-Hao Liu on 15/04/2017.
//  Copyright © 2017 Ken-Hao Liu. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution{
public:
    vector<string>solve(vector<string>&mat){
        vector<string>result;
        int m=mat.size(),n=mat[0].size();
        string prev;
        for(int i=0;i<m;i++){
            int pos=0;
            string s;
            for(int j=0;j<n;j++){
                while(j<n&&mat[i][j]=='?')j++;
                if(j==n)continue;
                char c=mat[i][j];
                j++;
                while(j<n&&mat[i][j]=='?')j++;
                s+=string(j-pos,c);
                pos=j,j--;
//                printf("s %s\n",s.c_str());
            }
            if(!s.empty()){
                while(i>=result.size())result.push_back(s);
                prev=s;
            }
            if(i==m-1)while(result.size()<m)result.push_back(prev);
        }
        return result;
    }
};
int main(int argc, const char * argv[]) {
    int t,r,c;
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>r>>c;
        Solution sol;
        vector<string>v(r);
        for(int j=0;j<r;j++){
            cin>>v[j];
        }
        vector<string>result=sol.solve(v);
        printf("Case #%d:\n",i+1);
        for(auto s:result)printf("%s\n",s.c_str());
    }
    return 0;
}

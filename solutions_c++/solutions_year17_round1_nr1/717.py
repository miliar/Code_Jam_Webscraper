//
//  main.cpp
//  test1
//
//  Created by Lingsong Zeng on 3/2/17.
//  Copyright © 2017 Lingsong Zeng. All rights reserved.
//




#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;
string s[30];
vector<pair<int,int> >a;
int main(){
    int t,cas=0;
    cin>>t;
    while(t--){
        printf("Case #%d:\n",++cas);
        int n,m;
        cin>>n>>m;
        for(int i=0;i<n;i++)
            cin>>s[i];
        a.clear();
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            if(s[i][j]!='?')
                a.push_back(make_pair(i,j));
        for(int i=0;i<a.size();i++){
            int x=a[i].first,y=a[i].second;
            int left=y,right=y,j=y-1;
            for(j=y-1;j>=0;j--)
            {
                if(s[x][j]!='?')
                    break;
            }
            left=j+1;
            for(j=y+1;j<m;j++)
            {
                if(s[x][j]!='?')
                    break;
            }
            right=j-1;
            int up=x,down=x;
            for(j=x-1;j>=0;j--){
                bool flag=true;
                for(int k=left;k<=right;k++)
                    if(s[j][k]!='?')
                        flag=false;
                if(!flag)
                    break;
            }
            up=j+1;
            for(j=x+1;j<n;j++){
                bool flag=true;
                for(int k=left;k<=right;k++)
                    if(s[j][k]!='?')
                        flag=false;
                if(!flag)
                    break;
            }
            down=j-1;
            //cout<<left<<" "<<right<<endl;
            for(int j=up;j<=down;j++)
                for(int k=left;k<=right;k++)
                    s[j][k]=s[x][y];
        }
        for(int i=0;i<n;i++)
            cout<<s[i]<<endl;
    }
}
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string str;
int ans[20];

bool solve(int ind , int prev , bool all);
int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int t;
    cin >> t;
    for(int i=1;i<=t;i++){
        cin >> str;
        if(solve(0,0,false)){
            cout << "Case #" << i << ": ";
            bool leading = true;
            for(int j=0;j<str.length();j++){
                if(leading && ans[j]==0)continue;
                leading = false;
                cout << ans[j];
            }
            if(i!=t)cout << "\n";
        }
    }
    return 0;
}


bool solve(int ind , int prev , bool all){
    if(ind == str.length())return true;
    int maxx = str[ind] - '0';
    if(all){
        for(int num = 9 ;num>=0;num--){
            if(num >= prev){
                if(solve(ind+1,num,true)){
                    ans[ind] = num;
                    return true;
                }
            }
        }
    }
    else{
        for(int num = maxx ;num>=0;num--){
            all = (num<maxx);
            if(num >= prev){
                if(solve(ind+1,num,all)){
                    ans[ind] = num;
                    return true;
                }
            }
        }
    }
    return false;
}

#pragma comment(linker, ”/STACK:38777216“
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <stack>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <time.h>
#include <map>
#include <set>

using namespace std;

const int N = 1005;
const int inf = 1000 * 1000 * 1000;
const int mod = 1000 * 1000 * 1000 + 7;

int n,q,k;
string s,answ;
int a[1005];

int main(){
    //freopen("B-small-attempt0.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>q;
    for(int i=1;i<=q;i++){
        cin>>s;
        answ = "";
        for(int i=0;i<(int)s.size();i++){
            char x = s[i];
            int it = i;
            while(s[it] == x){
                ++it;
                if(it == (int)s.size())break;
            }
            if(it == (int)s.size()){
                answ = s;
                break;
            }
            else{
                if(x - '0' > s[it] - '0'){
                    for(int j=0;j<i;j++)answ += s[j];
                    if(s[i] == '1'){
                        for(int j=1;j<(int)s.size();j++)answ += '9';
                    }
                    else{
                        answ += s[i] - 1;
                        for(int j=i+1;j<(int)s.size();j++)answ += '9';
                    }
                    break;
                }
            }
        }
        cout<<"Case #"<<i<<": "<<answ<<endl;
    }
    return 0;
}

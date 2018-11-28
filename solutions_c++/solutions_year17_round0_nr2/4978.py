#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <memory.h>
#include <cassert>
#include <complex>

using namespace std;
int dx[8]={1,-1,0,0,1,-1,1,-1};
int dy[8]={0,0,-1,1,1,-1,-1,1};
string s;
int t;
void ed(int idx){
    if(s[idx]=='0'||s[idx]=='1'){
        if(idx==0){
            s[idx]='0';
            return ;
        }
        s[idx]='9';
        ed(idx-1);
        return ;
    }

    s[idx]--;
    if(idx&&s[idx]<s[idx-1]){
        s[idx]='9';
        ed(idx-1);
    }
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        printf("Case #%d: ",tt);
        cin>>s;
        int sz=(int)s.size();
        int idx=-1;
        for(int i=0;i<sz-1;i++){
            if(s[i]>s[i+1]){
                idx=i;
                break;
            }
        }
        if(idx==-1){
            cout<<s<<endl;
        }else{
            for(int i=idx+1;i<sz;i++){
                s[i]='9';
            }
            bool pr=0;
            ed(idx);
            for(int i=0;i<sz;i++){
                if(s[i]!='0'){pr=1;}
                if(!pr){continue;}
                cout<<s[i];
            }
            cout<<endl;
        }
    }
    return 0;
}

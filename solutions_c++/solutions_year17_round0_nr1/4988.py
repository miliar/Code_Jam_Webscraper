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
int a[1003];
int t,k,ans;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        printf("Case #%d: ",tt);
        cin>>s>>k;
        int sz=(int)s.size();
        int cnt=0;
        int ans=0;
        bool ok=1;
        memset(a,0,sizeof(a));
        for(int i=0;i<sz;i++){
            if(a[i]&1){
                if(s[i]=='+'){s[i]='-';}else{
                s[i]='+';
                }
            }
            a[i+1]+=a[i];

            if((i+k)-1 >=sz){continue;}


            if(s[i]=='-'){
                ans++;
            s[i]='+';
                a[i+k]--;
                a[i]++;
                a[i+1]++;
            }
        }
        memset(a,0,sizeof(a));
        for(int i=sz-1;i>-1;i--){
            if(a[i]&1){
                if(s[i]=='+'){s[i]='-';}else{
                    s[i]='+';
                }
            }
            if(i){
            a[i-1]+=a[i];
            }
            if((i-k)-1 <0){continue;}
            if(s[i]=='-'){
                ans++;
                s[i]='+';
                a[i]++;
                if(i){
                    a[i-1]++;
                }
                if(i>=k){
                    a[i-k]--;
                }


            }
        }
        for(int i=0;i<sz;i++){
            if(s[i]=='-'){ok=0;}
        }
        if(!ok){
            cout<<"IMPOSSIBLE"<<endl;
        }else{
            cout<<ans<<endl;
        }
    }
    return 0;
}

#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<map>
#include<queue>
#include<cstring>
#include<stack>
#include<set>
#include<vector>
#include<iostream>
#include<fstream>
#include<math.h>
#include<cmath>
#define mp(x,y) make_pair(x,y)
#define INF 1e18
#define EPS 1e-5
using namespace std;
int const sz=1e5+2;
int t;

int main(){
    freopen("B-large.in","r",stdin);
   freopen("out.in","w",stdout);
scanf("%d",&t);
int cnt=1;

while(t--){
    string inp="";
     string ans="";

    cin>>inp;
    for(int i=0;i<inp.size()-1;i++){
        if(inp[i]>inp[i+1]){
            int k=i;
            if(inp[i]>'0')
            inp[i]-=1;
            while(inp[k]<inp[k-1]&&k>0){
                    inp[k-1]-=1;
                    inp[k]='9';
                    k--;

            }

                for(int j=i+1;j<inp.size();j++)
                    inp[j]='9';

            break;
        }
    }
    bool flag=true;
    for(int i=0;i<inp.size();i++){
            if(inp[i]!='0')
                flag =false;
            if(flag)
                continue;
            ans+=inp[i];
    }

printf("Case #%d: %s\n",cnt++,ans.c_str());

}
return 0;
}

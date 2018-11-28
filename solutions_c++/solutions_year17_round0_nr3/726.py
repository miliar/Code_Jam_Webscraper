#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
#include <map>
using namespace std;
typedef long long ll;

ll n,k;

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T,Case=1;
    
    for(scanf("%d",&T);Case<=T;Case++){
        printf("Case #%d: ",Case);
        
        scanf("%I64d%I64d",&n,&k);
        map<ll,ll> cur,nxt;
        nxt[n]=1;
        ll person=0,last_person=0;
        while(person<k){
           cur=nxt;
           nxt.clear();
           last_person=person;
           
           for(auto it=cur.begin();it!=cur.end();++it){
               ll val=it->first -1;
               ll cnt=it->second;
               if(val/2>0)nxt[val/2]+=cnt;
               if(val-val/2>0)nxt[val-val/2]+=cnt;
               person+=cnt;
           }
        }
        k-=last_person;
        //printf("++%I64d %I64d\n",last_person,person);
        for(auto it=cur.rbegin();it!=cur.rend();++it){
            //printf("++%I64d %I64d\n",it->first,it->second);
            if(k>it->second){
                k-=it->second;
            }else{
                ll cnt=it->first -1 ;
                printf("%I64d %I64d\n",cnt-cnt/2,cnt/2);
                break;
            }
        }
    }
    return 0;
}


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
int t,n,k,a[1000006];
bool comp(pair<int,pair<int,int> > a, pair<int,pair<int,int> > b){
    if(a.second.first!=b.second.first){
        return a. second.first>b.second.first;
    }
    if(a.second.second!=b.second.second){
        return a.second.second>b.second.second;
    }
    return a.first<b.first;}
int main(){
    freopen("C-small-2-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        printf("Case #%d: ",tt);
        scanf("%d %d",&n,&k);
        memset(a,-1,sizeof(a));
        vector<int> all;
        a[0]=a[n+1]=0;
        all.push_back(0);
        all.push_back(n+1);
        //k++;
        int cur=1;
        bool done=0;
        int idx=0;
        int l=100000000;
        int r=100000000;
        while(!done){
            vector<int> v;
            for(int i=0;i<all.size()-1;i++){
                int p=all[i];
                int nxt=all[i+1];
                if(p+1==nxt){continue;}
                idx=(p+nxt)/2;
                //cout<<p<<" "<<nxt<<" "<<idx<<endl;
                v.push_back(idx);
            }
            for(int i=0;i<v.size();i++){
                all.push_back(v[i]);
            }
            sort(all.begin(),all.end());
            vector<pair<int,pair<int,int> > >vv;
            for(int i=0;i<all.size();i++){
              //  cout<<all[i]<<" ";
                int mm=all[i];
                if(a[mm]==-1){
                    l=mm-all[i-1];
                    r=all[i+1]-mm;
                    if(l>r){swap(l,r);}
                    vv.push_back(make_pair(mm,make_pair(l,r)));
                }
            }
           // cout<<endl;
            sort(vv.begin(),vv.end(),comp);
            for(int i=0;i<vv.size();i++){
                //cout<<vv[i].first<<" ";
                a[vv[i].first]=cur++;
                if(a[vv[i].first]==k){
                    cout<<vv[i].second.second-1<<" "<<vv[i].second.first-1<<endl;
                    done=1;
                    break;
                }
            }
            //cout<<endl;
        }
    }
    return 0;
}

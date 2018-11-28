#include <math.h>
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <cstring>
#include <algorithm>
#include <stack>
#include <queue>
#include <cstring>
#include <sstream>
#include <stdlib.h>
#include <stdio.h>
#include <cctype>
#define inf 2000000000
#define MOD 1000000007
#define MAX 1000006
#define M   10000007
typedef long long ll;
using namespace std;
string s;
int n,k,a[MAX];
bool cmp(pair<int,pair<int,int> > a, pair<int,pair<int,int> > b){
if(a.second.first!=b.second.first){
return a. second.first>b.second.first;
    }
if(a.second.second!=b.second.second){
return a.second.second>b.second.second;
    }
    return a.first<b.first;
    }
int main(){
freopen("C-small-2-attempt1.in","r",stdin);
freopen("output.in","w",stdout);
int TC,tc=0;
scanf("%d",&TC);
while(TC--){
tc++;
scanf("%d %d",&n,&k);
printf("Case #%d: ",tc);
memset(a,-1,sizeof(a));
vector<int> all;
a[0]=a[n+1]=0;
all.push_back(0);
all.push_back(n+1);
int cur=1;
bool ans=0;
int idx=0;
int l=1e8;
int r=1e8;
while(!ans){
vector<int> v;
for(int i=0; i<all.size()-1; i++){
int p=all[i];
int nxt=all[i+1];
if(p+1==nxt){continue;}
idx=(p+nxt)/2;
v.push_back(idx);
}
for(int i=0; i<v.size(); i++){all.push_back(v[i]);}
sort(all.begin(),all.end());
vector<pair<int,pair<int,int> > >vv;
for(int i=0;i<all.size();i++){
int mm=all[i];
if(a[mm]==-1){
l=mm-all[i-1];
r=all[i+1]-mm;
if(l>r){swap(l,r);}
vv.push_back(make_pair(mm,make_pair(l,r)));
}
}
sort(vv.begin(),vv.end(),cmp);
 for(int i=0; i<vv.size(); i++){
a[vv[i].first]=cur++;
if(a[vv[i].first]==k){
printf("%d %d\n",vv[i].second.second-1,vv[i].second.first-1);
ans=1;
break;
}}
}}
return 0;
  }

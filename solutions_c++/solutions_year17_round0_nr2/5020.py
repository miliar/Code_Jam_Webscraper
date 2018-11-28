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
#define MAX 100005
#define M   10000007
typedef long long ll;
using namespace std;
int n,k;
string s;
int main(){
int TC,tc=0;
freopen("B-large.in","r",stdin);
freopen("output.in","w",stdout);
scanf("%d",&TC);
while(TC--){
 tc++;
  string s;
  cin>>s;
  int n=s.size();
  int a[n];
  for(int i=0; i<n; i++){
    a[i]=s[i]-'0';
  }int idx=-1;
 for(int i=0; i<n-1; i++){
    if(a[i]>a[i+1]){
     idx=i; break;
     }
 }
if(idx==-1){printf("Case #%d: ",tc);
cout<<s<<endl; continue;}
for(int i=n-1; i>idx; i--)a[i]=9;
if(a[idx]==0){
int j=idx;
while(a[j]==0&&j>=0){a[j]=9;j--;}
a[j]--;
}
else {
int j=idx;
while(a[j-1]>=a[j]&&j>0){a[j]=9;j--;}
a[j]--;
}
int i=0;
for(i=0; i<n; i++){
if(a[i]!=0){break;}
}printf("Case #%d: ",tc);
for(i; i<n; i++)printf("%d",a[i]);
printf("\n");
}
  return 0;
}

#include <iostream>
#include <stdio.h>
#include<list>
#include<string.h>
#include <queue>
#include <algorithm>
#define MAX 2005
using namespace std;
int n;
int TC;
double d;
double s[MAX];
double p[MAX];
double dif[MAX];
int main(){
    int tt=0;
    freopen("A-large.in","r",stdin);
    freopen("out.in","w",stdout);
    scanf("%d",&TC);
    while(TC--){tt++;
cin>>d>>n;
for(int i=0; i<n; i++){
cin>>p[i]>>s[i];
}
for(int i=0; i<n; i++){
 double dd=d-p[i];
 dif[i]=dd/s[i];
 }
 sort(dif,dif+n);
 reverse(dif,dif+n);
double ans=d/dif[0];
printf("Case #%d: %.6lf",tt,ans);
if(TC)printf("\n");
    }
}


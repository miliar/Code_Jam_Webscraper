#include<bits/stdc++.h>
using namespace std;


long long int a[100001];
double pos[10001],sp[10001];
int main(){
       freopen("C:\\Users\\Chandan\\Desktop\\input.txt", "r", stdin);
freopen("C:\\Users\\Chandan\\Desktop\\gcj.txt", "w", stdout);
long long N;
double D,x,y;
int t;
cin>>t;
int lc=1;
while(t--){
        cout<<"Case #"<<lc<<": ";
        lc++;
cin>>D>>N;
double min_time =0;
int ps=0;
for(int i=0;i<N;i++){
cin>>x>>y;
pos[i]=x;
sp[i]=y;
if (min_time<((D-x)/y)){
min_time=(D-x)/y;
ps=i;
}
}
//<<ps<<endl;
//cout<<sp[ps]<<endl;

double ans=(D/(D-pos[ps]))*sp[ps];
printf("%.7lf\n",ans);
}
return 0;
}

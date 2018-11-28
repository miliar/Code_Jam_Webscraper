#include<bits/stdc++.h>
#define ppi pair<int,int>
using namespace std;
bool com(ppi p1,ppi p2){
return p1.first<p2.first;
}
int main(){
int t,x=1;
cin>>t;
while(t--){
        int dis,n;
    cin>>dis>>n;
    vector<ppi>  v;
    float mt=-1;
    for(int i=0;i<n;++i){
        int d,s;
        cin>>d>>s;
        mt=max(mt,float(dis-d)/float(s));
    }
    cout<<"Case #"<<x++<<": ";
    printf("%.6f\n",float(dis)/mt);
}
return 0;
}


#include<bits/stdc++.h>
using namespace std;
int main(){
int t;
cin>>t;
for(int j=1;j<=t;j++){
int N,R,O,Y,G,bB,V;
cin>>N>>R>>O>>Y>>G>>bB>>V;
vector<pair<int,string>> v;
v.push_back(make_pair(R,"R"));
v.push_back(make_pair(Y,"Y"));v.push_back(make_pair(bB,"B"));
sort(v.begin(),v.end());
int c=v[0].first,b=v[1].first,a=v[2].first;
string C=v[0].second,B=v[1].second,A=v[2].second;
if(a>(b+c)) {
cout<<"CASE #"<<j<<": IMPOSSIBLE\n";
continue;
}
int reg=c;
int spare=(b-c);
int extra=a-reg-spare;
string s="";
for(int i=0;i<reg;i++)
{
s=s+A;
s=s+B;
if(extra>0) s=s+A+C,extra--;
else s=s+C;
}
for(int i=0;i<spare;i++){
s=s+A;
s=s+B;
}
cout<<"CASE #"<<j<<": "<<s<<"\n";

}


}
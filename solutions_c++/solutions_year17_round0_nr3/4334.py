#include<bits/stdc++.h>
using namespace std;
typedef pair<long long int,long long int> ii;
int main() {
// ios_base::sync_with_stdio(false);
// cin.tie(NULL);
int t;
cin>>t;
for(int f=1;f<=t;f++){
long long int n,k;
cin>>n>>k;
set<ii> s;
int ANS=0;
s.insert(ii(n,1));
int cnt=0;


while(s.size()!=0){

auto JK=s.end();
JK--;
ii A=*JK;
s.erase(A);
long long int N=A.first;
long long int L=A.second;
k-=L;
if(k<=0) {ANS=N;break;}
int k1=(N-1)/2;

bool b=0;
if(k1!=0){
for(auto it=s.begin();it!=s.end();it++){
ii temp=*it;
if(temp.first==k1) {
	s.erase(it);
	s.insert(ii(temp.first,temp.second+L)),b=1;
}
}
if(!b) s.insert(ii(k1,L));

}
k1=(N)/2;
b=0;
if(k1!=0){
for(auto it=s.begin();it!=s.end();it++){
ii temp=*it;
if(temp.first==k1) {

	s.erase(it);
	s.insert(ii(temp.first,temp.second+L)),b=1;
}
}
if(!b) s.insert(ii(k1,L));
}
}
ANS--;
 cout<<"Case #"<<f<<": "<<(ANS+1)/2<<" "<<(ANS)/2<<"\n";

}

}
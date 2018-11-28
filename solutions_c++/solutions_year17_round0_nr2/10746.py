#include<bits/stdc++.h>
#define pi 3.14159265359
#define oo INT_MAX
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
int main()
{
//#ifndef ONLINE_JUDGE
freopen("B-small-attempt0.in","r",stdin);
freopen("o.txt","w",stdout);
//#endif
ll tc,k,c=0,hc=0,bc=0;
cin>>tc;
string s,t;
for (int i=0;i<tc;i++){
cin>>k;
for(ll j=k;j>=0;j--){
	s=to_string(j);
	t=s;
	sort(t.begin(),t.end());
	if(s==t){
		cout<<"Case #"<<i+1<<": "<<s<<"\n";
	break;
	}
}
}
}

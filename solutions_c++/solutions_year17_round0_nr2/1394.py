#include<bits/stdc++.h>
using namespace std;
int main(){
	ifstream in("B-large.in.txt");
	ofstream out("output.txt");
	int t;
	in>>t;
	for(int i=1;i<=t;++i){
		long long n,d,ind=-1;
		in>>n;
		string s=to_string(n),ans;
		d=s.size();
		bool good=true;
		for(int j=0;j!=d-1;++j){
			if(s[j]>s[j+1]){
				good=false;
				break;
			}
			if(s[j]<s[j+1])
				ind=j+1;
		}
		if(good)
			ans=s;
		else if(ind!=-1){
			for(int j=0;j!=ind;++j)
				ans+=s[j];
			ans+=s[ind]-1;
			ans+=string(d-ind-1,'9');
		}
		else{
			if(s[0]!='1')
				ans+=s[0]-1;
			ans+=string(d-1,'9');
		}
		out<<"Case #"<<i<<": "<<ans<<endl;
	}
}
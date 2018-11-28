// Sourav Verma   IPG_2013108   CodeJam 2017

#include <bits/stdc++.h>
using namespace std;

bool istidy(int st,int e, string& s){
	/*bool flag=false;
	long long nd=n%10;
	while(n){
		long long d=n%10;
		if(d>nd) {
			flag=false;
			return flag;
		}
		n/=10;
	}
	flag=true; 
	return flag;*/
	
	int i=st;
	while(i<e && s[i]=='1') i++;
 	if(s[i]=='0')	{
 		for(int j=st;j<=e;j++) s[j]='9';
 		return true;
 	}
 	return false;
}

int main(){
	int t; cin>>t;
	for(int ts=1;ts<=t;ts++){
		string s; cin>>s; string s1="";  //int k; cin>>k;
		//long long n; cin>>n;
		int l=s.size()-1; 
		cout<<"Case #"<<ts<<": ";
		if(s[0]=='1' && istidy(0,l,s)) {
			s[l]='\0';
			cout<<s<<"\n";
			continue;
		}
		int i=0;
		while(i<l) {
			if(s[i]>s[i+1]) {
				s[i]-=1;
				s1+=s[i];
				for(int j=i+1;j<=l;j++)	s[j]='9';
				continue;
			}
			else if(s[i]=='1' && istidy(i,l,s)) continue;
			i++;
		}
		cout<<s<<"\n";
		//cout<<"Case #"<<ts<<": "<<n<<"\n";
	}
	return 0;
}

#pragma GCC optimize "Ofast,omit-frame-pointer,inline"
#include <bits/stdc++.h>
using namespace std;

string s,ans;

void solve(){
	ans="";
	int i,inversion = -1;	//finds the first inersion.. this is the only inversion we need to care about
	for(i=0;i<s.length()-1;i++){
		if(s[i]>s[i+1]){
			inversion = i;
			break;
		}
	}
	if(inversion == -1){	//there is no inversion
		ans = s;
		return;
	}

	if(s[inversion] == '1')
	{
		for(i=0;i<s.length()-1;i++)
			ans += "9";
		return;
	}

	for(i=0;i<inversion;i++){
		ans += s[i];
	}
	ans.push_back(s[i]-1);
	for(i=inversion+1;i<s.length();i++)
	{
		ans+="9";
	}
}

bool doBrute(){
	stringstream ss;
	ss<<s;
	long long x;
	ss>>x;
	bool hasInversion;
	do{
		hasInversion = false;
		long long t = x;
		while(t>=10){
			if((t/10)%10 > t%10){
				hasInversion = true;
				break;
			}
			t/=10;
		}
		if(hasInversion){
			x--;
		}
	}while(hasInversion);
	stringstream ss2;
	ss2<<x;
	ss2>>ans;
}

int main(){
    ios::sync_with_stdio(false);
    freopen("gcj2large.in","r",stdin);
    freopen("gcj2largeout.txt","w",stdout);
    int t,c=1;
    cin>>t;
    while(t--){
    	cin>>s;
    	cout<<"Case #"<<c++<<": ";
    	for(int i=0;i<25;i++){
    		solve();
    		s = ans;
	    }
    	//doBrute();
    	cout<<ans<<endl;
    }
	return 0;
}
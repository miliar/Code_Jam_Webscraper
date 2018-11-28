#include <bits/stdc++.h>
using namespace std;
int T,K;
string S;
int tell(int x,int y){
	printf("Case #%d: ",x);
//	cout<<"Case #"<<x<<": ";
	if(y>=0)
		cout<<y<<endl;
	else
		cout<<"IMPOSSIBLE"<<endl;
}
int main(){
	cin>>T;
	for(int z=1;z<=T;z++){
		cin>>S>>K;
		int ans=0;
		int p=0;
		bool possible=true;
		for(p=0;p<=S.length()-K;p++){
			if(S[p]=='+')
				continue;
			ans++;	
			for(int z=p;z<p+K;z++){
				if(S[z]=='+')
					S[z]='-';
				else
					S[z]='+';
			}
//			cout<<"p="<<p<<" S="<<S<<" ans="<<ans<<endl;
		}
		//cout<<"now p="<<p<<"flipped = "<<flipped<<endl;
		for(;p<S.length();p++)
			if(S[p]=='-'){
				possible=false;
				break;
			}
		if(possible)
			tell(z,ans);
		else
			tell(z,-1);		

			
	}		
	return 0;	
}

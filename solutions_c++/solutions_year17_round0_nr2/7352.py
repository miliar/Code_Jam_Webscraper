#include <bits/stdc++.h>

using namespace std;

int main(void){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	cin>>test;
	for(int t=1;t<=test;t++){
		long long num;
		cin>>num;
		string s="";
		while(num){
			s.push_back(num%10+'0');
			num/=10;
		}
		reverse(s.begin(),s.end());
		string ans = "";
		for(int i=0;i<s.size();i++){
			if(i<s.size()-1 && s[i]>s[i+1]){
				int nxt=i+1;
				while(i>0 && (s[i]<='1' || s[i-1]==s[i])){
					nxt = i;
					i--;
				}
				ans = "";
				for(int j=0;j<i;j++){
					ans.push_back(s[j]);
					
				}
				
				if(i!=0 || s[i]>'1'){
					ans.push_back(s[i]-1);
				}
				while(nxt<s.size())ans.push_back('9'),nxt++;
				break;
			}else ans.push_back(s[i]);
		}
		//~ if(ans.size()==0)ans = s;
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}

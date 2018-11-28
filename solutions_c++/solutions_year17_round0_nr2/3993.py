#include <bits/stdc++.h>
using namespace std;

int t,idx,can,isz;
string s;

int main(){
	freopen("B-small-attempt4.in","r",stdin);
	freopen("Q2.out","w",stdout);
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		cin>>s;
		isz=0;
		int n=s.length();
		for(int i=0;i<n;i++){
			can=1;
			for(int j=i;j<n;j++) if(s[i]>s[j]) can=0;
			if(can==0&&s[i]>=s[i+1]){
				s[i]--;
				idx=i+1;
				break;
			}
			else if(can==0){
				s[i+1]--;
				idx=i+2;
				break;
			}
		}
		if(can==0) for(int i=idx;i<n;i++) s[i]='9';
		if(s[0]=='0') isz=1;
		printf("Case #%d: ",tc);
		if(isz){
			for(int i=1;i<n;i++) cout<<s[i];
			cout<<endl;
		}
		else cout<<s<<endl;
	}
}

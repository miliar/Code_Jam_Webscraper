#include "bits/stdc++.h"

using namespace std;
int dp[12345];
bool chk(unsigned long long num){
	int l = num % 10, r = num%10;
	num/=10;
	if(num==0)
			return true;
	while(num){
		r = num%10;
		if(r > l)
			return false;
		l = r;
		num/=10;
	}
	return true;
}
void gen(){
	for(int i=1;i<12345;i++){
		if(chk(i)){
			dp[i] = i;
		}
		else
			dp[i] = dp[i-1];
		cout<<"Case #"<<i<<": "<<dp[i]<<endl;
	}

}
int main(){

	int t,i=1;
	cin>>t;
	while(t--){
	//	unsigned long long n;
		string n;
		cin>>n;
		cout<<"Case #"<<i++<<": ";
		int len=0,z=0,i;
		for(i=1;i<n.length();i++){
			if(n[i] < n[i-1])
				break;
				
		}
		if(i==n.length())
			cout<<n<<endl;
		else{
			i--;
			if(n[i]=='1'){
				n[i]='0';
				z++;
			}
			else if(n[i]=='0'){
				z++;
			}else
				n[i] = n[i]-1;
			while(i-1 >=0 && n[i] < n[i-1]){
				if(n[i-1]!='0')
					n[i-1] = n[i-1]-1;
				else
					z++;
				i--;
			}
			if( (i==0 && n[i]!='0') || i > 0){
			int lenwa = i+1;
			cout<<n.substr(0,lenwa);}
			for(int j=i+1;j<n.length();j++)
				cout<<9;
				
			cout<<endl;
		}
	
	}


	return 0;
}


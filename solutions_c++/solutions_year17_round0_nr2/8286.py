#include<bits/stdc++.h>
using namespace std;
bool f(long long n){
	while(n!=0){
		long long aux=n%10;
		n/=10;
		if(n%10>aux)return false;
	}
	return true;
}
long long fb(long long n){
	while(true){
		if(f(n)){
			return n;
		}
		n--;
	}
}
int main(){
	long long t,k;
	cin>>t;
	for(int cs=1;cs<=t;cs++){
		string s;
		cin>>k;
		if(k<10){
			cout<<"Case #"<<cs<<": "<<k<<endl;
			continue;
		}
		//cout<<fb(k)<<endl;
		//cout<<fb(k)<<endl;
		long long num;
		//do{
			stringstream ss;
			ss<<k;
			ss>>s;
			for(int i=0;i<s.size()-1;i++){
				int aux=s[i]-'0';
				if(aux>s[i+1]-'0'){
					int j=i;
					bool nf=true;
					while(j>0){
						if((s[j]-'0')-(s[j-1]-'0')>0){
							nf=false;
							break;
						}
						j--;
					}
					if(nf)j=0;
					s[j]=char((s[j]-'0')-1+48);
					//cout<<s[j]<<endl;
					for(int o=j+1;o<s.size();o++){
						s[o]='9';
					}
				}
			}
			//cout<<s<<endl;
			istringstream pp(s);
			pp >>num;
			//cout<<num<<endl;
		//}while(!f(num));
		cout<<"Case #"<<cs<<": "<<num<<endl;
	}
}
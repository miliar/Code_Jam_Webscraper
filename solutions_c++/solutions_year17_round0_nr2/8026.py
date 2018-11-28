#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
string func(string s){
	bool flag = true;
	int i;
	int n = s.size();
	if(n==1)
		return s;
	for(i=0;i<n-1;i++){
		if(s[i]>s[i+1]){
			flag = false;
			s[i]=s[i]-1;
			break;
		}
	}
	if(flag)
		return s;
	else
		for(i=i+1;i<n;i++){
			s[i]= '9';
		}
	return func(s);
}
int main(){
	long long int t,n,cased=1;
	string s;
	cin>>t;
	while(t--){
		char* pEnd;
		cin>>s;
		s = func(s);
	//	cout<<s<<endl;
		n = strtoll (s.c_str(), &pEnd, 10);
		cout<<"Case #"<<cased<<": "<<n<<endl;
		cased++;
	}
}
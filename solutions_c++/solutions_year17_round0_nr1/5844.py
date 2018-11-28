#include <bits/stdc++.h>
#include <fstream>
using namespace std;

bool yes(vector<int> a){
	int d=0;
	for(int i=0;i<a.size();i++){
		if(a[i]==0){
			d=1;
			break;
		}
	}
	if(d==0){
		return true;
	}
	return false;
}

int chk(vector<int> b){
	for(int i=0;i<b.size();i++){
		if(b[i]==0){
			return i;
		}
	}
	return b.size();
}
int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		string a;
		int k;
		cin>>a>>k;
		vector<int> b;
		for(int j=0;j<a.length();j++){
			if(a[j]=='+'){
				b.push_back(1);
			}
			else{
				b.push_back(0);
			}
		}
		if(yes(b)){
			cout<<"Case #" <<i+1<<": "<<0;
			if(i!=t-1){
				cout<<endl;
			}
			continue;
		}
		int d=0,m=0;
		for(int j=chk(b);j<=b.size()-k;){
			for(int l=j;l<j+k;l++){
					b[l]=b[l]^1;
			}
			d++;
			if(yes(b)){
				cout<<"Case #"<<i+1<<": "<<d;
				if(i!=t-1){
				cout<<endl;
			}
				m=1;
				break;
			}
			j=chk(b);
		}
		if(m==0){
			cout<<"Case #"<<i+1<<": IMPOSSIBLE";
			if(i!=t-1){
				cout<<endl;
			}
		}
	}
	return 0;
}

 

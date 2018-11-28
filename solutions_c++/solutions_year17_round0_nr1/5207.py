#include<bits/stdc++.h>

using namespace std;
int main(){
	fstream f,o;
	f.open("A-large.in");
	o.open("output.txt");
	int t;
	f >> t;
	int count=1;
	//cout<<t<<endl;
	for(int i=0; i<t; ++i){
		string s;
		f >> s;
		int k;
		f>> k;
		int imp=0;
		for(int j=0; j<s.length()-k+1; ++j){
			if(s[j]=='-'){
				++imp;
				for(int m=0; m<k; ++m){
					if(s[j+m]=='-'){
						s[j+m]='+';
					}
					else{
						s[j+m]='-';
					}
				}
			}
			//cout<<s<<endl;
		}
		int ans = 1;
		//cout<<s.length()-k;
		for(int j=0; j<k; ++j){
			if(s[s.length()-k+j] == '-')
				ans=0;
		}
		if(ans==0)
			o<<"Case #"<<count<<": IMPOSSIBLE"<<"\n";
		else
			o<<"Case #"<<count<<": "<<imp<<"\n";
		++count;
		cout<<count;
	}
	
}
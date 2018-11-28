#include <bits/stdc++.h>

using namespace std;

#define INTMAX 0x7FFFFFFF
#define INTMIN -0x80000000
#define LONGMAX 0x7FFFFFFFFFFFFFFF
#define LONGMIN -0x8000000000000000

int main(){
	int T;
	cin>>T;
	for(int tc=1; tc<=T; tc++){
		string s;
		cin>>s;
		int n = s.length();
		int k;
		cin>>k;
		int flip = 0;
		for(int i=0; i<=n-k; i++){
			if(s[i]=='-'){
				flip++;
				for(int j=i; j<i+k; j++){
					if(s[j]=='-')
						s[j] = '+';
					else	
						s[j] = '-';
				}
			}
			//cout<<s<<endl;
		}
		for(int i=0; i<n; i++){
			if(s[i]=='-'){
				flip = -1;
				break;
			}
		}
		cout<<"Case #"<<tc<<": ";
		if(flip==-1)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<flip<<endl;
	}
}
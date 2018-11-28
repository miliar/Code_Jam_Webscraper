#include <bits/stdc++.h>
using namespace std;
int main(void){
	int T;
	cin>>T;
	for(int t = 1;t<=T;t++){
		string s;
		int k;
		cin>>s>>k;
		int i=0;
		int ans = 0;
		bool possible = true;
		while(i<=(s.size()-k)){
			if(s[i] == '-'){
				ans++;
				//cout<<"ans";
				for(int j=i;j<k+i;j++){
					//cout<<"loop";
					if(s[j] == '-'){
						s[j] = '+';
					}
					else{
						s[j] = '-';
					}
				}
			}
			i++;
			//cout<<s<<endl;
		}
		i--;
		for(int j=i;j<s.size()&&possible;j++)
			if(s[j] == '-')
				possible = false;
		printf("Case #%d: ",t);
		if(possible)
			cout<<ans;
		else
			cout<<"IMPOSSIBLE";
		cout<<"\n";
	}
}
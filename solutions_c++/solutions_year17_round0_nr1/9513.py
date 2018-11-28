#include <bits/stdc++.h>
using namespace std;

int func(string s, int k){
	int i=0,count=0,len=s.size(),j;
	for(i=0;i<len;i++){

		if(s[i]=='-'){
			if(i+k>len){
				return -1;
			}
			else{
				for(j=i;j<i+k;j++){
					s[j]=(s[j]=='-' ?'+':'-');

				}
				count++;
			}
		}

	}
	return count;
}
int main(){
	int tc, m, i=0;
    string temp1,temp2;
	cin>>tc;
	while(i<tc){
		int k;
		cin>>temp1>>temp2;
		string str=temp1;
		stringstream convert(temp2);
		convert>>k;
		int ans=func(str, k);
		if(ans<0) cout<<"Case #"<<i+1<<": IMPOSSIBLE\n";
		else cout<<"Case #"<<i+1<<": "<<ans<<endl;
		i++;
	}
}

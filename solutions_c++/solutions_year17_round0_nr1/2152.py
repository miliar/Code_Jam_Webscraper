#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int z=1;z<=t;z++){
		string s;
		int k,cnt=0;
		cin >> s;
		cin >> k;
		bool ok=true;
		int len=s.length();
		for(int i=0;i<len;i++){
			if(s[i]=='-'){
				if(i+k>len){
					ok=false;
					break;
				}
				else{
					cnt++;
					for(int j=i;j<i+k;j++)
						if(s[j]=='-')
							s[j]='+';
						else
							s[j]='-';
				}
			}

		}
		if(!ok){
			printf("Case #%d: IMPOSSIBLE\n",z);
			continue;
		}
		for(int i=0;i<len;i++)
			if(s[i]=='-')
				ok=false;
		if(ok)
			printf("Case #%d: %d\n",z,cnt);
		else
			printf("Case #%d: IMPOSSIBLE\n",z);
	}

}
#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int testCases;
	cin>>testCases;
	for (int tc=1; tc<=testCases; tc++)	{
		bool tidy = false, found = false;
		string num;
		cin>>num;
		if(num.length()==1){
			tidy = true;
		}
		while(!tidy){
			tidy = true;
			found = false;
			for(int cnt1=0; cnt1<(num.length()-1); cnt1++){
				if(found){
					num[cnt1] = '9';
				}
				else{
					if((num[cnt1]-'0')>(num[cnt1+1]-'0')){
						tidy = false;
						found = true;
						num[cnt1] = num[cnt1] - '1' + '0';
					}
				}
			}
			if(found){
				num[num.length()-1] = '9';
			}
			if(num[0]=='0'){
				num = num.substr(1,num.length()-1);
			}
		}
		cout<<"Case #"<<tc<<": "<<num<<endl;
	}
	return 0;
}
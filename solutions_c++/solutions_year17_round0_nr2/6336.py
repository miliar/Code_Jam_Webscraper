#include <bits/stdc++.h>
using namespace std;

int main(){
	int i,j,k,l,n,m,t, test_case = 0;
	scanf("%d",&t);
	string num, ans = "";
	while(t--){
		test_case++;
		cin>>num;
		ans = "";
		l = num.length();
		ans.push_back(num[0]);
		int found = 0;
		for(i=1;i<l;i++){
			if(num[i-1] <= num[i]){
				ans.push_back(num[i]);
				continue;
			}
			else{
				found = 1;
				break;
			}
		}

		if(found){
			//We did not add ith character at this point
			ans = ans.substr(0, ans.length()-1);
			ans.push_back(char(num[i-1]-1));
			for(j=i-1;j>0;j--){
				if(ans[j] < ans[j-1]){
					ans = ans.substr(0, ans.length()-2);
					ans.push_back(char(num[j-1]-1));
				}
				else{
					break;
				}
			}
			while(ans.length() < l){
				ans.push_back('9');
			}
		}

		l = ans.length();
		i = 0;
		while(ans[i] == '0' && i < l){
			i++;
		}
		printf("Case #%d: ",test_case);
		while(i < l){
			printf("%c", ans[i]);
			i++;
		}
		cout<<endl;
	}
}
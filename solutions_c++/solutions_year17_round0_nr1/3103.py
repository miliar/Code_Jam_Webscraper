#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;
int main(){
	int T, k, count;
	string str;
	bool flag;

  	freopen ("A-large.in","r",stdin);
  	freopen("A-large-output", "w", stdout);

//Getting number of times
	scanf("%d", &T);

//For each input
	for(int t=1;t<=T;t++){
		count = 0;
		flag = 1;

		cin >> str >> k;

		printf("Case #%d: ", t);	

		int i;
		for(i=0; i<str.length(); i++){
			if(str[i] == '-'){
				if(i+k > str.length()){
					printf("IMPOSSIBLE");
					flag = 0;
					break;
				}
				count++;
				for(int j=i;j<i+k;j++)
					if(str[j] == '-')
						str[j] = '+';
					else
						str[j] = '-';
			}
		}
		if(flag)
			cout << count;

		printf("\n");		
	}
	
	return 0;
}
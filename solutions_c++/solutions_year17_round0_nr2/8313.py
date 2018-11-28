#include <bits/stdc++.h>

using namespace std;

char decrease(char c){
	if (c == '0')
		return '9';
	else
		return c-1;
}

int main(){
	int t;
	scanf("%d", &t);
	char num[25];
	for(int x=1; x<=t; x++){
		scanf("%s", num);
		for(int i=strlen(num)-1; i>0; i--){
			if (num[i] < num[i-1]){
				num[i] = '9';
				num[i-1]= decrease(num[i-1]);
			}
		}
		//sapu
		bool nine = false;
		for(int i=0; i<strlen(num); i++){
			if (num[i] == '9')
				nine = true;
			if (nine)
				num[i] = '9';
		}
		printf("Case #%d: ", x);
		bool ok = false;
		for(int i=0; i<strlen(num); i++){
			if (num[i] != '0')
				ok = true;
			if (ok)
				printf("%c", num[i]);
		}
		printf("\n");
	}
	return 0;
}
//173894
//169889
//596
//589
//111111111111111111111110
//99999999999999999999999
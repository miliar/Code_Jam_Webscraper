#include<iostream>
#include<cstring>

using namespace std;

int main(){
int t;
cin >> t;
for(int l = 1;l<=t;l++){
	char str[20];
	cin >> str;
	for(int i = 1;i<strlen(str);i++){
		if(str[i] < str[i-1]){
			str[i] = '9';
			str[i-1] = str[i-1] == '0'?'9':str[i-1]-1;
			int j = i-1;
			while(str[i] != '\0'){
				str[i++] = '9';
			}
			while(j>0 && str[j] < str[j-1]){
				str[j-1] = str[j-1] == '0'?'9':str[j-1]-1;
				str[j] = '9';
				j--;
			}
			break;
		}
	}
	int i = 0,j=0;
	while(str[i] == '0')i++;
	while(str[i] != '\0'){
		str[j++] = str[i++];
	}
	str[j] = '\0';
	cout << "Case #"<<l<<": "<<str << endl;
}
return 0;
}

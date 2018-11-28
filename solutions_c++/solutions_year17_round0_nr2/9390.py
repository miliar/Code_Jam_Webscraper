#include<bits/stdc++.h>
using namespace std;
char find(long unit){
	switch(unit){
		case 0:
			return '0';
			break;
		case 1:
			return '1';
			break;
		case 2:
			return '2';
			break;
		case 3:
			return '3';
			break;
		case 4:
			return '4';
			break;
		case 5:
			return '5';
			break;
		case 6:
			return '6';
			break;
		case 7:
			return '7';
			break;
		case 8:
			return '8';
			break;
		case 9:
			return '9';
			break;

	}
}
void recurseprint(char* a, int flag){
	int len = strlen(a);
	if(len==1){
		cout<<a;
		return;
	}
	else{
		char arr[20];
		char arr2[20];
		long unit;
		long num = atol(a);
		long num2 = num;
		while(num>0){
			unit=num;
			num=num/10;
		}
		char charval = find(unit);
		for(int j=0;j<len;j++){
			arr[j]=charval;
			arr2[j]='1';
		}
		long val = atol(arr);
		long val2 = atol(arr2);
		if(num2<val2-1){
			for(int i=0;i<len-1;i++)
				cout<<"9";
			return;
		}
		if(num2>=val){
			cout<<unit;
		}
		else{
			if((flag==1 && unit-1!=0)||flag==0){
				cout<<unit-1;
			}
			for(int i=0;i<len-1;i++)
				cout<<"9";
			return;
		}
		char newvar[20];
		int i;
		for(i=0;i<len-1;i++){
			newvar[i] = a[i+1];
		}
		newvar[i]='\0';
		recurseprint(newvar,0);
	}
}
int main(){
	int T;
	cin>>T;
	char num[19];
	for(int i=0;i<T;i++){
		cin>>num;
		cout<<"Case #"<<i+1<<": ";
		recurseprint(num,1);
		cout<<"\n";
	}
}
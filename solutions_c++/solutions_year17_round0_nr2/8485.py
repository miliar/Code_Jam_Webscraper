#include <iostream>
#include <stdio.h>
#include <cmath>
#include <stdlib.h>
#include <algorithm>
using namespace std;


int main(){
	//freopen ("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	int digit[20];
	int cnt,end;
	long long int inp,tmp;
	for(int i = 1;i<=T;i++){
		cin>>inp;
		cnt = 0;
		tmp = inp;
		while(tmp!=0){
			digit[++cnt] = tmp%10;
			tmp/=10;
		}
		//cout<<"digits:";
		//for(int j = cnt;j >=1;j--)
		//	cout<<digit[j];
		//cout<<endl;
		for(int j = 1;j<cnt;j++){
			if(digit[j]<digit[j+1]){
				for(int k = 1;k <= j;k++){
					digit[k] = 9;
				}
				digit[j+1]-=1;
			}
		}
		end = 1;
		cout<<"Case #"<<i<<": ";
		for(int j = cnt;j >=1;j--){
			if(digit[j]!=0){end = j;
				break;}
		}
		for(int j = end;j >=1;j--){
			cout<<digit[j];}
		cout<<endl;
	}

}
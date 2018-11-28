#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main(){
	int i,temp,t,totaltests;
	char array[30];
	freopen("output.in", "w", stdout);
	freopen("input.in", "r", stdin);
	cin >> t;
	totaltests = t;
	while (t--){
		cin >> array;
		int len = strlen(array);
		i = len - 1;
		while (i > 0){
			if (int(array[i] - '0') < int(array[i - 1] - '0')){
				temp = array[i - 1] - '0';
				array[i - 1] = (temp - 1) + '0';
				for (int index = i; index < len; index++){
					array[index] = '9';
				}
			}
			i--;
		}
		if (array[0] == '0'){
			int j = 0;
			while (array[j] == '0')
				j++;
			int k = j;
			j = 0;
			while (k < len){
				array[j++] = array[k++];
			}
			array[j] = '\0';
		}
		cout <<"Case #"<<totaltests-t<<": "<<array<<endl;
	}
	return 0;
}
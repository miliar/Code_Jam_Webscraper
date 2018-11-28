#include <iostream>
#include <cstdlib>
#include <string.h>
#include <fstream>

using namespace std;

void createstrfromarr(string sentence, int arr[], int len){
	char a;
	int i;
	if(arr[0] == 48){
		for(i =0;i<len;i++){
			if(arr[i]!=48)
				{break;}
		}
	}
	int x = i;
	int k = 0;
	for (i= x;i<len;i++){
		a = char(arr[i]);
		sentence[k]=a;
		k++;
	}
	sentence[k]='\0';
	for (i = 0;sentence[i]!='\0';i++){
		cout<<sentence[i];
	}
}

int main(){
	std::ifstream infile("B-large.in");
	int t,l;
	int r,p,count = 0;
	int no = 0, iswhile;
//	cout<<"Enter test cases : ";
	infile >> t;
	string sentence = "";
	getline(infile, sentence);
	for(l=0;l<t;l++){
	getline(infile, sentence);
//	cout<<"string is : "<<sentence<<endl;
	count = 0;
	int len = 0;
	for (int i = 0; sentence[i] != '\0'; i++) {
		len++;
	}
	if(len == 1) {
		cout<<"Case #"<<l+1<<": "<<sentence<<endl;
		continue;
	}
	int arr[len] = {0};
	for (int i= 0;sentence[i]!='\0';i++){
		arr[i] = sentence[i];
	}
	p = 1; int sub = 0;
	int index = len-1;
//	createstrsubarr(sentence, arr[]);
	while(p != 0) {
		for(r = 0; r<len-1; r++){
			if(arr[r]>arr[r+1]){
				p = 1;
				sub = 1;
				break;
			} else {p = 0; sub = 0; }
		}
//		cout<<no--;
		if(sub == 1) {
			iswhile = 0;
			while(arr[index] == 48) {
				arr[index] = int('9');
				index =  index - 1;
				iswhile = 1;
//				cout<<arr[index];
			}
			if(iswhile == 1) {
				arr[index] = arr[index] - 1;
			} else {
				arr[index] = arr[index] -1;
			}
		}
/*		cout<<endl;
		for(r = 0;r<len;r++){
			cout<<arr[r]<<" ";
		}
		cout<<endl;
*/	}
	cout<<"Case #"<<l+1<<": ";
	createstrfromarr(sentence,arr,len);
	cout<<endl;
	}
	return 0;
}

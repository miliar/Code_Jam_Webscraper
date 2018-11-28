#include<iostream>

using namespace std;
int a[20];

int arr(int p){
	int n=p,digit=0;
	while(p){
		digit++;
		p=p/10;
	}
	p=n;
	
	int i=digit;
	a[20]={};
	while(p){
		int r=p%10;
		a[--i]=r;
		p=p/10;
	}
	return digit;
	//cout << i << endl;
}
int main(){
	int test;
	cin >> test;
	for(int t=1;t<=test;t++){
		unsigned long long int n;
		cin >> n;
		int digit=0;
		
		
		digit=arr(n);
		bool flag=false;
		while(flag==0){
			int c=0;
			for(int i=0;i<digit-1;i++){
				if(a[i]<=a[i+1]){
					c++;
				}
				else{
					n--;
					break;
				}
			}
			//cout << c << endl;	
			digit=arr(n);
			/*for(int j=0;j<digit;j++)
				cout << a[j];
			cout << endl;
			*/
			if(n%10==0){
				n--;
				
				digit=arr(n);
			/*	for(int j=0;j<digit;j++)
					cout << a[j];
				cout << endl;
			*/}
			
			if(c==digit-1)
				flag=true;
			else
				flag=false;
			//cout << flag << endl;	
			
		}
		cout << "Case #" << t << ": ";
		for(int j=0;j<digit;j++)
			cout << a[j];
		cout << endl;
	}
	return 0;
}

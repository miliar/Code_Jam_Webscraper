#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;

int main(){
	ofstream myfile;
  	myfile.open ("Pancake.txt");
	int n,c,i,j,k,x,y,l,counter=0,len,flag=0;
	char a[1001],b;
	cin>>n;
	for(k=0;k<n;k++){           //test cases
		counter=0;
		flag=0;
		i=0;
		cin>>a;
		for(i=0;i<=1001;i++){
			if(a[i]!='+'&&a[i]!='-'){
				len=i;
				break;
			}
		}
		cin>>c;      
		
		for(j=0;j<len;j++){
			if(a[j]=='-'){
				x=j;
				if((x+c)<=len){
					y=x+c-1;
					for(l=x;l<=y;l++){
						
						if(a[l]=='+'){
							a[l]='-';
						}
						else{
							a[l]='+';
						}
					}
					counter++;
				}
				else if((x+c)>len){
					
					flag=1;
					break;
				}
				
			}
		}
		if(flag==1){
			cout<<"Case #"<<k+1<<": IMPOSSIBLE"<<endl;
			myfile<<"Case #"<<k+1<<": IMPOSSIBLE"<<endl;
		}
		else{
			cout<<"Case #"<<k+1<<": "<<counter<<endl;
			myfile<<"Case #"<<k+1<<": "<<counter<<endl;
		}
	}
}

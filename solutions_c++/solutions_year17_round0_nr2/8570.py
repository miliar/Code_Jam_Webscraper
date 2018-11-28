#include<iostream>
#include<conio.h>
#include<string.h>
#include<stdlib.h>
int main(){
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
int t;
std::cin>>t;
int q=t;
while(q--){
	std::string str1;
	std::cin>>str1;
	//int i_dec = atoi(str1.c_str());
	int len =str1.size();
	//std::cout<<str1[1]<<" "<<len;
	int x=0;
	for(int i=0;i<len-1;i++){
		if(str1[i]>str1[i+1]){
			x=1;
			break;
		}
	}
	int y=t-q;
	if(x==0){
		
		std::cout<<"Case #"<<y<<": "<<str1<<"\n";
	}
	else{
		for(int i=0;i<len-1;i++){
			if(str1[i]>=str1[i+1]){
				str1[i]=str1[i]-1;
				for(int j=i+1;j<len;j++)
					str1[j]='9';
				break;
			}
		}
		if(str1[0]=='0'){
			std::cout<<"Case #"<<y<<": ";
			//long long int i_dec = atoi(str1.c_str());
			for(int i=1;i<len;i++)
			std::cout<<str1[i];
		std::cout<<"\n";
		}
		else
			std::cout<<"Case #"<<y<<": "<<str1<<"\n";
	}
}
}
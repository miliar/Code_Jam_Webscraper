#include <iostream>
#include <cstdio>
using namespace std;

int process(int , char[] );
int process2(int ,int, char[] );
int checkforallsame(char[]);
int flipcount;


int main(int argc, char const *argv[])
{
	int T,K,ans;char string[1000],space;
	cin>>T;
	
	for (int i = 0; i < T; ++i)
	{	
		cin>>string;
		//cout<<"string:"<<string<<"\n";
		cin>>K;
		//cout<<"K:"<<K<<"\n";
		ans=process(K,string);
		if(ans==-1){
			cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<"\n";
		}
		else{
			cout<<"Case #"<<i+1<<": "<<ans<<"\n";
		}		
	}
	return 0;
}

int process(int K, char string[]){
	//cout<<"string:"<<string<<"\n";
	//cout<<"K:"<<K<<"\n";
	/*if (string[0]=='+')
	{
		cout<<"string:"<<string<<"\n";
	cout<<"K:"<<K<<"\n";
	}*/
	int len=0,samecheck,retans;
	for (len = 0; string[len]!='\0'; ++len);
	if(len<K+1){
		samecheck=checkforallsame(string);
		if(samecheck!=-1){
			return samecheck;
		}
		else{
			return -1;
		}
	}

	retans=process2(K,len,string);
	return retans;

}

int checkforallsame(char string[]){
	int len=0;
	if(string[0]=='+'){
		for (len = 0; string[len]!='\0'; ++len){
			if(string[len]!='+'){return -1;}
		}
		return 0;
	}
	else {if(string[0]=='-'){
		for (len = 0; string[len]!='\0'; ++len){
			if(string[len]!='-'){return -1;}
		}
		return 1;
	}
	else {return -1;}
}

}

int process2(int K,int len, char string[]){
	int i,j,flag=1,trackflip[len]={0};
	flipcount=0;
	for(i=0;i<=len-K;i++){

		if(string[i]=='-'){
			
			if((trackflip[i]%2)==0){
			flipcount++;
			for(j=0;j<K;j++){
				
			trackflip[i+j]++;
			}
		}

		}
				if(string[i]=='+'){
			
			if((trackflip[i]%2)==1){
				flipcount++;
			for(j=0;j<K;j++){
				
			trackflip[i+j]++;
			}
		}

		}

	}
	//now check
	for (i = 0; i < len; ++i)
	{	
		if(string[i]=='-'){
			
			if((trackflip[i]%2)==0){
				flag=0;
			
			}
		}

		
				if(string[i]=='+'){
			
			if((trackflip[i]%2)==1){
				flag=0;
			
			}
		}

		}

		if(flag){
			return flipcount;
		}
		else{
			return -1;
		}
	
}
#include<iostream>
#include<stdio.h>
#include<string>
#include<stdlib.h>
using namespace std;

int getlength(long long in){
	int length=0;
	for(long long i=1;i<=1e18;i*=10){
		if(in/i>0)
			length++;
	}
	return length;
}

int main(void){
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int ca;
	char buffer[20];
	scanf("%d",&ca);
	for(int i=0;i<ca;i++){
		bool chk=false;
		long long in;
		int length;
		scanf("%lld",&in);
		length=getlength(in);
		while(chk!=true){
			for(int j=0;j<length-1;j++){//msb msb-1,msb-1 msb-2,...,lsb+1 lsb
				if(chk==true){break;}
				sprintf(buffer,"%lld",in);
				char x=buffer[j],y=buffer[j+1];

				if(x>y){//need doing stuff
					long long minus,div=1;
					for(int m=0;m<length-(j+1);m++){div*=10;}
					minus=in%div;
					in=in-minus-1;

					sprintf(buffer,"%lld",in);
					length=getlength(in);
					for(int p=0;p<length-1;p++){
						if(buffer[p]>buffer[p+1]){
							break;
						}
						if(p==length-2){chk=true;}
					}
				}
				
			}
			if(in<10)chk=true;
			for(int p=0;p<length-1;p++){
				if(buffer[p]>buffer[p+1]){
					break;
				}
				if(p==length-2){chk=true;}
			}
		}
		printf("Case #%d: %lld\n",i+1,in);
	}
}
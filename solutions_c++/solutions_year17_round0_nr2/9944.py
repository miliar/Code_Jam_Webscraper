#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

#define  ll long long
int main()
{
    ll n,x,t,num_flag,flag,pos;
    char num[100];
    cin >> t;
    for(int ii=1;ii<=t;ii++){
		cin >> num;
		n=atoll(num);
		if(n<10) printf("Case #%d: %lld\n",ii,n);
		else{
			flag=0;
			while(flag!=1){
				num_flag=1;
				int len=strlen(num);
				for(int i=0;i<len-1;i++){
					if((num[i]-'0')>(num[i+1]-'0')) num_flag=0;
				}
				if(num_flag==1) flag=1;
				else{
					for(pos=len-1;pos>0;pos--){
						if((num[pos]-'0')< (num[pos-1]-'0')) break;
					}
					num[pos-1]--;
					for(int j=pos; j<len; j++) num[j]='9';
				}
				
			}
			printf("Case #%d: %lld\n",ii,atoll(num));
		}
	}	
    return 0;
}


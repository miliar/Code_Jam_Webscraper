#include<iostream>
#include<string.h>

using namespace std;

int c2i(char c);
char i2c(int c);
int main(){


	int T,k;
	long long int i;

	string n,temp;

	cin>>T;
	k=T;
	while(T--){
		cout<<"Case #"<<k-T<<": ";
		cin>>n;


		if(n.size()>1){
			here:
			for(i=0;i<(n.size())-1;i++) 	
			{
				if(c2i(n[i])>c2i(n[i+1]))
				{
					n[i]=i2c(c2i(n[i])-1);
					for(int j=i+1;j<n.size();j++) n[j]='9';
					goto here;
					break;
				}	
			}

		}
		here1:
		if(n[0]=='0') {
			n=&n[1];
			goto here1;
		}
		cout<<n;

		cout<<endl;
	}
	return 0;
}

int c2i(char c){
	if(c=='0') return 0;
	if(c=='1') return 1;
	if(c=='2') return 2;
	if(c=='3') return 3;
	if(c=='4') return 4;
	if(c=='5') return 5;
	if(c=='6') return 6;
	if(c=='7') return 7;
	if(c=='8') return 8;
	if(c=='9') return 9;
}

char i2c(int c){
	if(c==0) return '0';
	if(c==1) return '1';
	if(c==2) return '2';
	if(c==3) return '3';
	if(c==4) return '4';
	if(c==5) return '5';
	if(c==6) return '6';
	if(c==7) return '7';
	if(c==8) return '8';
	if(c==9) return '9';
}
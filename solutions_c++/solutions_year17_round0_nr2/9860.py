#include <iostream>

using namespace std;

int T,digit,j;
string number;
char numbers[]={'0','1','2','3','4','5','6','7','8','9'};

void subtract(int pos){
	if(!pos&&number[pos]=='1'){
		number.erase(0,1);
		for(int i=0;i<number.size();i++)number[i]='9';
	}
	else if(number[pos]=='0'){for(int i=pos;i<number.size();i++)number[i]='9';subtract(pos-1);}
	else{
		for(int i=1;i<10;i++)
			if(number[pos]==numbers[i])number[pos]=numbers[i-1];
		for(int i=pos+1;i<number.size();i++)number[i]='9';
	}
}

int main(){
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>number;
		j=0;
		while(j<number.size()){
			digit=0;
			for(j=0;j<number.size();j++){
				for(;digit<10;digit++)if(number[j]==numbers[digit])break;
				//cout<<"B"<<number<<endl;
				if(digit==10){
					subtract(j);
					//cout<<"A"<<number<<endl;
					break;
				}
			}
			//if(j!=number.size())subtract(number.size()-1);
		}
		cout<<"Case #"<<t<<": "<<number<<endl;
	}
	return 0;
}

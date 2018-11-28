#include <iostream>
#include <string.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		char *input, *output;
		int len, done=0,done2=0, check=1;
		cin>>input;
		len = strlen(input);
//		cout<<input<<" "<<len<<"\n";
		if(len==1){
			cout<<"Case #"<<j<<": ";
			cout<<input<<"\n";
			continue;
		}

		for(int i=0;i<len;i++){
			
			if((i+1)<len)
				if(input[i]>input[i+1]){
					check=0;
					break;
				}

		}

		if(check==0){
			for(int i=len-1;i>=0;i--){
				if(input[i]!='9' && done==0){
					input[i]='9';
					done=1;
				}
				else{
					if(done==0)
						continue;
					int n = input[i];
					if(n!=48 && n!=49 && done2==0){
						n--;
						input[i]=n;
						done2=1;
					}
					else if(done2==0){
						if(i==0)
							input[i]=48;
						else
							input[i]=57;
					}
					int ch=0;
					for(int k=i;k<=len-1;k++){
						if((k-1)>=0){
							if(input[k-1]>input[k]){
								input[k-1]--;
								for(int z=k;z<len-1;z++)
									input[z]=57;
							}
						}
					}
				}

			}
		}
		cout<<"Case #"<<j<<": ";
		for(int i=0;i<len;i++)
			if(input[i]!='0')
				cout<<input[i];
		cout<<"\n";

	}
}
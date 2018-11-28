#include <iostream>
#include <string.h>
using namespace std;

int main(){
	int t,t2,i,j;
	cin>>t;
	t2=t;

	int k,ans[t],len,coun=0;
	string s;

	while(t>0){

		cin>>s>>k;
		len=s.length();

		for(i=0; i<len; i++){

			if(s[i]=='-'){
				if((i+k)<=len){
					for(j=0; j<k; j++){
                        if(s[i+j]=='-'){
                            s[i+j]='+';}
                        else if(s[i+j]=='+'){
                            s[i+j]='-';}
                    }
                    coun++;
				}
				else{
					coun=-1;
					break;
				}
			}
		}

		ans[t-1]=coun;
		coun=0;
		t--;
	}

	//Output
	for(i=0; i<t2; i++){
		if(ans[t2-1-i]!=-1)
			cout<<"Case #"<<i+1<<": "<<ans[t2-1-i]<<endl;
		else
			cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
		}

	return 0;
}

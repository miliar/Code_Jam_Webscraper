#include<iostream>
#include <stdio.h>
#include<string.h>
#include<vector>
using namespace std;
int main(){

	//freopen("4.in","r",stdin);
	//freopen("op4.txt","w",stdout);
	int T;
	cin>>T;
	for(int t = 1; t <= T; t++){
	
		string N;
		cin>>N;
		int n = N.length();
		for(int i = 0; i < n - 1; i++){
		
				if(N[i] > N[i+1]){
			
				while(i) {
				
		            if(N[i] == N[i-1])
		                i--;
		            else
		                break;
            	}
		        N[i]--;
		        i++;
		        while(N[i]!='\0') {
		            N[i]='9';
		            i++;
		        }
		        break;
			}
		}
		N.erase(0, N.find_first_not_of('0'));
	    cout<<"Case #"<<t<<": "<<N<<endl;
	}
	return 0;
}


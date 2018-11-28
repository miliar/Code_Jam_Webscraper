#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <set>
#include <algorithm>
#include <queue>
#include <math.h>
#include <iomanip>
#include <map>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int ij=1;ij<=t;ij++){
		char s[1001];
		int k;
		cin>>s;
		cin>>k;
		int count=0;
		int len = strlen(s);
		for(int i = 0; i < len-k+1; i++){

			if(s[i]=='-'){
				for(int j = i; j < i+k; j++)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';

				}
				count++;
			}
		}
		int flag=0;
		for(int i = 0; i < len; i++){
			//cout<<s[i];
			if(s[i]=='-')
				flag=1;
		}
		if(flag==1){
			cout<<"Case #"<<ij<<": IMPOSSIBLE";
		}
		else{
			cout<<"Case #"<<ij<<": "<<count;
		}
		cout<<endl;
	}


	
	return 0;
}

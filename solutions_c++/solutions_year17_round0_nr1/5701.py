/*
MADE BY SUDHANSH AGGARWAL
GOGLE CODE JAM 2017 QUALIFICATION ROUND
OVERSIZE PANCAKE FLIPPER
saggarw2@stevens.edu
*/

#include<iostream>
#include<string>

using namespace std;

void cjq1(int x){
	int s,k;
	string a;
	cin>>a>>k;
	s=a.length();
	if(k>s){
    	// We check if they really need to be flipped for pancakes < min needed to be flipped
    		for(int i=0;i<s;i++){
        		if (a[i]=='-'){
            		cout<<"\nCase #"<<x<<": IMPOSSIBLE";
            		return;
        		}
    		}
    	cout<<"\nCase #"<<x<<": 0";
    	return;
	}
	else{
    	int count=0,i=0;
    	for(;i<s-k+1;i++){
        	if(a[i]=='+')
            	continue;
        	else{
            	count++;
            	//FLIP
            	for(int j=0;j<i+k;j++){
                	if(a[j]=='-')
                    	a[j]='+';
                	else
                    	a[j]='-';
            	}
        	}
    	}
    	// If last k-1 things are left, we check them individually
    	for(;i<s;i++){
        	if(a[i]=='-'){
            	cout<<"\nCase #"<<x<<": IMPOSSIBLE";
            	return;
        	}
    	}
    	cout<<"\nCase #"<<x<<": "<<count;
    	return;
	}
}

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
    		cjq1(i+1);
	}
	cout<<endl;
	return 0;
}

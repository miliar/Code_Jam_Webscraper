
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <string>

using namespace std;

int main(){

    int T,j=1,R,C;
    char cake[25][25];
    freopen ("in.in","r",stdin);
    freopen ("out.out","w",stdout);

    cin>>T;
    while(j<=T){
    	//input
    	cin>>R>>C;
    	for(int i=0;i<R;i++){
    		for(int k=0;k<C;k++)
    			cin>>cake[i][k];
    	}
		// for(int i=0;i<R;i++){
  //   		for(int k=0;k<C;k++)
  //   			cout<<cake[i][k];
  //   		cout<<endl;
  //   	}
    	for(int i=0;i<R;i++){
    		//left to right
    		for(int k=1;k<C;k++){
    			if(cake[i][k]=='?')
    				cake[i][k] = cake[i][k-1];
    		}
    		//right to left
    		for(int k=C-2;k>=0;k--){
    			if(cake[i][k]=='?')
    				cake[i][k] = cake[i][k+1];
    		}
    	}
    	for(int k=0;k<C;k++){
    		//top to bottom
    		for(int i=1;i<R;i++){
    			if(cake[i][k]=='?')
    				cake[i][k] = cake[i-1][k];
    		}
    		//bottom to top
    		for(int i=R-2;i>=0;i--){
    			if(cake[i][k]=='?')
    				cake[i][k] = cake[i+1][k];
    		}
    	}
        cout<<"Case #"<<j<<": "<<endl;
        for(int i=0;i<R;i++){
    		for(int k=0;k<C;k++)
    			cout<<cake[i][k];
    		cout<<endl;
    	}
        j++;
    }
    return 0;
}

#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool  f(int n){
		int p=0;int c=n,d=n,e=0;
		while(c!=0){
			c=c/10;
			p++;
		} int a[p],b[p];
		for(int k=0;k<p;k++){
			a[k]= d%10;b[k]=a[k];
			d=d/10;
	    }
	    sort(a,a+p);
	    for(int k=0;k<p;k++){
	    	if(b[p-1-k] == a[k]){e++;}
	    }
	    if(e==p) return true;
	    else return false;
}

int main(){
	int t;
	cin>>t;
	int n;
	for(int j=0;j<t;j++){
		cin>>n;
		for(int k=n;k>0;k--){
			if(f(k)) {cout<<"Case #" << (j+1)<<": "<< k<<endl; break;}
		}
		}
}
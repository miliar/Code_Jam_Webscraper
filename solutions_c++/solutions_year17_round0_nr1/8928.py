#include<iostream>
#include<string.h>
using namespace std;

int main(){
  int t;
  cin>>t;
  
  for(int i=0;i<t;i++){
  	  char ch[1000];
  	  int k;
  	  cin>>ch>>k;
  	  
  	  
  	  int len,count=0,flag=0;
  	  len=strlen(ch);
  	  
  	  for(int j=0;j<=len-k;j++){
  	  	if(ch[j]=='-'){
  	  	  for(int m=j;m<(j+k);m++){
  	  	  	    if(ch[m]=='-')
  	  	  	       ch[m]='+';
  	  	  	    else
  	  	  	       ch[m]='-';
			  } 
			  count++;
		   }
  	  	}
  	  for(int l=len-k-1;l<len;l++){
  	  	  if(ch[l]=='-'){
  	  	  	flag++;
  	  	  	}
  	  	}
  	  	if(flag!=0)
  	  	      cout<<"Case #"<<(i+1)<<": IMPOSSIBLE"<<endl;
  	  	else
  	  	 	  cout<<"Case #"<<(i+1)<<": "<<count<<endl;
  	}
  	return 0;
}

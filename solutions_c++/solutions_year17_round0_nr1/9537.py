#include<bits/stdc++.h>
using namespace std;

int main(){
  int i,j,k,it,it2,no,iteratorr=0,strr,index=0,test;
  scanf("%d",&test);
  for(i=0;i<test;i++){
    char arr[10];
    cin>>arr>>k;
    strr=strlen(arr);
  	  for(j=0;j<=strr-k;j++){
  	  	if(arr[j]=='-'){
  	  	  for(it=j;it<(j+k);it++){
  	  	  	    if(arr[it]=='-')
  	  	  	       arr[it]='+';
  	  	  	    else
  	  	  	       arr[it]='-';
          }iteratorr++;
        }
    }
  	  for(it2=strr-1-k;it2<strr;it2++){
  	  	  if(arr[it2]=='-'){
  	  	  	index++;
      }}
  	  	if(index!=0){
                printf("Case #%d: IMPOSSIBLE\n",i+1);
  	  	}
  	  	else{
                printf("Case #%d: %d\n",i+1,iteratorr);
        }
  	}
return 0;
}

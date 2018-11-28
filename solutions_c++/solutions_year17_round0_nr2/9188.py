#include<iostream>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		  int n;
		  cin>>n;
		  
		  for(int j=n;j>=1;j--){
		  	
		  	  if((j/1000)==0){
		  	  	
		  	  	if((j/100)==0){
		  	  	    if((j/10)==0){
		               cout<<"Case #"<<i+1<<": "<<j<<endl;
		               break;
		            }
		  	  	else
		  	  	    if(j/10<=j%10){
		               cout<<"Case #"<<i+1<<": "<<j<<endl;
		               break;
		            }
		        }
		  	  	
		  	  else
		        if((j/100<=(j%100)/10)&&((j%100)/10<=j%10)){
		  	        cout<<"Case #"<<i+1<<": "<<j<<endl;
		  	        break;
		  	        }
				}
			
			   else
			     if((j/1000<=j/100)&&(j/100<=j/10)&&(j/10<=j%10)){
		  	        cout<<"Case #"<<i+1<<": "<<j<<endl;
		  	        break;
		  	    }
		  	}
		}
  return 0;
}
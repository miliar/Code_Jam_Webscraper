#include<iostream>
using namespace std;
#define fre freopen("0.in","r",stdin),freopen("0.out","w",stdout)

int main(){
    
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	/*long long*/ int n,i,t3,j;
	int t;
	cin>>t;
	int flag,t1,t2;
	    for(j=1;j<=t;j++){

	    	cin>>n;
        
            for(i=n;i>=0;i--){

            	flag=1;
                if(i<=9)
				 break;
                else{
                	t3=i;
	    	        t1=t3%10;
                    t3=t3/10;

	        	    while(t3){ 
	    		      t2 = t3%10;
	    		      if(t2 > t1)
					  {
					  	flag=0;
						  break;
						  }

                	  t3=t3/10;
                	  t1=t2;
	         	    }
     	        }
     	        if(flag==1)
				  break;

            }
            
            cout<<"Case #"<<j<<": "<<i<<"\n";
	    }
	return 0;
}

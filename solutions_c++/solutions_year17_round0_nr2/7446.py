#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main() {
 
  	
      int t;
      cin>>t;
       int c=1;
        while(t--){
            
        long long int n,ans,save;
        cin>>n;
        bool flag=false;
        int pre2=0,pre,next;
        for(long long int i=n;i>=1;){
            int count=0;
            pre=i%10;
            if(i/10==0) {ans=i; flag=true; break;}
            for(long long int j=i/10;j>0;j=j/10){
                next=j%10;
                count++;
                if(next>pre) {
                	save=j;
				break;
			}
			pre2=pre;
                pre=next;
                if(j/10==0) flag=true;
            }
            if(flag) { ans=i; break;}
            else if(pre==0&&next!=0&&pre2==0)i=i-1;
            else i=save*pow(10,count);

        }
        if(flag) cout<<"Case #"<<c<<": "<<ans<<endl;
       c++;
    }
  
	return 0;
}


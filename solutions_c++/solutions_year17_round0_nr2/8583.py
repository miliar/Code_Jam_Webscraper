#include <iostream>
using namespace std;

int main() {
    int i,t,j,count,temp,flag1;
    
    long long int n,tmp;
	cin>>t;
	for(j=1;j<=t;j++){
	    cin>>n;
	    int a[20]={0};
	    int tmp=n;
	    count=0;
	    while(tmp>=1){
	        tmp/=10;
	        count++;
	    }
	    temp=count;
	    tmp=n;
	    //cout<<count<<endl;
	    while(tmp>=1){
	        a[--count]=tmp%10;
	        tmp/=10;
	    }
	    for(i=temp-1;i>0;i--)
	    {
	        if(a[i]<a[i-1]){
	            a[i]=9;
	            a[i-1]-=1;
	        }
	        
	    }
	    int flag=0;
	    if(a[0]==0)
	    flag1=1;
	    cout<<"Case #"<<j<<": ";
	    for(i=0;i<temp;i++){
	    if(a[i]==0&&flag1)
	    continue;
	    flag1=0;
	    if(a[i]==9)
	    flag=1;
	    if(flag)
	    cout<<"9";
	    else 
	    cout<<a[i];
	    }
	    cout<<endl;
	}
	return 0;
}

#include<iostream>
#include<string>
using namespace std;
int main(){
	int TT;
	cin>>TT;
	long long int n,k;
	long long int a[100][2];
	//2*a,2*a+1
	//a-1,a


	//2*a-1,2*a
	//a-1,a

	for(int T=1;T<=TT;++T){
	    cin>>n>>k;
	    for(int i=0;i<100;++i){
	        a[i][0]=0;
	        a[i][1]=0;
	    }
	    a[0][0]=1;
	    a[0][1]=0;
	    int i=0;
	    long long int x=n;
	    cout<<"Case #"<<T<<": ";

            long long int y,z;
	    while(true){
	        y=(x-1)/2;
	        z=(x-1)/2;
	        a[i+1][0]+=a[i][0];
	        if(x%2==0){
	            y+=1;
	            a[i+1][1]+=a[i][0];
	        }
	        else{
	            a[i+1][0]+=a[i][0];
	        }
	        if(a[i][0]>=k){
	            cout<<y<<" "<<z<<"\n";
                    break;
	        }
	        else{
	            k-=a[i][0];
	        }
	        y=(x-2)/2;
	        z=(x-2)/2;
	        a[i+1][1]+=a[i][1];
	        if(x%2==1){
	            y+=1;
	            a[i+1][0]+=a[i][1];
	        }
	        else{
	            a[i+1][1]+=a[i][1];
	        }
	        if(a[i][1]>=k){
	            cout<<y<<" "<<z<<"\n";
                    break;
	        }
	        else{
	            k-=a[i][1];
	        }
	        ++i;
	        x/=2;
	    }
	}
	return 0;
}

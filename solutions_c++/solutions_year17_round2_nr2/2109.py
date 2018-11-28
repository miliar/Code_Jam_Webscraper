#include <iostream>
#include <iomanip>
using namespace std;
void settle(char *A,int r,int y,int b,char R,char Y,char B,int n){
    int i,k=0;
    for(i=0;i<r;i++){
   		 A[k]=R;
   		 k+=2;
   		}
   		if(k>=n)
   		 k=1;
   		for(i=0;i<y;i++){
   		 A[k]=Y;
   		 k+=2;
   		 if(k>=n)
   		 k=1;
   		}
   		for(i=0;i<b;i++){
   		 A[k]=B;
   		 k+=2;
   		}
}
int main() {
   int a,q,n,i,t,r,o,y,g,b,v;
   cin>>t;
   for(a=1;a<=t;a++){
   	cin>>n>>r>>o>>y>>g>>b>>v;
   	char A[n];
   	int c=n/2;
   	if(r>c || y>c ||b>c){
   	    cout<<"Case #"<<a<<": IMPOSSIBLE"<<endl;
   	}
   	else{
   	    if(r>y){
   	        if(r>b){
   	            settle(A,r,y,b,'R','Y','B',n);
   	        }
   	        else{
   	            settle(A,b,y,r,'B','Y','R',n);
   	        }
   	    }
   	    else if(y>b){
   	        settle(A,y,r,b,'Y','R','B',n);
   	    }
   	    else{
   	        settle(A,b,y,r,'B','Y','R',n);
   	    }
   		
   cout<<"Case #"<<a<<": ";
   for(i=0;i<n;i++)
    cout<<A[i];
   cout<<endl;
   	}
   }
   return 0;
}
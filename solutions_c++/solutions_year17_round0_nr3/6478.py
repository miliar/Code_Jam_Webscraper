#include<stdlib.h>
#include<stdio.h>
#include <math.h> 
#include<iostream>
#include<fstream>


using namespace std;

void rez(long long &x, long long &y){
	if(x%2==1) {x=x/2; y=x;}
	else {x=x/2; y=x-1;}
}

int main(){
ifstream in; ofstream out;
in.open("C-large (1).in"); out.open("output.txt");	
out.clear();

int t;
long long int n,k, kk, x, y, xx, yy, cX, cY, catiX, catiY, s;

in>>t; 
for(int i=1; i<=t;i++){
	in>>n>>k;
	
	if(n%2==1) {x=n/2; if(k!=1) y=0; else y=x; catiX=2; catiY=0;}
	else{ x=n/2; y=x-1; catiX=1; catiY=1;}
	s=1;
	
	while(s<k){
		
		
		if(s+catiY+catiX>=k) {
			kk=k-s;
			if(x<y)	{
				long long aux; aux=x; x=y; y=aux;
				aux=catiX; catiX=catiY; catiY=aux;
			}
			if(catiX-kk>=0) rez(x,y);
			else rez(y,x); 
			if(x<y) {long long aux; aux=x; x=y; y=aux;}	
		    s=s+catiY+catiX;		
		}
		else{
		s=s+catiY+catiX;
		cX=0; cY=0; xx=0; yy=0;
		//new X & Y + how many
		if(x%2==1 && y%2==1) {xx=x/2; yy=0; cX=cX+2*catiX+2*catiY;}
		else if(x%2==0) {
		   if(x!=0){
		     xx=x/2; if(xx-1>0) yy=xx-1; else yy=0;
		     cX=cX+catiX; cY=cY+catiX;
		   }
		   if(y%2==0 && y!=0) {cX=cX+catiY; cY=cY+catiY;}
		   if(y%2==1) {
		   	 if(y/2==xx) cX=cX+2*catiY;
		   	 else       cY=cY+2*catiY;
		   } 
		}
		else if (y%2==0) {
		if(y!=0){
		  xx=y/2; if(xx-1>0) yy=xx-1; else yy=0;
		  cX=cX+catiY; cY=cY+catiY;
	    }
		if(x%2==1){
		      if(y==0){ xx=x/2;}
			  if(x/2==xx) cX=cX+2*catiX;
			  else       cY=cY+2*catiX; 	
		   }
		}
		x=xx; y=yy; catiX=cX; catiY=cY;
		//if(i==27) cout<<"x="<<x<<" y="<<y<<" catiX="<<catiX<<" catiY="<<catiY<<" s="<<s<<endl;
		//if(x==0 && y==0) {
		  // cout<<"x="<<x<<" y="<<y<<" catiX="<<catiX<<" catiY="<<catiY<<" s="<<s<<" n="<<n<<" k="<<k<<endl; s=s+1; break;	
		//}
		
	   }
		
	} //cout<<endl;
    out<<"Case #"<<i<<": "<<x<<" "<<y<<endl;
			
	}
    
	 

   
	



in.close(); out.close();	

return 0;	
}

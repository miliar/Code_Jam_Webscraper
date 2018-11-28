#include<iostream>
using namespace std;
int check(int b){
	int r,rem;
	r=b%10;
	b=b/10;
	while(b>0){
		rem=r;
		r=b%10;
     	b=b/10;	
     	if(rem<r)return 0;
	}
	return 1;
}
int tidy(int a){
	while(a>0){
	if(check(a)==1)return a;
	a=a-1;
   }
   return 0;
}
int main()
{ 
   
    int t,last;
	cin>>t;
	if(t<1 || t>100)return 0;
	int *l_tidy=new int[t];
	for(int i=0;i<t;i++)
	{cin>>last;
	if(last<1 || last>1000)return 0;
	l_tidy[i]=tidy(last);
    }
    	for(int i=0;i<t;i++){
    		cout<<"Case #"<<i+1<<": "<<l_tidy[i]<<endl;
		}
	return 0; 
}

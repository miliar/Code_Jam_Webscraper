#include<iostream>
using namespace std;
bool tidy( int n){
int ptr,mx;
mx=n%10;
while(n){
ptr=n%10;
n=n/10;
if(ptr>mx) return false ;
else mx=ptr;
}
return true;
}

int main(){
int i,j,t;
cin>>t;
 int n;
for(j=1;j<=t;j++){
cin>>n;

for(i=n;i>=1;i--)
	if(tidy(i))
		break;
	
cout<<"Case #"<<j<<": "<<i<<endl;

}

return 0;}

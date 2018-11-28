/* All men have limits. They learn what they are and learn
   not to exceed them, I ignore mine. -Batman           */

#include <bits/stdc++.h>
//#include <Windows.h>
using namespace std;

int scan(long long int n){
	int a;int i(0);
	while(n>0){
		a=n%10;
		n/=10;
		i++;
		
		if(n%10>a)return i;
	}return 0;
}
bool tidy(long long int n){
	
	int a;
	while(n>0){
	a=n%10;
	n/=10;
	if(n%10>a)return 0;
	}return 1;
	
}

int main(){

long long int n;
int tcase;
cin>>tcase;
for(int i=1;i<=tcase;i++){
cin>>n;
cout<<"Case #"<<i<<": ";
if(tidy(n))cout<<n<<endl;
else{
	while(1){
		long long int c=pow(10,scan(n));
		n-=n%c;
		if(tidy(n)){
		cout<<n<<endl;
		break;
		}
		n--;
	}
}

}





return 0;
}


#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#define lli long long int
using namespace std;

 
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
lli t;
cin>>t;
int T=1;
while(T<=t){
lli n;
cin>>n;
bool flag;
lli ans;
for(lli i=n;i>0;i--){
lli arr[18];
int k=0;
lli N=i;
	while (N!=0)
		{
		arr[k]=N%10;
		N/=10;
		k++;	
		}
for(int j=0;j<k-1;j++){
	if(arr[j]>=arr[j+1]){
		flag=true;
		
	}
	else
		{
		flag=false;
		break;	
	}
}
if(flag==true){
	ans=i;
	break;
}
}
cout<<"Case #"<<T<<": "<<ans<<endl;
T++;
}

}


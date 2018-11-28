#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<vector>
#include<stack>
#define gc getchar_unlocked
using namespace std;
typedef long long int int64;
int64 a[1000],ln;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
int64 i,j,k,n,m,w,sum,ans,t,tmp,ist,pr=-1,cnt=1,a1;
cin>>t;
while(t--) {
	scanf("%lld",&m);
	tmp=m;ln=0;ist=1,pr=-1,a1=1;
	while(tmp>0){
		tmp/=10;
		ln++;
	}
	tmp=m;
	for(i=ln-1;i>=0;i--){
		a[i]=tmp%10;
		tmp/=10;
	}
	//for(i=0;i<ln;i++)cout<<a[i];cout<<endl;
	for(i=0;i<ln;i++){
		if (!(a[i]==0||a[i]==1) && ist==1)a1=0;

		if (a[i]<pr)ist=0;
		else pr=a[i];
	}
//	cout<<ist<<" "<<a1<<endl;
	if (ist==1){
		printf("Case #%lld: %lld\n",cnt,m);
		cnt++;
		continue;
	}
	if (a1==1){
		printf("Case #%lld: ",cnt);cnt++;
		for(i=0;i<ln-1;i++)printf("9");printf("\n");
		continue;
	}
	pr=-1;
	for (i=0;i<ln;i++) {
		if(a[i]>=pr){pr=a[i];continue;}
		else break;
	}
	//a[i-1]--;
	for(k=i-1;k>=0;k--){
		if(k==0){a[k]--;break;}
		if(a[k]>a[k-1]){a[k]--;break;}
		if(a[k]==a[k-1]){a[k]=9;}
	}
	for (;i<ln;i++) {
		a[i]=9;
	}
	printf("Case #%lld: ",cnt);cnt++;
	for(i=0;i<ln;i++)printf("%lld",a[i]);printf("\n");

}	
return 0;
}
 
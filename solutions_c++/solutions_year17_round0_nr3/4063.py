#include "iostream"
#include "cstdio"
#include "cstring"
#include "cmath"
using namespace std;
int main()
{
	freopen("C-small-2-attempt3.in.txt", "r", stdin);  
    freopen("zz.txt", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		long long n,k;
		cin>>n>>k;
		printf("Case #%d: ",cas);
		int t=log2(k);
		//cout<<t<<endl;
		long long h=pow(2,t);
		//cout<<h<<endl;
		n-=k;
		n++;
		long long zz=n/h;   //属于第几组
		if(zz*h!=n) zz++;   
		if(zz%2){
			cout<<zz/2<<" "<<zz/2<<endl;
		}else{
			cout<<zz/2<<" "<<zz/2-1<<endl;
		}
	}
	return 0;
}
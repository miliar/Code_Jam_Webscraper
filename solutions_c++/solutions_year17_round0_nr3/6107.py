#include<fstream>
using namespace std;
ifstream cin("C-large.in");
ofstream cout("my.out");
long long T,n,k;
long long hibit(long long x){
	long long res=1;
	while (res*2<=x) res*=2;
	return res;	
}
int main(){
	cin>>T;
	for (long long u=1; u<=T; u++) {
		cin>>n>>k;
		cout<<"Case #"<<u<<": ";
		long long h=hibit(k);
		long long h1=h-1;
		long long a=n-h1;
		long long r=a % h;
		long long q=a / h;
		if (r<k-h1) cout<<q/2<<" "<<(q-1)/2<<endl;
		else cout<<(q+1)/2<<" "<<q/2<<endl;
	}
	return 0;	
}

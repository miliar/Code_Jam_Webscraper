#include<fstream>
using namespace std;
ifstream cin("B-small-attempt3.in");
ofstream cout("B-small-attempt0.out");
long long t;
long long n,bit,a[20],b[20],ans[20],minn,mink;
void init(long long x){
	bit=0;
	minn=11;
	while (x) {
		a[++bit]=x % 10;
		x /= 10;
		if (a[bit]<=minn) {minn=a[bit]; mink=bit;}	
	}
} 
int main(){
	cin>>t;
	for (long long u=1; u<=t; u++) {
		cin>>n;
		cout<<"Case #"<<u<<": ";
		init(n);
		for (long long i=1; i<=bit; i++) b[bit-i+1]=a[i];
		mink=bit-mink+1;
		//cout<<"    "<<mink<<endl;
		//cout<<b[1]<<b[2]<<b[3]<<b[4]<<endl;
		//cout<<minn<<endl;
		long long now=0;
		bool bbb=false;
		while (true) {
			for (long long i=now+1; i<=mink; i++) {
				if (i!=mink) if (b[i]>minn && b[i]>=b[i+1]) {
					ans[i]=b[i]-1;
					//cout<<"fuck"<<endl;
					for (long long j=i+1; j<=bit; j++) ans[j]=9; bbb=true; break;
				}
				if (i!=mink) if (b[i]>minn && b[i]<b[i+1]) {
					ans[i]=b[i];
					continue;
					//cout<<"fuck"<<endl;
					//for (long long j=i+1; j<=bit; j++) ans[j]=9; bbb=true; break;
				}
				if (i==mink) if (b[i]>minn) {
					ans[i]=b[i]-1;
					//cout<<"fuck"<<endl;
					for (long long j=i+1; j<=bit; j++) ans[j]=9; bbb=true; break;
				}
				ans[i]=minn;
			}
			if (bbb) break;
			now=mink;
			if (now==bit) break;
			minn=11;
			for (long long i=bit; i>now; i--) {
				if (b[i]<=minn) {minn=b[i]; mink=i;}		
			}
		}
		bool is=false;
		for (long long i=1; i<=bit; i++) if (ans[i]!=0 || is) {
			is=true;
			cout<<ans[i];
		}
		cout<<endl;
	}
	return 0;
}

#include<fstream>
#include<math.h>
#include<vector>
#include<queue>
using namespace std;

ifstream cin ("A-large.in");
ofstream cout ("a.out");

long tc=0;

int doit(){
	tc++;
	long n,d;
	long k,s;
	long double t;
	cin>>d>>n;
	long double mint=-1;
	while(n--){
		cin>>k>>s;
		t = (long double)(d-k) / (long double)(s);
		if( (t>mint)||(mint==-1) ){
			mint = t;
		}
	}
	long double ans = (long double)(d) / (long double)(mint);
	cout<<"Case #"<<tc<<": "<<fixed<<ans<<endl;
}

int main(){
	long t;
	cin>>t;
	while(t--){
		doit();
	}
}

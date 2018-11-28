#include <bits/stdc++.h>
using namespace std;
long long ones[25];

void pre(){
	for(int i=1;i<=19;i++){
		long long tmp=1ll;
		for(int j=1;j<=i;j++){
			ones[i]+=tmp;
			tmp*=10ll;
		}
		//cout<<ones[i]<<endl;
	}
	return ;
}
int main(){
	pre();
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		long long n;
		cin>>n;
		int digit = 0;
		for(int i=1;i<=19;i++){
			if(n < ones[i]) {
				digit = i-1;
				break;
			}
		}
		long long re = 9;
		long long ans[20];
		ans[0] = 0;
		for(int i=1;i<=digit;i++){
			long long tmp = n/ones[digit-i+1];
			if(tmp > re){
				tmp = re;
			}

			n -= ones[digit-i+1]*tmp;
			ans[i] = ans[i-1]+tmp;
			re -= tmp;
			//cout<<i<<" "<<tmp<<" "<<n<<" "<<re<<endl;
		}
		printf("Case #%d: ",t);
		for(int i=1;i<=digit;i++){
			cout<<ans[i];
		}
		cout<<endl;

	}
}
#include <bits/stdc++.h>
using namespace std;

#define MAXN 22

char n[MAXN];

void solve(){
	for (int i = 0; n[i+1] != '\0'; ++i)
	{
		if(n[i] > n[i+1]){
			n[i]--;
			for (int j = i+1; n[j] != '\0'; ++j)
			{
				n[j] = '9';
			}
			i = -1;
		}
	}
}

int main(){
	int T, indx;
	cin>>T;
	for (int j = 1; j <= T; ++j)
	{
		cin>>n;
		cout<<"Case #"<<j<<": ";
		if(n[1] == '\0'){
			cout<<n<<endl;
		}
		else{
			solve();
			indx = 0;
			while(n[indx] == '0'){
				indx++;
			}
			for (int i = indx; n[i] != '\0'; ++i)
			{
				cout<<n[i];
			}
			cout<<endl;
		}
	}

	return 0;
}
#include<iostream>
#include<queue>
using namespace std;
bool a[1001];
string s;
int n,k,ans;
int main(){
	ios::sync_with_stdio(false);
	//freopen("pancake3.in","r",stdin);
	//freopen("pancake.txt","w",stdout);
	int t;
	cin >> t;
	for(int r=1; r<=t ;r++){
		cin >> s >> k;
		n=s.size();
		ans=0;
		for(int i=0; i<n ;i++){
			a[i]=(s[i]=='+');
		}
		for(int i=0; i<=n-k ;i++){
			if(a[i]) continue;
			ans++;
			for(int j=i; j<i+k ;j++) a[j]=!a[j];
		}
		bool ok=true;
		for(int i=n-k+1; i<n ;i++) if(!a[i]) ok=false;
		cout << "Case #" << r << ": ";
		if(!ok) cout << "IMPOSSIBLE\n";
		else cout << ans << '\n';
	}
}

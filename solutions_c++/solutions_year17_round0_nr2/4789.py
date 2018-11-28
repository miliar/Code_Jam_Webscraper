/*input
10
1000000000000000000
2
3
4
132
1000
21
111111111111111110
1000000000000000000
1234567890
*/
#include <bits/stdc++.h>
#define endl '\n'
#define fo(i,n) for(i=0;i<n;++i)
#define forr(i,n) for(i=n-1;i>=0;--i)
using namespace std;
typedef long long int ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	ifstream cin("B-large.in");
 	ofstream cout("b_large_output.txt");

	int t, i, j;
	cin>>t;
	for(int te=1;te<=t;te++){
		cout<<"Case #"<<te<<": ";
		ll m;
		ll n, temp;
		vector<ll>a;
		a.clear();
		cin>>n;
		temp = n;
		while(temp>0){
			m = temp % 10;
			a.push_back(m);
			temp /= 10;
		}
		// reverse(a.begin(),a.end());
		// for(i=0;i<(int)a.size();i++)
		// 	cout<<a[i]<<" ";
		// cout<<endl;
		for(i=1;i<(int)a.size();i++){
			if(a[i] > a[i-1]){
				a[i] = a[i] - 1;
				for(j = 0 ; j < i ; j++)
					a[j] = 9;
			}
		}
		reverse(a.begin(),a.end());
		bool z = false;
		for(i=0;i<(int)a.size();i++){
			if(a[i]==0 && z==false){
				continue;
			}
			z = true;
			cout<<a[i];
		}
		cout<<endl;
	}
	return 0;
}

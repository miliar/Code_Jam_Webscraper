#include<bits/stdc++.h>
#define fri(i,n) for(int i=0;i<n;i++)
#define fr(i,a,b) for(int i=a;i<=b;i++)
#define ol(v) v.begin(),v.end()
#define forc(v) for(auto it:v)
#define se second
#define fi first
#define pb push_back
#define pf push_front
#define MX 1e18
#define MN -MX

using namespace std;
typedef long long ll;
typedef long double ld;

template <typename T> istream&operator>>(istream &inp, vector<T> &vec){
	fri(i,vec.size()) inp>>vec[i];
	return inp;
}

template <typename T> ostream&operator<<(ostream &oup, vector<T> vec){
	forc(vec) oup<<it<<" ";
	oup<<"\n";
	return oup;
}


int main(){
	ios::sync_with_stdio(false);
	#ifdef DBG
		freopen("in", "r", stdin);
	#endif
	
	int t;
	cin>>t;
	fri(test,t){
		string s;
		int n, ans =0;
		cin>>s>>n;
		int l = s.length();
		vector<int> arr(l, 0);
		fri(i, l) arr[i] = (s[i]=='+')?1:0;
		fr(i, 0, l-n){
			if(arr[i]==0){
				ans++;
				fr(j, i, i+n-1){
					arr[j] = !arr[j];
				}
			}
		}
		bool f = 1;
		fri(i, l) if(arr[i]==0){f=0;break;}
		cout<<"Case #"<<test+1<<": ";//<<((f)?ans:"IMPOSSIBLE")<<"\n";
		if(f){
			cout<<ans<<"\n";
		}
		else cout<<"IMPOSSIBLE\n";
	}
	
	
	return 0;
}

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
		cin>>s;
		int l = s.length();
		//vector<int> arr(l, 0);
		//bool f = 0;
		for(int i=l-1;i>=0;i--){
			//arr[i] = i;
			for(int j = i-1;j>=0;j--){
				if(s[j] > s[i]){ 
					
					s[j]--;
					for(int k=j+1;k<l;k++) s[k]='9';				
				}
			}
		}
		//arr[0] = 19;
		//int mn = 19;
		/*fri(i, l) mn = min(mn, arr[i]);
		if(f){
			s[mn]--;// = '0';
			fr(i, mn+1, l-1) s[i] = '9';}*/
		int i=0;
		while(i<l and s[i]=='0')i++;
		if(i<l) s = s.substr(i, l-i);
		else s = "0";
		cout<<"Case #"<<test+1<<": "<<s<<"\n";
	}
	
	
	return 0;
}

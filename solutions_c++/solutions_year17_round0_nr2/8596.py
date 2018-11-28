#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef  vector<unsigned long long > vull;

#define pb push_back
#define mp make_pair
#define X first
#define Y second

#define rep(i,n) for(int i=0;i<(n);i++)
#define Rep(i,a,b) for(int i=(a);i<(b);i++)
#define repr(i,n) for(int i=(n-1);i>=0;i--)
#define wh(t) while(t--)
#define all(x) (x).begin(),(x).end()
#define sz(a) a.size()

#define MOD 1000000007
#define PI 3.14159265358979
#define endl '\n'
string x;


int check(string s){
	int inc=0,v;
	bool f=false;
	x=s;
	for(int i=sz(s)-1;i>=1;i--){
		if(s[i]>=s[i-1]){
			inc++;
		}
		else{
			f=true;
			v=i;

		}
	}
	if(f){
		return v;
	}
	else
		return -1;


}


int main()
{
	string s,tt;
	ll i,k,n,T;
	cin>>T;
	rep(t,T){

		cin>>s;
		while((k=check(s))!=-1){
			Rep(j,k,sz(s)){
				s[j]='9';
			}
			s[k-1]-=1;
		}

		cout<<"Case #"<<t+1<<": ";
		bool f=0;
		rep(i,sz(s)){
			if(f){
				cout<<s[i];
			}
			else{
				if(s[i]!='0'){
					f=1;
					cout<<s[i];
				}
			}
		}
		cout<<endl;

	}

	return 0;

}

/*
	Author: Hamza Hasbi
	Copyrights: "h.hamza" ==> "www.hamzahasbi.me"
	Date: 08/04/2017 17:24:56
*/
#include<bits/stdc++.h>
#define ll long long
#define ld long double
#define ull unsigned long long
#define uld unsigned long double
#define ui unsigned int
#define ud unsigned double
#define uf unsigned float
#define pi 2*acos(0.0)
#define module cin.ignore()
#define rep(i,l,r) for(auto i=l;i<=r;i++)
#define range(x,y) for(auto x:y)
//inline lcm(int a,int b) {return a*b/__gcd(a,b);}
//inline gcd(ll a,ll b) {return 1LL*b == 0 ? a : gcd(1LL*b, a*1LL % b*1LL);}
using namespace std;


bool tidy(unsigned long long a){
	vector<int>digits;
	vector<int>dup;
	while(a){
		digits.push_back(a%10);
		dup.push_back(a%10);
		a/=10; 
	}
	reverse(digits.begin(),digits.end());
	sort(dup.begin(),dup.end());
	for(int i=0;i<digits.size();i++){
		if(dup[i]!=digits[i]) return false;
	}
	return true;
}
main()
{

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	freopen("outputB.out","w",stdout);
	freopen("B-small-attempt0.in","r",stdin);
	int t,it=1;
	cin>>t;
	while(t--){
		unsigned long long n;
		cin>>n;
		
		unsigned long long lo=1,hi=n,curr=1;
		
		while(lo<=hi){
			if(tidy(lo)) curr=lo;
			lo++;
		}
		
		cout<<"Case #"<<it++<<": "<<curr<<endl;
	}
	
	return 0;
}


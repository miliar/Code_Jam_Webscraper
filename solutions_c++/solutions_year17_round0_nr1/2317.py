//teja349
#include <bits/stdc++.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <utility>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <iomanip> 
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 << endl; prints xxx77
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx


using namespace std;
#define f(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) f(i,0,n)
#define fd(i,a,b) for(i=a;i>=b;i--)
#define pb push_back
#define mp make_pair
#define vi vector< int >
#define vl vector< ll >
#define ss second
#define ff first
#define ll long long
#define pii pair< int,int >
#define pll pair< ll,ll >
#define sz(a) a.size()
#define inf (1000*1000*1000+5)
#define all(a) a.begin(),a.end()
#define tri pair<int,pii>
#define vii vector<pii>
#define vll vector<pll>
#define viii vector<tri>
#define mod (1000*1000*1000+7)
#define pqueue priority_queue< int >
#define pdqueue priority_queue< int,vi ,greater< int > >

//std::ios::sync_with_stdio(false);  
string s;  
int flip(int ind,int k){
	int i;
	rep(i,k){
		if(s[i+ind]=='+'){
			s[ind+i]='-';
		}
		else{
			s[ind+i]='+';
		}
	}
	return 0;

}
int main(){
	std::ios::sync_with_stdio(false);
	int t;
	cin>>t;
	int t1=t;
	while(t--){
		cout<<"Case #"<<t1-t<<": ";
		int k,i,haha=0;
		cin>>s;
		cin>>k;
		int n=s.length();
		rep(i,s.length()){
			if(i+k-1==n){
				break;
			}
			if(s[i]=='+')
				continue;
			haha++;
			flip(i,k);

		}
		int flag=0;
		rep(i,s.length()){
			if(s[i]=='-'){
				flag=1;
				break;
			}
		}
		if(flag)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<haha<<endl;
	}
}


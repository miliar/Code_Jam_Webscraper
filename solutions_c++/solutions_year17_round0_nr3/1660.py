#include <bits/stdc++.h>
#define ll long long

// IDE: Code::Blocks
// Programming language: c++11
// Compiler: g++

using namespace std;

int main()
{
	// input and output files data.in and output.out
	ifstream cin("data.in");
	ofstream cout("output.out");
    int t;
    cin>>t;
    for(int i=1; i<=t; i++){
		priority_queue<ll>Q;
		unordered_map<ll, ll>M;
		ll n, k;
		cin>>n>>k;
		Q.push(n);
		M[n]=1;
		ll f;
		while(k>0){
			f=Q.top();
			if(!M[f/2])Q.push(f/2);
			M[f/2]+=M[f];
			if(!M[f/2-(f%2==0)])Q.push(f/2-(f%2==0));
			M[f/2-(f%2==0)]+=M[f];
			Q.pop();
			k-=M[f];
		}
		ll a = f/2;
		ll b = f/2-(f%2==0);
		cout<<"Case #"<<i<<": "<<a<<" "<<b<<endl;
    }
}

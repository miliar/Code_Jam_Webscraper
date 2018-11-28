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
    int A[20];
    for(int i=1; i<=t; i++){
		ll n;
		cin>>n;
		int cnt=0;
		while(n){
			A[cnt++]=n%10;
			n/=10;
		}
		int mini = A[0];
		for(int i=1; i<cnt; i++){
			if(A[i]>mini){
				while(A[i]==0)i++;
				A[i]--;
				for(int j=0; j<i; j++)A[j]=9;
				mini=A[i];
			}
			mini=min(A[i], mini);
		}
		cout<<"Case #"<<i<<": ";
		for(int i=cnt-1-(A[cnt-1]==0); i>=0; i--){
			cout<<A[i];
		}cout<<endl;
    }
}

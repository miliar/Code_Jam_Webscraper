#include <bits/stdc++.h>
#define endl '\n'
#define ll long long
#define ii pair<int, int>
#define vi vector<int, int>
#define vii vector<pair<int, int>>
#define fi first
#define se second
#define pb push_back
#define mp make_pair

//Language: c++11
//Compiler: g++
//IDE: Code::Blocks

using namespace std;

double d, pos, v, mt;
int n;

int main()
{
	int t;
	double ans;
	cin>>t;
	for(int k=1; k<=t; k++){
		cin>>d>>n;mt=0;
		for(int i=0; i<n; i++){
			cin>>pos>>v;
			mt=max(mt, (d-pos)/v);
		}
		cout<<setprecision(30)<<"Case #"<<k<<": "<<d/mt<<endl;
	}
	cin>>ans;
}

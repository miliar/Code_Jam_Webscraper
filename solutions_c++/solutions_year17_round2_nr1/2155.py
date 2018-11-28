#include <bits/stdc++.h>
using namespace std;
#define ll long long int


int main(){
#ifndef LOCAL
    ifstream cin("input.in");
    ofstream cout("output.out");
#endif
	int g;
	cin>>g;
	for(int j = 1;j<=g;j++){
           double d, n;
           cin>>d>>n;
           double y = 0;
          for(int i = 0;i<n;i++){
          	double k, s;
          	cin>>k>>s;
          	y = max(y, (d-k)/s);
          }
          cout<<"Case #"<<j<<":"<<" ";
          cout<<fixed<<setprecision(6)<<d/y<<endl;
	}
}

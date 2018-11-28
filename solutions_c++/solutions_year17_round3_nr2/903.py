#include<bits/stdc++.h>

using namespace std;
               
void solve()
{
	int n, m, x1, x2, y1, y2;

	cin>>n>>m;
	cin>>x1>>y1;
	if(n+m>1) cin>>x2>>y2;
	if(n==1 || m==1) {
		cout<<2<<endl;
		return;
	}


	if(x1>x2) 
		swap(x1, x2),
		swap(y1, y2);

	if((x2-y1)>=720 || (y2-x1)<=720) 
		cout<<2;
	else
		cout<<4;
	cout<<endl;
}

int main()
{
	int T;
	cin>>T;

	for(int i=1; i<=T; ++i)
		cout<<"Case #"<<i<<": ",
		solve();
	return 0;
}
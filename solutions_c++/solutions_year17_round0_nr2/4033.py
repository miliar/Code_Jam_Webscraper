#include<bits/stdc++.h>
using namespace std;

static const int MOD = 1000000007;

#define ll long long
#define ull unsigned long long

//DEBUG
bool debug=false;
#define DEB(x) if(debug==true){clog<<#x<<" = "<<x<<endl;}
#define DEB2(x,y) if(debug==true){clog<<#x<<" = "<<x<<"; "<<#y<<" = "<<y<<endl;}


int main(int argc,char *argv[])
{
	std::ios_base::sync_with_stdio(false);
	if(argc>1&&string(argv[1])=="-d") debug=true;

	int i,j,k,t,n,case_no=0,temper;
	ll m;
	string A;
	cin>>t;
	while(t--)
	{
		cin>>m;
		A=to_string(m);
		n=A.size();
		for(i=n-1;i>0;i--)
		{
			if(A[i]<A[i-1]){
				j=i;
				temper=A[i];
				while(j<n&&A[j]<'9'){
					A[j]='9';
					j++;
				}
				A[i-1]--;
			}
		}
		cout<<"Case #"<<(++case_no)<<": "<<stoll(A)<<endl;
	}
	return 0;
}
#include<bits/stdc++.h>
using namespace std;

static const int MOD = 1000000007;

#define ll long long;
#define ull unsigned long long;

//DEBUG
bool debug=false;
#define DEB(x) if(debug==true){clog<<#x<<" = "<<x<<endl;}
#define DEB2(x,y) if(debug==true){clog<<#x<<" = "<<x<<"; "<<#y<<" = "<<y<<endl;}


int main(int argc,char *argv[])
{
	std::ios_base::sync_with_stdio(false);
	if(argc>1&&string(argv[1])=="-d") debug=true;

	int i,j,k,t,n,m,case_no=0,countr=0;
	string s;
	cin>>t;
	while(t--)
	{
		cin>>s;
		cin>>k;
		n=s.size();
		countr=0;
		for(i=0;i<=n-k;i++)
		{
			if(s[i]=='-')
			{
				for(j=i;j<i+k;j++)
				{
					if(s[j]=='+')
						s[j]='-';
					else if(s[j]=='-')
						s[j]='+';
				}
				countr++;
			}
		}
		bool impossible=false;
		for(i=n-k+1;i<n;i++)
		{
			if(s[i]=='-'){
				impossible=true;
				break;
			}
		}
		cout<<"Case #"<<(++case_no)<<": ";
		if(impossible)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<countr<<endl;
	}
	return 0;
}
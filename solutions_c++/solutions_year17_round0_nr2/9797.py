/*input
3
132
1000
7
*/
#include <bits/stdc++.h>
using namespace std;
#define lint long long
#define inf LLONG_MAX
#define fori(a,b) for(lint i=a;i<b;i++)
#define forj(a,b) for(lint j=a;j<b;j++)
typedef vector<int> vi;
#define pair < lint , lint > pii
#define pb(y) push_back(y)
#define cin fin
#define cout fout
int main() {
	// your code goes here
	ifstream fin;
	ofstream fout;
	fin.open("B-small-attempt0.in",ios::in);
	fout.open("output b.txt",ios::out);
	lint t;
	cin>>t;
	for(lint zx=1;zx<=t;zx++)
	{
		cout<<"Case #"<<zx<<": ";
		lint n;
		cin>>n;
		lint ans=1;
		fori(1,n+1)
		{
			lint x=i;
			lint arr[4];
			arr[0]=0;
			arr[1]=0;
			arr[2]=0;
			arr[3]=0;
			arr[0]=x%10;
			x=x/10;
			arr[1]=x%10;
			x=x/10;
			arr[2]=x%10;
			x=x/10;
			arr[3]=x%10;
			lint flag=0;
			forj(0,3)
			{
				if(arr[j]<arr[j+1])
					flag=1;
			}
			if(flag==0)
				ans=i;

		}
		cout<<ans<<"\n";
		
	}
	return 0;
}
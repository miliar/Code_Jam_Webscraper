    #include <cstdio>
	#include <iostream>
	#include <string.h>
	#include <cstring>
	#include <cmath>
	#include <math.h>
	#include <algorithm>
	#include <iomanip>
	#include <map>
	#include <set>
	#include <vector>
	#include <sstream>
	#include <queue>	
	#include <bitset>
	using namespace std;	
	#define FOR(i,f_limit) for(long long int i=0;i<f_limit;i++)
	#define FR(i,s_limit,f_limit) for(long long int i=s_limit;i<f_limit;i++)
	typedef long long int llong;
	// typedef vector<int> vi;
	// typedef pair<int ,int> ii;
	// typedef vector<ii> vii;

	int main()
	{
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
		ios_base::sync_with_stdio(false);
		cin.tie(NULL);
		llong t;
		cin>>t;
		llong c=1;
		while(t--)
		{
			string n;
			cin>>n;
			llong pos,maxi=n[0]-'0';
			llong f=0,st;
			llong freq[10]={0};
			FOR(i,n.length())
			{
				
				if(n[i]-'0'<maxi)
				{
					pos=i;
					f=1;
					break;
				}
				else
				{
					maxi=n[i]-'0';
					freq[maxi]++;
					if(freq[maxi]==2) st=i-1;
				}
			}
			if(f==0)
			{
				cout<<"Case #"<<c++<<": "<<n<<endl;
				continue;
			}
			if(freq[maxi]>1) pos=st+1;
			n[pos-1]=n[pos-1]-1;
			FR(i,pos,n.length())
			{				
				n[i]='9';
			}
			string temp;
			if(n[0]=='0')
			{
				cout<<"Case #"<<c++<<": ";
				FOR(i,n.length()-1)
				{
					cout<<n[i+1];
				}
				cout<<endl;
			}
			else cout<<"Case #"<<c++<<": "<<n<<endl;

		}
		
		return 0;
	}
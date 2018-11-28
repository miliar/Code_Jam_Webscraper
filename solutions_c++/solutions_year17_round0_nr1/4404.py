#include<bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;

#define fast ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define endl '\n'
#define pb push_back
#define mp make_pair
#define full(a) a.begin(),a.end()
#define mem(a,x) memset(a,x,sizeof(a))
#define test int t;cin>>t; while(t--)
#define MOD 1000000007

using namespace std;

bool flip(bool a)
{
	return !a;
}

int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("output.txt","w",stdout);
	//srand(time(NULL));
	int t;
	cin>>t;
	int hmm = 0;
	while(t--)
	{
		string s;
		int k;
		cin>>s;
		cin>>k;
		bool a[s.length()];	
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='+') a[i] = 1;
			else a[i] = 0;
		}
		cout<<"Case #"<<++hmm<<": ";
		int ANS = 0;
		for(int i=s.length()-1;i>=0;--i)
		{
			if(a[i]==0 && i>=(k-1))
			{
				ANS++;
				int c = 0; 
				for(int j=i;c<k;--j)
				{
					a[j] = flip(a[j]);
					c++;
				}
			}
		}
		bool allOne = true;
		for(int i=0;i<s.length();i++) if(a[i]==0) allOne = false;
		if(allOne) cout<<ANS<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
		
	}	
}

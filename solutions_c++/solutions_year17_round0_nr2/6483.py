#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
typedef long double ld;
typedef vector<int> vi; 
typedef vector<ll> vl; 
typedef vector<ld> vd; 
typedef vector<vi> vvi; 

#define IOS         ios_base::sync_with_stdio(false); 
#define pb          push_back
#define mp          make_pair
#define mod         1000000007
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n)   for(int (i) = 0; (i) < (n); ++(i))
#define mem(i,n)    memset(i,n,sizeof(i))
#define gcd(a,b)    __gcd(a,b)
#define sz(a)       ((int)(a.size()))
#define len(a)      ((int)a.length())
#define all(vi)     vi.begin(), vi.end()
#define mem(i,n)    memset(i,n,sizeof(i))
#define ff          first
#define ss          second
#define trav(container, it)      for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define present(container, element) (container.find(element) != container.end()) 
#define cpresent(container, element) (find(all(container),element) != container.end()) 	second

typedef vector<vector<int> > matrix;

int main(int argc, char const *argv[])
{
	IOS;
	int t;
	cin>>t;
	int tcount=0,k;
	string str="";
	while(t--)
	{
		tcount++;
		str="";
		cin>>str;
		//cout<<str<<endl;
		int l=len(str);
		int i=1;
		while(i<l)
		{
			if(str[i]<str[i-1])
			{
				str[i-1]=str[i-1]-1;
				int pos=i-1;
				while(pos>0)
				{
					if(str[pos-1]>str[pos])
						str[pos-1]=str[pos-1]-1;
					else
						break;
					pos--;
				}
				i=pos+1;
				while(i<l)
				{
					str[i]='9';
					i++;
				}
				break;
			}
			i++;
		}
		//cout<<str<<endl;
		bool flag=false;
		rep(i,l)
		{
			if(str[i]=='0')
			{
				flag=true;
				break;
			}
		}
		int start=0;
		if(flag)
		{
			start=1;
			FOR(i,1,l-1)
			{
				str[i]='9';
			}
		}
		cout<<"Case #"<<tcount<<": ";
		FOR(i,start,l-1)
		{
			cout<<str[i];
		}
		cout<<endl;
	}
	return 0;
}
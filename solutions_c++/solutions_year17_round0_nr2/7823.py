#include<bits/stdc++.h>

using namespace std;

typedef long long int ll;

typedef vector <int> vi;
typedef vector <long> vl;
typedef vector <long long> vll;
typedef pair<int,int> pai;

typedef pair<int,string> pas;

typedef vector <pai> vpai;
typedef vector<pas > vpas;

const ll INF=ll(1e18);
const int MOD=1e9+7;


#define init(x) memset(x,0,sizeof(x))



int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	freopen("B-small-attempt0.txt","r",stdin);
	freopen("output 2 -s.txt","w",stdout);
	int tt,p=1;
	cin>>tt;
    //bhavesh
	while(p<=tt)
	{
		cout<<"case #"<<p<<": ";
		string s,s1="";
		cin>>s;
		int n=s.length(),i=0;
		for (int i = 1; i < n; i++)
		{
			if(s[i]<s[i-1])
			{
				s[i-1]=s[i-1]-1;
				if(s[i-1]=='0')
				{
					//s.erase(0,n);
					s="";
					for(int j=0;j<n-1;j++)
					{
						s+='9';
					}
					break;
				}
				else
				{
					for(int j=i;j<n;j++)
					{
						s[j]='9';
					}
					i-=2;
				}
			}
		}
		cout<<s<<"\n";
		p++;
	}
}

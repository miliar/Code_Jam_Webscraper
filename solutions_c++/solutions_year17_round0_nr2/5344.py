//Author:- IITian_Sujal
//let's keep it simple and easy....
#include<bits/stdc++.h>
#define ll          long long int
#define mp          make_pair
#define pii         pair<int,int>
#define pb          push_back
#define vi          vector<int>
#define Max(a,b)    ((a)>(b)?(a):(b))
#define Min(a,b)    ((a)<(b)?(a):(b))
#define rep(i,a,b)  for (__typeof((b)) i=(a);i<(b);i+=1)
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define mod	        1000000007
#define endl        '\n'
using namespace std;

int main()
{
	int t;
	freopen("1.txt","r",stdin);
	freopen("a.out","w",stdout);
	cin >>t;
	rep(y,1,t+1)
	{
		string s;
		cin >>s;
		//cout<<s<<" ";
		int l=s.size();
		for (int i = l-1; i >=0; i--)
		{
			for (int j = i-1; j >=0; j--)
			{
				if(s[j]>s[i])
				{
					s[j]-=1;
					for(int k=j+1;k<l;k++)
					{
						s[k]='9';
					}
					break;
				}
			}
		}
		int z=0;
		for(int i=0;i<l;i++)
		{
			if(s[i]!='0')
			{
				z=i;
				break;
			}
		}
		cout<<"Case #"<<y<<": ";
		for (int i = z; i < l; ++i)
		{
					cout<<s[i];			
		}
		cout<<endl;

	}
}

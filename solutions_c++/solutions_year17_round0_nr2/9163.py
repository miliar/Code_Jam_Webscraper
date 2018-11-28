#include<bits/stdc++.h>
#define ll long long
#define vi vector<int>
#define vc vector<char>
#define vll vector<ll>
#define pb push_back
#define sf scanf
#define pf printf
#define mp make_pair
#define all(V) V.begin(),V.end()

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t;
	ifstream fin;
	ofstream fout;
	fin.open("B-large.txt");
	fout.open("op.txt");
	fin>>t;
	int ii=0;
	while(t--)
	{
		ii++;
		char a[20];
		fin>>a;
		int n=strlen(a);
		for(int i=1;i<n;i++)
		{
			if(a[i-1]>a[i])
			{
				a[i-1]--;
				for(int j=i;j<n;j++)
				{
					a[j]='9';
				}
				for(int j=i-2;j>=0;j--)
				{
					if(a[j]>a[j+1])
					{
						a[j]--;
						a[j+1]='9';
					}
				}
				break;
			}
		}
		ll ans=0;
		for(int i=0;i<n;i++)
		{
			ans=ans*10+(a[i]-'0');
		}
		fout<<"Case #"<<ii<<": "<<ans<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}


/* 
Name: Mohit Khare
B.Tech 2nd Year
Computer Science and Engineering
MNNIT Allahabad
*/
#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define ALL(x) x.begin(), x.end()
#define boost ios_base::sync_with_stdio(false);

#define mem(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define mp make_pair
#define X first
#define Y second

#define rep(i,n) for(int i=0;i<n;i++)
#define repr(i,a,b) for(int i=a;i<b;i++)
#define revr(i,a,b) for(int i=a;i>b;i--)
#define pr1(a) cout<<a<<endl;
#define pr2(a,b) cout<<a<<" "<<b<<endl;

//const int dx[4]={0,1,0,-1};
//const int dy[4]={1,0,-1,0};
#define linf 99999999999999999ll	
#define PI 3.1415926535897932384626
#define mod 1000000007
const int maxn=1e5+1;

int main()
{
	freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	rep(tt,t)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int len = s.length();
		int ans = 0,f=0,neg=0,pos=0,neg2=0;
		int a[len+1];
		a[0]=-1;
		repr(i,1,len+1)
		{
			if(s[i-1]=='-')
				a[i] = 0;
			else a[i] = 1;
		}
		int freq[len+10];
		memset(freq,0,sizeof(freq));
		int ind= 0;
		for(int i = 1; i+k<=len+1;i++)
		{
			freq[i]+=freq[i-1];
			ind = i;
			if( (a[i]==0 && freq[i]%2==0) || (a[i]==1 && freq[i]%2==1) )
			{
				if(freq[i+k]<len+2)
				{
					freq[i+k]--;
					freq[i]++;
					ans++;
					//cout<<i<<endl;
				}
			}
			//cout<<freq[i]<<" ";
		}
		for(int j = ind+1;j<=len;j++)
			freq[j]+=freq[j-1];
		repr(i,1,len+1)
		{
			if((a[i]==0 && freq[i]%2==0) || (a[i]==1 && freq[i]%2==1))
			{
				f=1;
				break;
			}
		}	
		if(f)
			cout<<"Case #"<<tt+1<<": IMPOSSIBLE\n";
		else 
			cout<<"Case #"<<tt+1<<": "<<ans<<endl;
	}
	return 0;	
}
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
		ll n;
		cin>>n;
		cout<<"Case #"<<tt+1<<": ";
		ll k = n;
		int arr[20],l=0,s=0,ch[20];
		while(k>0)
		{
			k/=10;
			l++;
		}
		k = n;
		int j = 0;
		while(k>0)
		{
			arr[l-j-1] = k%10;
			//arr[l-j-1] = ch[s];
			//s++;
			k/=10;
			j++;
		}
		int ini = arr[l-1],ind=0;
		for(int i = l-2;i>=0;i--)//got the index
		{
			if(arr[i] > ini)
			{
				arr[i]--;
				for(int m = i+1; m < l;m++)
				{
					arr[m] = 9;
				}
			}
			ini=arr[i];
		}
		int n1 = 0;
		rep(i,l)
		{
			if(arr[i]==0 && n1==0)
			{
				continue;
			}
			else
			{
				n1=1;
				cout<<arr[i];
			}
		}
		cout<<endl;
	}
	return 0;	
}
#include<bits/stdc++.h> //_Shaffi
using namespace std;
#define sc scanint
#define sl scanlong
#define gc getchar
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define in(a,arr) sc(a); arr.push_back(a);
#define mi 100000007
#define DO int t; scanf("%d",&t); while(t--)
#define st(arr); sort(arr.begin(),arr.end());
#define er(arr); arr.erase(unique(arr.begin(),arr.end()),arr.end());
#define INF INT_MAX
#define mx(arr) *max_element(arr.begin(),arr.end())
#define mn(arr) *max_element(arr.begin(),arr.end())
#define getst(s) getline(cin>>ws,s)
#define sci(a,b) sc(a),sc(b);
#define scl(a,b) sl(a),sl(b);
#define MAX 664579
typedef long long ll;
typedef vector<int> vi;
typedef vector<pair<int,int> > pi;
void scanint(int &x);
void scanlong(ll &x);
void scanint(int &x)
{
        int flag=0;
        register int c = gc();
        if(c == '-') flag=1;
	x = 0;
	for(;(c<48 || c>57);c = gc());
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
        if(flag == 1)x=-x;
}
void scanlong(ll &x)
{
        int flag=0;
        register int c = gc();
        if(c == '-') flag=1;
	x = 0;
	for(;(c<48 || c>57);c = gc());
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
        if(flag == 1)x=-x;
}
ll N,K,num,temp;
ll dp[101],arr[101];
int main()
{
	int t,i;
	sc(t);
	for(i=1;i<=t;i++)
	{
		sl(N); sl(K);
		int count=-1;
		arr[0]=N/2;
		if(N%2==0)
        {
            dp[0]=1;
        }
		else
        {
            dp[0]=2;
        }
		num=K;
		while(num!=0)
		{
			num=num/2;
			count++;
		}
		for(int j=0;j<count;j++)
		{
			if(arr[j]%2==0)
            {
                dp[j+1]=dp[j];
            }
			else
            {
                dp[j+1]=dp[j] + pow(2,j+1);
            }
			arr[j+1]=arr[j]/2;
		}


		if(dp[count] < K + 1 - pow(2,count))
        {
            cout << "Case #" << i << ": " << arr[count]-1 << " " << arr[count]-1 << endl;
        }
		else if (dp[count] >= K+1 )
        {
            cout << "Case #" << i << ": " << arr[count] << " " << arr[count] << endl;
        }
		else
        {
            cout << "Case #" << i << ": " <<arr[count]  << " " << arr[count]-1 << endl;
        }
	}
	return 0;
}

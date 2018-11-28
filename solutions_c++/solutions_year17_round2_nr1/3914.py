/*  chuckie   */
#include <bits/stdc++.h>
#define CHUCKIE

 
#define cint(d) scanf("%d", &d)
#define cint2(a, b) scanf("%d %d", &a, &b)
#define cint3(a, b, c) scanf("%d %d %d", &a, &b, &c)
#define cint4(a, b, c, d) scanf("%d %d %d %d", &a, &b, &c, &d)
 
#define clong(d) scanf("%lld", &d)
#define clong2(a, b) scanf("%lld %lld", &a, &b)
#define clong3(a, b, c) scanf("%lld %lld %lld", &a, &b, &c)
#define clong4(a, b, c, d) scanf("%lld %lld %lld %lld", &a, &b, &c, &d)
 
const long long MOD = 1000000007;
#define MODSET(d) if ((d) >= MOD) d %= MOD;
#define MODR(d) ((d)>=MOD?(d)%MOD:(d))
#define MODNEGSET(d) if ((d) < 0) d = ((d % MOD) + MOD) % MOD;
#define MODADDSET(d) if ((d) >= MOD) d -= MOD;
#define MODADDWHILESET(d) while ((d) >= MOD) d -= MOD;
 
#define foreach(it,c) for(__typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++) 
#define MAX 1000000
#define ll long long
#define mp make_pair
#define pb push_back
 
using namespace std;

typedef vector<int> vi;
typedef pair<int,int> ii;


bool cmp(int arr1[], int arr2[])
{
	return arr1[0] < arr1[1];
}


int main()
{
	
	#ifdef CHUCKIE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int t,case_no=1;
	cin>>t;
	
	while(t--)
	{
		cout<<fixed;
		cout<<setprecision(12);
		long double d, n;
		cin>>d>>n;
		
		vector<pair<long double,long double > > arr;
		//long double arr[10004][2];
		arr.resize(10004);
		
		for(int i=0;i<n;i++)
		{
			cin>>arr[i].first>>arr[i].second;
		}
		
		//sort(arr[0],arr[0]+n,cmp);
		sort(arr.begin(),arr.begin() + n);
		
		long double mins=9999999999;
		int minidx=99999999;
		
		for(int i=n-1;i>=0;i--)
		{
			//cout<<arr[i].second<<endl;
			if(arr[i].second<=mins)
			
			{
				mins=arr[i].second;
				minidx=i;
			}
		}
		//cout<<minidx<<" ";
	   long double prevt=(d-arr[minidx].first)/mins,currt,prevs=arr[minidx].second,prevk=arr[minidx].first;
	   //cout<<prevt<<endl<<d<<endl<<arr[minidx].first<<endl<<mins<<endl;
		
		for(int i=minidx-1; i>=0;i--)
		{
			if(arr[i].second <= prevs)
			{
				prevt=(d-arr[i].first)/arr[i].second;
				prevs=arr[i].second;
				prevk=arr[i].first;
				continue;
			}
			
			else{
			currt=(prevk-arr[i].first)/(arr[i].second-prevs);
			if(currt>=prevt)
			{
				prevt=(d-arr[i].first)/arr[i].second;
				prevs=arr[i].second;
				prevk=arr[i].first;
			}
			}
			
		}
		//cout<<prevt<<" "<<d;
		
		long double ans=d/prevt;
		cout<<fixed;
		cout<<setprecision(12);
		cout<<"Case #"<<case_no++<<": "<<ans<<"\n";
		
	}
	
	
	
	return 0;
}

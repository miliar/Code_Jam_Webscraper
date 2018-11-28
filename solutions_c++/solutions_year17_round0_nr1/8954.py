/*
Name: Sushant Oberoi
MNNIT Allahabad
*/		
#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define sd(a) scanf("%d",&a)
#define slld(a) scanf("%lld",&a)
#define fl(i,a,b) for(int i=a;i<b;i++)
#define fle(i,a,b) for(int i=a;i<=b;i++)
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0)
#define wl(t) while(t--)
#define mod 1000000007
#define MAX 1000000
#define pb push_back
#define mp make_pair
#define fi first
#define se second

int main()
{
	int t;
	sd(t);
	int x=1;
	wl(t){
		printf("Case #%d: ",x++);
		string s; int k;
		cin>>s; sd(k);
		int ans=0;
		int len=s.length();
		int f[len+1]={0};
		fle(i,0,len-k){
		    	if(i>0)
			   f[i]+=f[i-1];
			if(s[i]=='-' && (!(f[i]&1))){
				ans++;
				f[i]++;
				f[i+k]--;
			}
			else if(s[i]=='+' && (f[i]&1)){
				ans++;
				f[i]++;
				f[i+k]--;
			}
		}
		int flag=0;
		fl(i,len-k+1,len){
		    f[i]+=f[i-1];
		    if(s[i]=='-' && (!(f[i]&1)) || s[i]=='+' && (f[i]&1))
			{
				flag=1;
				break;
			}
		}
		if(flag) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}
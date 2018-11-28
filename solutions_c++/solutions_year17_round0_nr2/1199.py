#include<bits/stdc++.h>
#define pb push_back
#define ll long long int
#define inf 1450000090
#define fastio ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define sd(x) scanf("%d",&x)
#define sd2(x,y) scanf("%d%d",&x,&y)
#define sdl(x) scanf("%lld",&x)
#define nax 100010
#define mp make_pair
#define sz(x) (int)(x.size())
#define pi pair <int ,int >
#define pii pair < int , pair <int ,int > >
#define MOD 1000000007
using namespace std;
int arr[25];
int convert(ll t)
{
	int ctr = 0 ;
	ll cpy = t;
	while(cpy!=0)
	{
		cpy/=10;
		ctr++;
	}
	for (int i = ctr-1; i >= 0; --i)
	{
		arr[i] = t%10;
		t/=10;
	}
	return ctr;
}
int main(int argc, char const *argv[])
{
  freopen("input.txt","read",stdin);
  freopen("output.txt","write",stdout);
  int t;
  sd(t);
  for(int tt=1;tt<=t;tt++)
  {
  	 printf("Case #%d: ",tt);
  	 ll n;
  	 sdl(n);
  	 memset(arr,0,sizeof arr);
  	 int ctr = convert(n);
  	 for (int i = 0; i < ctr-1; ++i)
  	 {
  	 	if(arr[i] > arr[i+1])
  	 	{
  	 		int ptr = i;
  	 		while(ptr >= 0 && arr[ptr] == arr[i])
  	 			ptr--;
  	 		ptr++;
  	 		arr[ptr]--;
  	 		for (int j = ptr+1; j < ctr; ++j)
  	 		{
  	 			arr[j] = 9;
  	 		}
  	 	}
  	 }
  	 int start = 0;
  	 if(arr[start] == 0)
  	 	start++;
  	 for (int i = start; i < ctr; ++i)
  	 {
  	 	printf("%d",arr[i]);
  	 }
  	 puts("");
  }
  return 0;
}
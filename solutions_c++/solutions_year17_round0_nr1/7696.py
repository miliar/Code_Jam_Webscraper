#include<bits/stdc++.h>

#define vi vector <int>
#define vlli vector <long long>

#define pb push_back
#define mp make_pair

#define ff first
#define ss second

#define foreach(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();it++)

#define all(x) x.begin(),x.end()

#define ll long long

#define INF 3f3f3f3f
#define MOD 1000000007
#define MAXN 1005
using namespace std;

ll BIT[MAXN],N;

void update(ll ind,ll val)
{
	for(;ind<=N; ind+=(ind&(-ind)))
	 BIT[ind] += val;
}

ll query(ll ind)
{
	ll sum=0;
	for(;ind>0;ind-= (ind&(-ind)))
	{
	    sum+=BIT[ind];
	}
	return sum;
}

int main()
{
	//N = 1002;
	freopen("A-large.in","r",stdin);
	freopen("out1.txt","w",stdout);
    N = 1002;
	int T;
	scanf("%d",&T);
	int t=1;
	while(T--)
	{
		printf("Case #%d: ",t++);
		string s;
		cin >> s;
		
		//scanf("%s",&s);
		int K;
		cin >> K;
		//scanf("%d",&K);
		memset(BIT,0,sizeof(BIT));
		
		int fg=0;
		int  cou=0;
		for(int i=0;i<s.size();i++)
		{
			int count = query(i+1) ;
			if(i>=K)
			 count  = count - query(i-K+1);
			//cout  << "count " << count << " ";
			if(count%2)
			{
				if(s[i]=='-')
				 s[i]='+';
				else s[i] ='-';
			}
			
			//cout  << s[i] << " ";
			if(s[i]=='-')
			{
				   if(K <= s.size()-i )
				   {
				     update(i+1,1);
					 
				   }
				   else 
				   {
				   	fg=1;
				   	break;
				   }
				   cou++;		
			}
			else 
			{
					
			}
		}
		if(fg)
		 printf("IMPOSSIBLE\n");
		else printf("%d\n",cou);
	}
	
	return 0;
}

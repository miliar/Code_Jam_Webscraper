# include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;

// Input macros
#define s(n)                        scanf("%d",&n)
#define p(n)                        printf("%d\n",n)
#define pl(n)                       printf("%lld\n",n);
#define INF                         (int)1e9
#define EPS                         1e-9
// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())
#define DBG(vari) cerr<<#vari<<" = "<<(vari)<<endl;
#define mod 1000000007LL

// Useful container manipulation / traversal macros
#define all(n)                      for(int i=0;i<n;i++)
#define alls(m)                     for(int j=0;j<m;j++)
#define rep(a,n)                    for(int i=a;i<n;i++)
#define each(v, c)               	for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all1(a)                     a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                   memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
#define init(Arr) memset((Arr), 0, sizeof (Arr))


int cases,a,b,c,d,i,j,k,n,m,t,ar[1000001],flag,w[1010][1010],cur=0,ans;
string ch,ch2;
pii p;

bool myfunction (int i,int j) { return (i<j); }

int main()
{
   
   	 freopen("in.txt","r",stdin);
	 freopen("out.txt","w",stdout);	
	s(cases);
	
	for(t=1;t<=cases;t++)
	{
		printf("Case #%d: ",t);
		cin>>ch;
		s(m);
		n=ch.size();
		
		ans=0;
		cur =0 ;
		for(i=0;i<n-m+1;i++){

			if(ch[i] == '-'){
				ans++;
				for(j=i;j<i+m;j++){
					if(ch[j] == '-')
						ch[j] = '+';
					else
						ch[j]='-';
				}

			}

		}

		for(i=0;i<n;i++){
			if(ch[i] == '-')
			{
				cur =1;
				cout<<"IMPOSSIBLE\n";
				break;
			}
		}
		
		if(cur == 0)
			cout<<ans<<"\n";
			
	}
		
	
return 0;	
		
}
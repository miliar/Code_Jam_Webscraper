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
#define each(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all1(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
#define init(Arr) memset((Arr), 0, sizeof (Arr))

int convert(char c) {
	return (int)(c) - (int)('0');
}

char conchar(int i) {
	return (char)(i+(int)('0'));
}

int main() 
{

	int cases;

	s(cases);

	for(int t=1;t<=cases;t++) {
		printf("Case #%d: ", t);

		char num[20];
		scanf("%s",num);

		int n = strlen(num);

		int right = convert(num[n-1]);

		for(int i=n-2;i>=0;i--) 
		{
			int cur = convert(num[i]);
			if(right < cur) 
			{
				num[i] = conchar(cur-1);
				right = cur-1;

				for(int j=i+1;j<n;j++)
					num[j]='9';
			}
			else if(cur < right)
				right = cur;
		}

		int j = 0;
		while(num[j] == '0')
			j++;

		while(j<n)
		{
			printf("%c", num[j]);
			j++;
		}
		cout<<endl;
	}

	return 0;
}
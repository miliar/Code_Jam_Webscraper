#include <bits/stdc++.h>
 using namespace std;
typedef long long int ll ;
typedef long double ld;

#define MOD 1000000007ll
#define all(v) v.begin() , v.end()
#define allr(v) v.rbegin(), v.rend()
#define for0(i,n) for(__typeof(n) i = 0; i < n ; i++) 
#define forab(i,a,b) for(__typeof(a) i = a ; i < b ; i++) 
#define forba(i,b,a) for(__typeof(a) i = b ; i > a ; i--) 
#define forc(c,it) for(__typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define pb     push_back
#define mp     make_pair
#define MAX 100005

int n , k;
string s;

bool check(string s)
{
	int siz = s.size();

	for(int i = 0 ; i < siz ; i++)
	{
		if(s[i] == '-')
			return false;
	}
	return true;
}

int main(int argc, char const *argv[])
{
  ios_base::sync_with_stdio(false);
  
  #ifndef ONLINE_JUDGE
  freopen("in","r",stdin);
  freopen("out","w",stdout);
  #endif

  cin>>n;

  for(int i = 1 ; i <= n ; i++)
  {
  	cin>>s>>k;
  	int siz = s.size();
  	int ans = 0;

  	for(int j = 0 ; j < siz ; j++)
  	{
  		if(s[j] == '-' && ((j+k) <= siz))
  		{
  			ans++;

  			for(int l = j ; l < j+k ; l++)
  			{
  				if(s[l] == '-')
  					s[l] = '+';
  				else
  					s[l] = '-';
  			}	
  		}
  	}

  	if(check(s))
  		printf("Case #%d: %d\n" , i, ans);
  	else
  		printf("Case #%d: IMPOSSIBLE\n", i);
  }



  return 0;
}  
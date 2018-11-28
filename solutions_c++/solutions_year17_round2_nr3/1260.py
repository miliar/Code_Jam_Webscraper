#include <bits/stdc++.h>
 using namespace std;
typedef long long int ll ;
typedef long double ld;

#define MOD 1000000007ll
#define all(v) v.begin() , v.end()
#define allr(v) v.rbegin(), v.rend()
#define for0(i,n) for(__typeof(n) i = 0; i < n ; i++)  
#define forc(c,it) for(__typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define pb     push_back
#define mp     make_pair
#define MAX 100005
template<typename T, template<typename ELEM, typename ALLOC=std::allocator<ELEM> > class Container>
std::ostream& operator<< (std::ostream& o, const Container<T>& container)
{ typename Container<T>::const_iterator beg = container.begin();
  /*o << "[";*/ while(beg != container.end()) o << " " << *beg++; /*o << " ]";*/ return o; }

int t , n , q, d, s;
vector<pair<int,int> >horses;
int route[105][105];
int u , v;

int main(int argc, char const *argv[])
{
  ios_base::sync_with_stdio(false);
  
  #ifndef ONLINE_JUDGE
  freopen("in","r",stdin);
  freopen("out","w",stdout);
  #endif

  scanf("%d" , &t);

  for(int i = 1 ; i <= t ; i++)
  {
  	printf("Case #%d: " , i);

  	scanf("%d %d" , &n , &q);

  	horses.pb(mp(0 , 0));

  	for(int j = 0 ; j < n ; j++)
  	{
  		scanf("%d %d" , &d , &s);
  		horses.pb(mp(d , s));
  	}

  	for(int j = 0 ; j < n ; j++)
  	{
  		for(int k = 0 ; k < n ; k++)
  		{
  			scanf("%d" , &d);
  			route[j+1][k+1] = d;
  		}
  	}

  	while(q--)
  	{
  		scanf("%d %d" , &s , &d);
	  	vector<double> dp(n+2 , 1e14);
	  	dp[s] = 0;

	  	for(int j = s ; j <= d ; j++)
	  	{
	  		for(int k = s ; k < j ; k++)
	  		{
	  			double dist = 0;

	  			for(int l = k ; l <= j-1 ; l++)
	  				dist += route[l][l+1];

	  			int hdist = horses[k].first;

	  			if(dist != -1 && hdist >= dist)
	  			{
	  				dp[j] = min(dp[j] , dp[k] + (dist / horses[k].second));
	  			}
	  		}
	  	}

	  	printf("%lf\n" , dp[d]);
  		
  	}

  	horses.clear();
  }



  return 0;
}
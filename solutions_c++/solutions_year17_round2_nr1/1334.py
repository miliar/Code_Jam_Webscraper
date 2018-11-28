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

int t , d , n;
double dist, speed;

int main(int argc, char const *argv[])
{
  ios_base::sync_with_stdio(false);
  
  #ifndef ONLINE_JUDGE
  freopen("in","r",stdin);
  freopen("out","w",stdout);
  #endif

  cin >> t;

  for(int i = 1 ; i <= t ; i++)
  {
  	double tim = 0;
  	cin >> d >> n;

  	for(int j = 0 ; j < n ; j++)
  	{
  		cin >> dist >> speed;
  		dist = d - dist;
  		double ti = dist/speed;

  		tim = max(tim , ti);
  	}

  	double ans = d / tim;

  	printf("Case #%d: %lf\n" , i , ans);

  }



  return 0;
} 
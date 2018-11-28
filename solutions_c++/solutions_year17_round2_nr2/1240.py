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

int t, n , r , o , y , g , b , vo;
bool solved;


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
  	cin >> n >> r >> o >> y >> g >> b >> vo;
  	solved = false;

	cout << "Case #" << i << ": ";

	vector<pair<int , char> >v;
	v.pb(mp(r , 'R'));
	v.pb(mp(b , 'B'));
	v.pb(mp(y , 'Y'));

	sort(all(v));
	string ans;

	if(v[2].first > v[1].first + v[0].first) 
  		cout << "IMPOSSIBLE\n";
  	else
  	{
  		int x = v[2].first;
  		int y = v[1].first + v[0].first - v[2].first;
  		
  		while(v[2].first > 0)
  		{
  			ans.pb(v[2].second);
  			v[2].first--;

  			if(y > 0)
  			{
  				ans.pb(v[1].second);
  				ans.pb(v[0].second);
  				y--;
  				v[1].first--;
  				v[0].first--;
  			}
  			else if(v[1].first > 0)
  			{
  				ans.pb(v[1].second);
  				v[1].first--;
  			}
  			else
  			{
  				ans.pb(v[0].second);
  				v[0].first--;
  			}

  		}

  		cout << ans << endl;


  	}

  }

  return 0;
}  
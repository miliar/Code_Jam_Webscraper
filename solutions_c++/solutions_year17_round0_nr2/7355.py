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

int t;
ll i , n;

bool tidy(vector<int> s)
{
	int siz = s.size();

  for(int i = 0 ; i < siz-1 ; i++)
  {
    if(s[i+1] < s[i])
      return false;
  }
   return true;
}

void print(vector<int> s)
{
  int siz = s.size();
  int i;

  for(i = 0 ; i < siz ; i++)
  {
    if(s[i] != 0)
      break;
  }

  for(int j = i ; j < siz ; j++)
    printf("%d" , s[j]);
}

int main(int argc, char const *argv[])
{
  ios_base::sync_with_stdio(false);
  
  #ifndef ONLINE_JUDGE
  freopen("in","r",stdin);
  freopen("out","w",stdout);
  #endif
  
  scanf("%d" , &t);
  
  for(int j = 1 ; j <= t ; j++)
  {
  	scanf("%lld" , &n);

    ll temp = n;
    vector<int> s;

    while(temp > 0)
    {
      s.pb(temp%10);
      temp = temp / 10;
    }

    reverse(all(s));

    while(1)
    {
      if(tidy(s))
      {
        printf("Case #%d: " , j);
        print(s);
        printf("\n");  
        break;
      }
      
      int k = s.size() - 1;

      while(k >= 0)
      {
        if(s[k] != 9)
        {
            s[k] = 9;
            int l = k - 1;

            while(l >= 0)
            {
                if(s[l] != 0)
                {
                  s[l]--;
                  break;
                }
                else
                {
                  s[l] = 9;
                  l--;
                }
            }

          break;

        }
        else 
          k--;
      }

    }

  }

  return 0;
}  


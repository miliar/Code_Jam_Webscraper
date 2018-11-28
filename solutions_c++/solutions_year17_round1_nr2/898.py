#include <algorithm>
#include <vector>
#include <climits>
#include <iostream>
#include<set>

using namespace std;
const int MAXN = 200;

multiset<long long> s[MAXN];
long long r[MAXN];
vector<pair<long long, pair<int , int> >  > v;

long long lef[MAXN][MAXN] , rig[MAXN][MAXN];

int main() {
    int T;
    cin >> T;
    for(int t = 0;t < T;t ++)
    {
      int n, p;
      cin >> n >> p;

      for(int i = 1;i <= n;i ++)
        s[i].clear();
      v.clear();


      for(int i = 1;i <= n;i ++)
        cin >> r[i];

      for(int i = 1;i <= n;i ++)
        for(int j = 1;j <= p;j ++)
        {
          long long a;
          cin >> a;

          long long be = 1 , en = 1e9;
          long long m1 = -1;

          while(be <= en)
          {
            long long mid = (be + en) / 2;
            if(mid * 90 * r[i] <= a * 100)
            {
              m1 = mid;
              be = mid + 1;
            }
            else
              en = mid - 1;
          }
          long long m2 = -1;
          be = 1 , en = 1e9;

          while(be <= en)
          {
            long long mid = (be + en) / 2;
            if(mid * 110 * r[i] >= a * 100)
            {
              m2 = mid;
              en = mid - 1;
            }
            else
              be = mid + 1;
          }

          lef[i][j] = m2 , rig[i][j] = m1;
          if(m1 >= m2 && m1 != -1 && m2 != -1)
          {
            v.push_back(make_pair(min(m1 , m2) , make_pair(i , j)));
            v.push_back(make_pair(max(m1 , m2) + 1 , make_pair(-i , j)));
          }
        }


      sort(v.begin() , v.end());

      int cnt = 0;
      int ans = 0;

      for(int i = 0;i < (int)v.size();i ++)
      {
        int pos = i;

        while(pos < (int)v.size() && v[pos].first == v[i].first)
        {
          int ind = v[pos].second.first;
          if(ind < 0) ind = -ind;

          int j = v[pos].second.second;

          if(v[pos].second.first > 0)
          {
            s[ind].insert(rig[ind][j] + 1);
            if(s[ind].size() == 1)
              cnt ++;
          }
          else
          {
            if(s[ind].find(v[pos].first) != s[ind].end())
            {
              s[ind].erase(s[ind].find(v[pos].first));
              if(s[ind].size() == 0)
                cnt --;
            }
          }
          pos ++;
        }

        i = pos - 1;

        while(cnt == n)
        {
          for(int j = 1;j <= n;j ++)
          {
            s[j].erase(s[j].begin());
            if(s[j].size() == 0)
              cnt --;
          }
          ans ++;
        }

      }
      cout << "Case #" << t + 1 << ": " << ans << endl;
    }
}

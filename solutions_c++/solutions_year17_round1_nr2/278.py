#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, p;
int search(pair<int,int> serv[50][50], vector<int> &startpoint)
{
  if (startpoint[0] == p)
    return 0;
  vector<int> ori = startpoint;
    for (int s=serv[0][startpoint[0]].first; s<=serv[0][startpoint[0]].second; s++)
    {
      int i;
      for (i=1; i<n; i++)
      {
        while (startpoint[i] < p && serv[i][startpoint[i]].second < s)
          startpoint[i]++;
        if (startpoint[i] == p || serv[i][startpoint[i]].first > s)
        {
          startpoint = ori;
          break;
        }
        if (serv[i][startpoint[i]].first <= s)
          ;
      }
      if (i==n)
      {
        for (int i=0; i<n; i++)
          startpoint[i] ++;
        return 1+search(serv, startpoint);
      }
      else
        ;
    }
    startpoint[0] ++;
  return search(serv, startpoint);
}
int main()
{
	int tc;
	cin >> tc;
  for (int tt=1; tt<=tc; tt++)
  {
    cin >> n >> p;
    int cost[50];
    for (int i=0; i<n; i++)
      cin >> cost[i];
    int avail[50][50];
    for (int i=0; i<n;i++)
      for (int j=0;j<p;j++)
        cin >> avail[i][j];
    pair<int,int> serv[50][50];
    for (int i=0; i<n; i++)
      for (int j=0; j<p; j++)
      {
        int be, ed;
        if (10*avail[i][j] % (11*cost[i]) == 0)
          be = (10*avail[i][j] / (11*cost[i]));
        else
          be = (10*avail[i][j] / (11*cost[i]))+1;
        ed = (10*avail[i][j] / (9*cost[i]));
        if (be <= ed)
          serv[i][j]=make_pair(be,ed);
        else
          serv[i][j] = make_pair(-1,-2);
        
      }
    for (int i=0; i<n; i++)
      sort(serv[i], serv[i]+p);
    vector<int> start(n,0);
    int res = search(serv, start);

    cout << "Case #" << tt << ": " << res << endl;
  }
}

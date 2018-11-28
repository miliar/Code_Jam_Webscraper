// DISCLAIMER: maximal Bipartite matching algo from http://www.geeksforgeeks.org/maximum-bipartite-matching/
// A C++ program to find maximal Bipartite matching.
#include <iostream>
#include <string.h>
#include<cstdio>
#include<algorithm>
using namespace std;
 
// M is number of applicants and N is number of jobs
#define M 10
#define N 10
 
// A DFS based recursive function that returns true if a
// matching for vertex u is possible
bool bpm(bool bpGraph[M][N], int u, bool seen[], int matchR[])
{
    // Try every job one by one
    for (int v = 0; v < N; v++)
    {
        // If applicant u is interested in job v and v is
        // not visited
        if (bpGraph[u][v] && !seen[v])
        {
            seen[v] = true; // Mark v as visited
 
            // If job 'v' is not assigned to an applicant OR
            // previously assigned applicant for job v (which is matchR[v]) 
            // has an alternate job available. 
            // Since v is marked as visited in the above line, matchR[v] 
            // in the following recursive call will not get job 'v' again
            if (matchR[v] < 0 || bpm(bpGraph, matchR[v], seen, matchR))
            {
                matchR[v] = u;
                return true;
            }
        }
    }
    return false;
}
 
// Returns maximum number of matching from M to N
int maxBPM(bool bpGraph[M][N])
{
    // An array to keep track of the applicants assigned to
    // jobs. The value of matchR[i] is the applicant number
    // assigned to job i, the value -1 indicates nobody is
    // assigned.
    int matchR[N];
 
    // Initially all jobs are available
    memset(matchR, -1, sizeof(matchR));
 
    int result = 0; // Count of jobs assigned to applicants
    for (int u = 0; u < M; u++)
    {
        // Mark all jobs as not seen for next applicant.
        bool seen[N];
        memset(seen, 0, sizeof(seen));
 
        // Find if the applicant 'u' can get a job
        if (bpm(bpGraph, u, seen, matchR))
            result++;
    }
    return result;
}

int qi[2];

bool canMakeKit(int q1, int q2) {
  int x = max(q1/qi[0], q2/qi[1]);
  for(int i=1;i<=x+3;i++) {
    if ( (1.0*q1 >= 0.9*i*qi[0] && 1.0*q1 <= 1.1*i*qi[0]) && (1.0*q2 >= 0.9*i*qi[1] && 1.0*q2 <= 1.1*i*qi[1])) 
      return true;
  }
  return false;
}

bool canAlone(int q1) {
  int x = q1/qi[0];
  for(int i=1; i <= x+3   ;i++) {
    if ( (1.0*q1 >= 0.9*i*qi[0] && 1.0*q1 <= 1.1*i*qi[0])) 
      return true;
  }
  return false;
}

// Driver program to test above functions
int main()
{
    int t;
    cin >> t;
    for(int caso = 1; caso<=t;caso++) {
      int n, p; 
      cin >> n >> p;
      if( n==1) {
        cin >> qi[0];
        int ret = 0;
        for(int i=0;i<p;i++) {
          int x;
          cin >> x;
          if(canAlone(x))
            ret++;
        }
          printf("Case #%d: %d\n", caso, ret);
      } else {
        cin >> qi[0] >> qi[1];
        int tab[2][10];
        for(int i=0;i<2;i++)
          for(int j=0;j<p;j++)
            cin >> tab[i][j];
        bool  bpGraph[M][N];
        memset(bpGraph,0,sizeof(bpGraph));
        for(int i=0;i<p;i++)
          for(int j=0;j<p;j++) {
            if(canMakeKit(tab[0][i], tab[1][j]))
             bpGraph[i][j] = 1;
            else bpGraph[i][j] = 0;
          }
        printf("Case #%d: %d\n", caso, maxBPM(bpGraph));   
      }
    }
    return 0;
}

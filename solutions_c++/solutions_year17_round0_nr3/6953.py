#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

struct stall 
{
  int L;
  int R;
  bool occupied;
  
  int min()
  {
    return std::min(L,R);
  }
  
  int max()
  {
    return std::max(L,R);
  }
};

void solve()
{
  int N; cin >> N;
  int K; cin >> K;
  
  // construct stalls
  vector<stall> stalls(N);
  
  for(int i = 0; i < N; i++)
  {
    stalls[i].L = i;
    stalls[i].R = (N - i) - 1;
    stalls[i].occupied = false;
  }
  
  for(int k = 0; k < K; k++)
  {
    int bestIndex = -1;
    
    for(int n = 0; n < N; n++)
    {
      if(!stalls[n].occupied)
      {
        // if first available, assume OK
        if(bestIndex == -1)
        {
          bestIndex = n;
          continue;
        }

        // check if better
        int curMin = stalls[bestIndex].min();
        int newMin = stalls[n].min();
                
        if(newMin > curMin)
        {
          //cout << n << " WINS: " << newMin << " vs " << curMin << endl;
          bestIndex = n;
          continue;
        }
        
        int curMax = stalls[bestIndex].max();
        int newMax = stalls[n].max();
                
        if(curMin == newMin && newMax > curMax)
        {
          bestIndex = n;
          continue;
        }
      }
    }
    
    if(bestIndex == -1)
    {
      cout << "FATAL ERROR" << endl;
      return;
    }
    
    
    //cout << bestIndex << " is winner" << endl;
    
    if(k == K - 1)
    {
      cout << stalls[bestIndex].max() << " " << stalls[bestIndex].min() << endl;
      return;
    }
    
    // set occupied
    stalls[bestIndex].occupied = true;
    
    
    // update stalls
    int left = bestIndex - 1;
    while(left >= 0)
    {
      stalls[left].R = bestIndex - left - 1;
      if(stalls[left].occupied)
      {
        break;
      }      
      left--;
    }
    
    int right = bestIndex + 1;
    while(right < N)
    {
      stalls[right].L = right - bestIndex - 1;
      if(stalls[right].occupied)
      {
        break;
      }      
      right++;
    }
    
    // debug: print stalls
    /*for(int i = 0; i < N; i++)
    {
      if(!stalls[i].occupied)
      {
        //cout << "Stal #" << i << ": " << stalls[i].L << " - " << stalls[i].R << endl;
      }
    }
    */
  }
}


int main()
{ 
  int n; cin >> n;
  for(int i = 1; i <= n; i++)
  {
    cout << "Case #" << i << ": ";
    solve();
  }
}
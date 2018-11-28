#include <iostream>
#include <string>
#include <map>
#include <queue>
using namespace std;

string flip(string state, int i, int k)
{
  //cout << "Pre-state: " << state << endl;
  for(int j = 0; j < k; j++)
    {
      if(state[j + i] == '-')
	state[j + i] = '+';
      else
	state[j + i] = '-';
    }
  //cout << "Post-state: " << state << endl;
  return state;
}

void popNextStates(queue<pair<string, int> > *nxtStates, string state,
		   int numFlips, int k)
{
  for(int i = 0; i < state.length() - k + 1; i++)
    nxtStates->push(pair<string, int>(flip(state, i, k), numFlips + 1));
}

bool chkHappy(string state)
{
  for(int i = 0; i < state.length(); i++)
    if(state[i] != '+')
      return false;
  return true;
}
      
int calcNumFlips(string start, int k)
{
  map<string, int> minFlips;
  queue<pair<string, int> > nxtStates;
  nxtStates.push(pair<string, int>(start, 0));

  while(!nxtStates.empty())
    {
      string curState = nxtStates.front().first;
      int numFlips = nxtStates.front().second;
      
      nxtStates.pop();
      if(minFlips.find(curState) == minFlips.end())
	{
	  if(chkHappy(curState))
	    return numFlips;
	  minFlips[curState] = numFlips;
	  popNextStates(&nxtStates, curState, numFlips, k);
	}
    }

  return -1;
}

int main() {

  int t;
  cin >> t;  
  for (int i = 1; i <= t; i++) {
    int k;
    string start;
    cin >> start >> k;
    int numFlips = calcNumFlips(start, k);
    cout << "Case #" << i << ": ";
    if (numFlips > -1)
      cout << numFlips;
    else
      cout << "IMPOSSIBLE";
    cout << endl;
  }

  return 0;
}

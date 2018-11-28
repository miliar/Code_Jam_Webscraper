#include <iostream>
#include <string>

using namespace std;

void solve(string, int, int);
string flip(string, int, int);


int main()
{
   int cases;
   cin >> cases;

   for(int i = 0; i < cases; i++)
   {
      string S;
      int K;
      int end;
      
      cin >> S;
      cin >> K;
      end = S.length();

      cout << "Case #" << i+1 << ": ";

      solve(S, K, end);
   }
 
   return 0;
}	 

string flip(string S, int start, int end)
{
   for(int i = start; i < end; i++)
   {
      if(S[i] == '+')
	 S[i] = '-';
      else
	 S[i] = '+';
   }

   return S;
}

void solve(string S, int K, int end)
{
   int flips = 0;
      
   for(int i = 0; i <= end-K; i++)
   {
      if(S[i] != '+')
      {
	 S = flip(S, i, i+K);
	 flips++;
      }
   }

   int numPos = 0;
   for(int i = 0; i < end; i++)
      if(S[i] == '+')
	 numPos++;
   
   if(numPos == end)
      cout << flips << endl;
   else
      cout << "IMPOSSIBLE" << endl;
}

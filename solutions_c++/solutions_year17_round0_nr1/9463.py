#include<iostream>
#include<string>

using namespace std;

string flipPancakes(string input, int k)
{
  int n=input.length(),curr=0;
  int first_negative, negative_length=0;
  int result=0;
  if(n==0)
  	return "0";
  if(n<k)
    return "IMPOSSIBLE";
  while(curr<n)
  {
      if(input[curr]=='+')
        curr++;
      else
      {
        negative_length = curr+k-1;
        if((curr+k-1)>=n)
          return "IMPOSSIBLE";
        else
        {
          while(input[curr]=='-' && curr<=negative_length)
          {
            input[curr] = '+';
            curr++;
          }
          first_negative = curr;
          while(curr<=negative_length)
          {
            if(input[curr] == '-')
              input[curr] = '+';
            else
              input[curr] ='-';
            curr++;
          }
        }
        result++;
        curr = first_negative;
      }
  }

  return to_string(result);
}

int main()
{
  int T,t,k;
  string input;
  cin >> T;
  for(t=0;t<T;t++)
  {
    cin>> input >> k;
    cout << "Case #" << (t+1) << ": " << flipPancakes(input,k) << endl;
  }

  return 0;
}

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

string replace(string s, int position, int length) {
	for (int i = 0; i < length; ++i)
	{
		if (s.length()-1 >= position+i)
		{
			if (s[position+i] == '+')
			{
				s[position+i] = '-';
			} else {
				s[position+i] = '+';
			}
		}
	}
	return s;
}

int main(int argc, char **argv) {
  int t, K, counter;
  string S;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

  bool tidy1,tidy2;

  for (int i = 1; i <= t; ++i) {
    cin >> S >> K;
    tidy1 = true;
    tidy2 = true;

  	counter = 0;
    for (int j = 0; j < S.length(); ++j)
    {
    	if (S[j] == '-')
    	{
			tidy1 = false;
			break;
    	}
    }

   //  if (S[0] == '-')
   //  {
   //  	S = replace(S, 0, K);
   //  }

   //  if (S[S.length()-1] == '-')
   //  {
   //  	S = replace(S, S.length() - K, K);
   //  }

    for (int j = 0; j < S.length() - K; ++j)
    {
    	if (S[j] == '-')
    	{
    		S = replace(S, j, K);
    		counter++;
    	}
    }

    if (S[S.length()-1] == '-')
    {
     	S = replace(S, S.length() - K, K);
     	counter++;
    }

    for (int j = 0; j < S.length(); ++j)
    {
    	if (S[j] == '-')
    	{
    		tidy2 = false;
    	}
    }


    cout << "Case #" << i << ": " << (tidy1 ? "0" : (tidy2 ? std::to_string(counter) : "IMPOSSIBLE"))  << endl;
  }
}
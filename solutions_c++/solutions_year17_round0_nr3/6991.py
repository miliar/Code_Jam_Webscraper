#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

void insert( vector<int> &cont, int value ) {
    vector<int>::iterator it = std::lower_bound( cont.begin(), cont.end(), value, std::less<int>() );
    cont.insert( it, value );
}

int main()
{

int cases;
cin>> cases;

for( int caseNum = 1; caseNum <= cases; caseNum++ )
{
  vector<int> gaps;

  long long stals, people, left, right;
  cin>> stals>> people;
  insert( gaps, stals);

  for( int person = 0; person < people; person++ )
  {
    left = ceil( (gaps.back()-1)/2.0 );
    right = floor( (gaps.back()-1)/2.0 );
//cout<< gaps.back()<< " = "<< left<< " + "<< right<< " +1\n"; 
    gaps.pop_back();
    insert( gaps, left);
    insert( gaps, right);
  }

  cout<< "Case #"<< caseNum<< ": "<< left<< " "<< right<< endl;
}

return 0;
}

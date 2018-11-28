#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <queue>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main()
{

  long long int sortcount = 1;
	long long int t,Case = 1, n, m, max,min,counter = 1;
  cin >> t;


  while(t != 0)
  {
  
    map<long long int,long long int> mymap;
    //  X  Y 
    //X is the value inserted
    //Y is the number of times itis there
    queue<long long int> values;

    t--;
  	long long int people, n;
  	cin >> n >> people;

    mymap[n] = 1;
    values.push(n);
    while(people != 0)
    {
      long long int current = values.front();
      values.pop();
      //cout << current << endl;
      //people--;
      if(current % 2 == 0)
      {
        max = current / 2;
        if(max == 0)
          min = 0;
        else
          min = max - 1;
      }
      else
      {
        max = min = current / 2;
      }

      if( people - mymap[current] >= 0)
      {
        if(max != min)
        {
          if( mymap[max] == 0 )
          {
            values.push(max);
          }
          if( mymap[min] == 0 )
          {
            values.push(min);
          }

          mymap[max] += mymap[current];
          mymap[min] += mymap[current];
          
        }
        else
        {
          if( mymap[max] == 0 )
          {
            values.push(max);
          }
          mymap[max] += mymap[current]*2;
        }
        people = people - mymap[current];

      }
      else // if ( people - mymap[current] < 0 )
      {
        people = 0;
      }
      

    }
  	cout << "case #" << Case++ << ": "<< max << " " << min << endl;
  	values.empty();
	}
}
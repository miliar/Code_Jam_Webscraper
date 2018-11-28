
#include <iostream>


#include <algorithm>
#include <numeric>  // accumulate
#include <fstream>
#include <vector>
#include <string>

#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
// GCJ Challenge 2017
//


using namespace std;


#define SMALL_INPUT_FILE "C-small-2-attempt0.in"
#define LARGE_INPUT_FILE "C-large.in"
#define OUTPUT_FILE "bathroomstalls-output.txt"
#define FILENAME_SIZE 20


typedef long long ll;
typedef pair< ll, ll> range;

typedef pair< ll, range > stall_range;

class Compare
{
  public:

      bool operator() ( stall_range & item1,stall_range & item2  )
      {

          if(item1.first != item2.first)
          {
              return (item1.first < item2.first);
          }

          else
          {

              return (item1.second.first > item2.second.first);
          }
      }

};


int main()
{





    fstream  inpfd ,outfd ;
	char inputfile[FILENAME_SIZE];
	char ch;
	inputfile[FILENAME_SIZE - 1] = '\0';
	string inp;
	cout << inputfile[3];
 /*
	if (argc > 1 )
	{
		// not overflow safe --> get string length of destination
		strncpy( inputfile , argv[1] , strlen( argv[1] ) );
	}
	*/
    cin >> ch ;

    if ( ch == 's' )
    {
		inpfd.open( SMALL_INPUT_FILE ,ios::in);
	}
	else
	{
		inpfd.open( LARGE_INPUT_FILE ,ios::in);
	}


	outfd.open( OUTPUT_FILE , ios::out );

	if ( ! inpfd )
	     printf("Not opened\n");


	int T, i = 1 ;

    ll K,N,midans;
    priority_queue <stall_range, vector<stall_range>, Compare> stallQ;


	inpfd >> T;

	ll ls,rs;
	while(T-->0)
    {
       inpfd >> N >> K;

       stallQ = priority_queue <stall_range, vector<stall_range>, Compare>();
       stallQ.push(make_pair(N,make_pair(0,N+1)));
       stall_range maxr;

       while(K-->0)
       {
          maxr = stallQ.top();
          stallQ.pop();

          midans = maxr.second.first +( maxr.second.second-maxr.second.first) / 2;

          ls = midans - maxr.second.first- 1;
          rs = maxr.second.second- midans - 1;


          stallQ.push(make_pair(ls , make_pair(maxr.second.first,midans )));
          stallQ.push(make_pair(rs , make_pair(midans ,maxr.second.second)));



       }

        outfd << "Case #" << i++ << ": " << max(ls,rs) << " " << min(ls,rs) << "\n";



    }


	inpfd.close();
	outfd.close();


	return 0;
}
